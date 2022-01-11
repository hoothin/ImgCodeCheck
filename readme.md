ImgCodeCheck 图片验证码识别API
==========================

---
+ Requirements 🔲 运行环境

> Python3 🔲 安装Python3

> pip3 install ddddocr 🔲 安装ddddocr识别库

+ Usage 🔲 用法

  - Local 🔲 本地识别
  > deCodeImg.py -i D:/case.jpg

  - Web api 🔲 搭建web服务识别
  > deCodeImg.py -m -p 416

  > Start run.cmd 🔲 或者直接运行 run.cmd，可修改 cmd 以自定义端口等
    
  > Visit http://127.0.0.1:416/?img= 🔲 接口为 http://127.0.0.1:416/?img= 后面可接上去头的 base64 数据、本地图片路径或者在线图片网址
  
用在[【邀请码助手】](https://chrome.google.com/webstore/detail/register-invitation-code/ndmlflmkmohjoechiepcpflbljadmemp)上时运行 run.cmd 启动服务后填入 http://127.0.0.1:416/?img= 即可
