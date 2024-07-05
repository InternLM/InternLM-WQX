<div align="center">

<img src="https://raw.githubusercontent.com/InternLM/InternLM/main/assets/logo.svg" width="200"/>
  <div> </div>
  <div align="center">
    <b><font size="5">InternLM2-WQX</font></b>
    <sup>
      <a href="https://internlm.intern-ai.org.cn/">
        <i><font size="4">HOT</font></i>
      </a>
    </sup>
    <div> </div>
  </div>

[![license](https://raw.githubusercontent.com/InternLM/InternLM/main/assets/license.svg)](./LICENSE)



InternLM2-WQX-20B <a href="https://huggingface.co/internlm/internlm2-wqx-20b">🤗</a> <a href="https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-20b/summary"><img src="./assets/modelscope_logo.png" width="20px"></a> ｜ InternLM2-WQX-VL-20B <a href="https://huggingface.co/internlm/internlm2-wqx-vl-20b">🤗</a> <a href="https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-vl-20b/summary"><img src="./assets/modelscope_logo.png" width="20px"></a>
</div>

# Introduction

InternLM2-WQX与InternLM2-WQX-VL是InternLM团队于2024年高考前夕最新推出的文曲星系列模型。

高考覆盖各类学科及题型，同时因其开考前的“绝密性”，被视作中国最具权威的考试之一，成为评估考生综合能力的“试金石”。这一面向人类设计的高难度综合性测试，目前普遍被研究者用于考察大模型的智能水平。InternLM2-WQX系列模型在2024年高考评测集[GAOKAO-Eval](https://github.com/open-compass/GAOKAO-Eval)上取得了优异的成绩，综合表现与GPT-4o相当，且超越了国内外一系列开源大模型，体现了InternLM2-WQX系列模型优秀的性能。

我们即将更新关于文曲星系列模型数据准备的相关说明，敬请期待。


# Model Zoo


| Model                       | HuggingFace                          | ModelScope                           | Release Date |
| --------------------------- | ----------------------------------------- | ---------------------------------------- | ------------ |
| **InternLM2-WQX-20B**          | [🤗internlm2-wqx-20b](https://huggingface.co/internlm/internlm2-wqx-20b) | [<img src="./assets/modelscope_logo.png" width="20px" /> internlm2-wqx-20b](https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-20b/summary) | 2024-06-04   |
| **InternLM2-WQX-VL-20B**          | [🤗internlm2-wqx-vl-20b](https://huggingface.co/internlm/internlm2-wqx-vl-20b) | [<img src="./assets/modelscope_logo.png" width="20px" /> internlm2-wqx-vl-20b](https://modelscope.cn/models/Shanghai_AI_Laboratory/internlm2-wqx-vl-20b/summary) | 2024-06-04   |


## MD5 Check

### LLM权重文件的md5值
```
md5sum ./*
5209adfd6ef7d1724848ff0372362568  ./model-00001-of-00004.safetensors
e37ee2eafecfed543d10dca75998204e  ./model-00002-of-00004.safetensors
ea3da8035b0c2a31c369dd463adf9b52  ./model-00003-of-00004.safetensors
f1ff218f801c69fd4c12c534b64e1b60  ./model-00004-of-00004.safetensors
```

### MLLM权重文件的md5值
```
md5sum ./*
158657dbae9bc369d67cf4bfbdfaaf71  ./pytorch_model-00001-of-00005.bin
c21db8ac1315c10df768f6c3ae3f2825  ./pytorch_model-00002-of-00005.bin
ebc4b0b70e8e9f1adc0b728558d650fb  ./pytorch_model-00003-of-00005.bin
eaa393a66dc632d0a6f0f7d815c439bb  ./pytorch_model-00004-of-00005.bin
7e6e3237d99a7e8bd7ca9ba10747bfdb  ./pytorch_model-00005-of-00005.bin

./clip_l_560_pro7b/*
97b05f40ee9826eda467489eed65f85c  ./clip_l_560_pro7b/pytorch_model.bin
```

# Quick Start

### 快速调用**InternLM2-WQX-20B**语言模型

使用transformers 后端进行推理

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"

tokenizer = AutoTokenizer.from_pretrained("internlm/internlm2-wqx-20b", trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    "internlm/internlm2-wqx-20b",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True
).to(device).eval()

query = "已知圆柱和圆锥的底面半径相等，侧面积相等，且它们的高均为$ \\sqrt { 3 }$，则圆锥的体积为（ ）．\nA. $ 2 \\sqrt { 3 } \\pi$\nB. $ 3 \\sqrt { 3 } \\pi$\nC. $ 6 \\sqrt { 3 } \\pi$\nD. $ 9 \\sqrt { 3 } \\pi$"

inputs = tokenizer(query, return_tensors="pt")

inputs = inputs["input_ids"].to(device)

gen_kwargs = {"max_length": 1024, "do_sample": False}

outputs = model.generate(inputs, **gen_kwargs)
outputs = outputs[0].cpu().tolist()[len(inputs[0]) :]

response = tokenizer.decode(outputs, skip_special_tokens=True)
print(response)
```

使用vllm 后端进行推理：

```python
from vllm import LLM, SamplingParams

model_name = "internlm/internlm2-wqx-20b"
prompts = ["已知圆柱和圆锥的底面半径相等，侧面积相等，且它们的高均为$ \\sqrt { 3 }$，则圆锥的体积为（ ）．\nA. $ 2 \\sqrt { 3 } \\pi$\nB. $ 3 \\sqrt { 3 } \\pi$\nC. $ 6 \\sqrt { 3 } \\pi$\nD. $ 9 \\sqrt { 3 } \\pi$"]
sampling_params = SamplingParams(temperature=0.0, max_tokens=1024)

llm = LLM(
    model=model_name,
    trust_remote_code=True,
    enforce_eager=True,
)

outputs = llm.generate(prompts, sampling_params)

for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, \nGenerated text: {generated_text!r}")
```

### **InternLM2-WQX-20B**语言模型的 Web UI

使用transformers后端进行推理：

```
python basic_demo/web_ui_wqx.py -m internlm/internlm2-wqx-20b
```

### 快速调用**InternLM2-WQX-VL-20B**视觉语言模型

使用transformers后端进行推理:

```python
from PIL import Image
from io import BytesIO
import requests
from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM
import torch
from infer_wqx_vl import process_query_and_image, HD_transform

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
```
针对这个选项里面有图片的考题，我们将图片进行了合并并标记上`<IMAGE {id}>`来让语言模型能理解多图考题。 当前示例展示的是已经拼接好的图片，详细的图像预处理请参考[GAOKAO-Eval](https://github.com/open-compass/GAOKAO-Eval)中的多模态处理工具。

### **InternLM2-WQX-VL-20B**语言模型的 Web UI

使用transformers后端进行推理：

```
python web_ui_wqx_vl.py -m internlm/internlm2-wqx-vl-20b
```

# Citation

```bibtex
@misc{2024internlm2wqx,
    title={https://github.com/InternLM/InternLM-WQX},
    author={InternLM Team},
    howpublished = {\url{https://github.com/InternLM/InternLM-WQX}},
    year={2024}
}
```