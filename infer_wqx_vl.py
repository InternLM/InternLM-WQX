from PIL import Image
from io import BytesIO
import numpy as np
import requests
import torchvision.transforms as transforms
from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
import torch

def padding_336(b):
    width, height = b.size
    tar = int(np.ceil(height / 560) * 560)
    top_padding = int((tar - height) / 2)
    bottom_padding = tar - height - top_padding
    left_padding = 0
    right_padding = 0
    b = transforms.functional.pad(b, [left_padding, top_padding, right_padding, bottom_padding], fill=[255, 255, 255])

    return b


def HD_transform(img, hd_num=25):
    width, height = img.size
    trans = False
    if width < height:
        img = img.transpose(Image.TRANSPOSE)
        trans = True
        width, height = img.size
    ratio = (width / height)
    scale = 1
    while scale * np.ceil(scale / ratio) <= hd_num:
        scale += 1
    scale -= 1
    new_w = int(scale * 560)
    new_h = int(new_w / ratio)

    img = transforms.functional.resize(img, [new_h, new_w], )
    img = padding_336(img)
    width, height = img.size
    if trans:
        img = img.transpose(Image.TRANSPOSE)

    return img

def process_query_and_image(query, image, model, HD_transform):
    def process_image(img):
        img = img.convert("RGB")
        img = HD_transform(img, hd_num=4)
        img = model.vis_processor(img).unsqueeze(0).cuda().half()
        return model.encode_img(img)

    embeds = []
    im_mask = []
    images_loc = [0]

    for i, pts in enumerate(images_loc + [len(query)]):
        subtext = query[0:pts]
        text_embeds = model.encode_text(subtext, add_special_tokens=True)
        embeds.append(text_embeds)
        im_mask.append(torch.zeros(text_embeds.shape[:2]).cuda())

        if i == 0:
            image_embeds = process_image(image)
            embeds.append(image_embeds)
            im_mask.append(torch.ones(image_embeds.shape[:2]).cuda())

    embeds = torch.cat(embeds, dim=1)
    im_mask = torch.cat(im_mask, dim=1).bool()

    return embeds, im_mask
if __name__ == "__main__":
    model_path = "internlm/internlm2-wqx-vl-20b"
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModel.from_pretrained(model_path, torch_dtype=torch.bfloat16, trust_remote_code=True).cuda().eval()
    model.cuda().half()
    model.tokenizer = tokenizer

    image_url = "https://ks-1302698447.cos.ap-shanghai.myqcloud.com/img/phymerge.png"
    query = "体育课上两位同学在室内羽毛球场进行羽毛球比赛，羽毛球在空中上升的运动轨迹如图中虚线所示，考虑空气阻力，羽毛球加速度方向示意图可能正确的是（\u3000\u3000） \nA:<IMAGE 0>  \nB: <IMAGE 1>  \nC:<IMAGE 2>  \nD:<IMAGE 3> "

    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    embeds, im_mask = process_query_and_image(query, image, model, HD_transform)

    outputs = model.generate(inputs_embeds=embeds, im_mask=im_mask,
                                temperature=0.0, max_new_tokens=256, num_beams=1,
                                do_sample=False, repetition_penalty=1.0)
    output_token = outputs[0]
    output_text = model.tokenizer.decode(output_token, add_special_tokens=False)
    print(output_text)
    #  <s> 斜向下
    # 答案是：C</s>

