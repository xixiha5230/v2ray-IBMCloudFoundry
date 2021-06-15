import os
import json
import base64
import subprocess
import _thread as thread
import time

UUID = "2ac61062-7cad-4d10-b84a-a3e4ac286bd6"
PATH = "/sss"
IBMEMAIL = "email"
IBMPASS = "password"
CFNAME = "app name"


def cmd_run(args):
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)


def restart():
    time.sleep(30)
    cmd_run(args=("rm", "app", "a.json", "a.py", "-rf"))

    time.sleep(60*60*24*4)

    cmd_run(args=("./cf", "l", "-a", "https://api.us-south.cf.cloud.ibm.com",
                  "login", "-u", IBMEMAIL, "-p", IBMPASS))
    cmd_run(args=("./cf", "rs", CFNAME))


if __name__ == '__main__':
    data = {}
    inbounds = {}
    settings = {}
    clients = {}
    clients["id"] = UUID
    clients["level"] = 0
    settings["clients"] = [clients]
    settings["decryption"] = "none"
    streamSettings = {}
    streamSettings["network"] = "ws"
    path = {}
    path["path"] = PATH
    streamSettings["wsSettings"] = path
    inbounds["port"] = 8080
    inbounds["protocol"] = "vless"
    inbounds["settings"] = settings
    inbounds["streamSettings"] = streamSettings
    protocol = {}
    protocol["protocol"] = "freedom"
    data["inbounds"] = [inbounds]
    data["outbounds"] = [protocol]
    with open("config.json", "w") as f:
        json.dump(data, f)
        f.close

    cmd_run(args=("chmod", "+x", "config.json"))
    cmd_run(args=("./v2ray", "-c", "config.json"))
    thread.start_new_thread(restart, ())
