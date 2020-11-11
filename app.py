import os
import json
import base64
import subprocess

UUID = "2ac61062-7cad-4d10-b84a-a3e4ac286bd6"
PATH = "/sss"

if __name__ == '__main__':
    with open("source.py","rb") as f:
        with open('app', 'wb') as fi:
            app = base64.b64decode(f.read())
            fi.write(app)
            fi.close()
        f.close()
    
    data = {}

    inbounds = {}
    settings = {}
    clients = {}
    clients["id"] = UUID
    clients["alterId"] = 64
    settings["clients"] = [clients]
    settings["disableInsecureEncryption"] = True
    streamSettings = {}
    streamSettings["network"] = "ws"
    path={}
    path["path"] = "/"
    streamSettings["wsSettings"] = path
    inbounds["port"] = 8080
    inbounds["protocol"] = "vmess"
    inbounds["settings"] = settings
    inbounds["streamSettings"] = streamSettings

    protocol = {}
    protocol["protocol"] = "freedom"

    data["inbounds"] = [inbounds]
    data["outbounds"] = [protocol]

    with open("a.json", "wb") as fjs:
        json.dump(data, fjs)
        fjs.close
        
    args = ("./app", "-c", "a.json")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)
    print("ok")

