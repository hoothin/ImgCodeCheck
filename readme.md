ImgCodeCheck
==========================

---
+ Requirements | 运行环境

Python3 | 安装Python3

pip3 install ddddocr | 安装ddddocr识别库

+ Usage | 用法

    - Local | 本地识别

    deCodeImg.py -i imgParam or deCodeImg.py -m makeServer -p port

    - Web api | 搭建web服务识别

    Start run.cmd | 运行run.cmd，可修改cmd自定义端口等
    
    Visit http://127.0.0.1:416/?img= | 接口为 http://127.0.0.1:416/?img= 后面可接上去头的base64数据、本地图片路径或者在线图片网址
