# 🐶 Bark

<a href="http://www.repostatus.org/#active"><img src="http://www.repostatus.org/badges/latest/active.svg" /></a>
[![Twitter](https://img.shields.io/twitter/url/https/twitter.com/OnusFM.svg?style=social&label=@OnusFM)](https://twitter.com/OnusFM)
[![](https://dcbadge.vercel.app/api/server/J2B2vsjKuE?compact=true&style=flat&)](https://discord.gg/J2B2vsjKuE)


[Examples](https://suno-ai.notion.site/Bark-Examples-5edae8b02a604b54a42244ba45ebc2e2) | [Model Card](./model-card.md) | [Playground Waitlist](https://3os84zs17th.typeform.com/suno-studio)

Bark is a transformer-based text-to-audio model created by [Suno](https://suno.ai). Bark can generate highly realistic, multilingual speech as well as other audio - including music, background noise and simple sound effects. The model can also produce nonverbal communications like laughing, sighing and crying. To support the research community, we are providing access to pretrained model checkpoints ready for inference.

This repo is a fastAPI Endpoint for Bark. Link to [orignal repo](https://github.com/suno-ai/bark)

<p align="center">
<img src="https://user-images.githubusercontent.com/5068315/230698495-cbb1ced9-c911-4c9a-941d-a1a4a1286ac6.png" width="500"></img>
</p>

## 🔊 Demos

[![Open in Spaces](https://img.shields.io/badge/🤗-Open%20In%20Spaces-blue.svg)](https://huggingface.co/spaces/suno/bark)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1eJfA2XUa-mXwdMy7DoYKVYHI1iTd9Vkt?usp=sharing)

## 🤖 Usage
1. Clone the repo
2. run docker cmd `docker build -t <name_of_image> .`
3. after the build is complete run `docker run -p 9000:9000 bark_api` to start the container
4. The Endpoint is exposed at port `9000` by default (use postman of equivalent for inference.)
5. The inference will return a Audio file (FileResponse class)
