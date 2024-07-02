ImgCodeCheck 图片验证码识别API
==========================

---
+ Requirements
  - Python 3.9.7
  - pip3 install ddddocr==1.0.6

+ Usage
  - Local: 
  `python3 deCodeImg.py -i D:\codeimg.png`

  - Web api: 
  `python3 deCodeImg.py -m -p 416` or Start run.cmd. 
   Visit `http://127.0.0.1:416/?img=` then.
  
---
+ 运行环境
  - Python 3.9.7
  - ddddocr 1.0.6

+ 安装
  - 安装 [python 3](https://www.python.org/downloads/)
  - 安装 ddddocr 库：打开命令提示符，输入以下命令并回车
  `pip3 install ddddocr==1.0.6`
+ 用法
  - 运行 web 识别服务器，可用于邀请码助手，方法如下：
    
    双击 `run.cmd` 即可
    接口默认为 `http://127.0.0.1:416/?img=` <br>后面可接上 base64 图片数据、本地图片路径或者在线图片网址（预先 encodeURIComponent）
  - 用在[【邀请码助手】](https://chrome.google.com/webstore/detail/register-invitation-code/ndmlflmkmohjoechiepcpflbljadmemp)上时运行 `run.cmd` 启动服务后填入 `http://127.0.0.1:416/?img=` 即可

  - 用于怠惰小说下载器时需要预先设置，[教程](https://afdian.net/p/c7fc3abc8e8411ee9b1852540025c377)

  - 本地识别：使用以下命令可识别本地 `D:\codeimg.png` 里的验证码
    <br>`python3 deCodeImg.py -i D:\codeimg.png`
