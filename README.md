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

# Citation

```bibtex
@misc{2024internlm2wqx,
    title={https://github.com/InternLM/InternLM-WQX},
    author={InternLM Team},
    howpublished = {\url{https://github.com/InternLM/InternLM-WQX}},
    year={2024}
}
```