from wsgiref.simple_server import make_server
from urllib import parse, request
import ddddocr, sys, getopt, re, base64

def getImgBytes(imgParam):
    if re.match(r'^http', imgParam) != None:
        resp = request.urlopen(imgParam)
        img_bytes = bytearray(resp.read())
    elif re.search(r'(\.jpg|\.jpeg|\.png|\.gif)$', imgParam) != None:
        with open(imgParam, 'rb') as f:
            img_bytes = f.read()
    else:
        img_bytes = base64.b64decode(imgParam)
        pass
    return img_bytes

def deCodeImg(imgBytes):
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(imgBytes)
    return res

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html'),('Access-Control-Allow-Origin', '*')])
    if environ["PATH_INFO"] == "/":
        params = parse.parse_qs(environ["QUERY_STRING"])
        if "img" not in params:
            return [b'--- DeCodeImg Server Started ---<br>Powered by hoothin<br>http://127.0.0.1:416/?img=c:/codeimg.png<br>http://127.0.0.1:416/?img=http://a.a/codeimg.png<br>http://127.0.0.1:416/?img=Base64 Data']
        action = "getCode"
        if "action" in params.keys():
            action = params["action"][0]
        if action == "getCode":
            try:
                result=deCodeImg(getImgBytes(params["img"][0]))
            except:
                return [b'Image data is incorrect!']
            return [str.encode(result)]
    return [b'1']


def main(argv):
    port = 416
    makeServer = False
    imgParam = ""
    try:
        opts, args = getopt.getopt(argv,"hi:mp:",["ifile=", "makeServer", "port="])
    except getopt.GetoptError:
        print('deCodeImg.py -i <imgParam> or deCodeImg.py -m <makeServer> -p <port>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('deCodeImg.py -i <imgParam> or deCodeImg.py -m <makeServer> -p <port>')
            sys.exit()
        elif opt in ("-i", "--imgParam"):
            imgParam = arg
            print(deCodeImg(getImgBytes(imgParam)))
            sys.exit()
        elif opt in ("-m", "--makeServer"):
            makeServer = True
        elif opt in ("-p", "--port"):
            port = arg
    if makeServer == True:
        print('--- DeCodeImg Server Started ---\nPowered by hoothin\nhttp://127.0.0.1:416/?img=c:/codeimg.png\nhttp://127.0.0.1:416/?img=http://a.a/codeimg.png\nhttp://127.0.0.1:416/?img=Base64 Data')
        httpd = make_server('', port, app)
        httpd.serve_forever()
    elif imgParam == "":
        print('--- DeCodeImg --- \n-h to view help')

if __name__ == "__main__":
   main(sys.argv[1:])