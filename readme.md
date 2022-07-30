ImgCodeCheck 图片验证码识别API
==========================

---
+ Requirements
  - Python 3.9.7
  - pip3 install ddddocr==1.0.6

+ Usage
  - Local
  > `python3 deCodeImg.py -i D:\codeimg.png`

  - Web api
  > `python3 deCodeImg.py -m -p 416` or Start run.cmd <br>
  > Visit http://127.0.0.1:416/?img=
  
---
+ 运行环境
> Python 3.9.7 + ddddocr 1.0.6

+ 安装
  - 安装 python 3
  - 安装 ddddocr 库
  > `pip3 install ddddocr==1.0.6`
+ 用法
  - 本地识别
  > `python3 deCodeImg.py -i D:\codeimg.png`

  - 搭建web服务识别，用于邀请码助手
  > 双击 run.cmd 即可<br>
  > 接口为 http://127.0.0.1:416/?img= <br>后面可接上去头的 base64 数据、本地图片路径或者在线图片网址<br>
用在[【邀请码助手】](https://chrome.google.com/webstore/detail/register-invitation-code/ndmlflmkmohjoechiepcpflbljadmemp)上时运行 run.cmd 启动服务后填入 http://127.0.0.1:416/?img= 即可
