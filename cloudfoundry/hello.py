import atexit
import os
import json
import base64
import subprocess


def generateBinary(file_in, file_out):
    with open(file_in, "rb") as fin:
        with open(file_out, 'wb') as fout:
            b = base64.b64decode(fin.read())
            fout.write(b)
            fout.close()
        fin.close()


def cmd_run(args):
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)


if __name__ == '__main__':
    generateBinary("v2ray.py", "v2ray")
    generateBinary("v2ctl.py", "v2ctl")
    generateBinary("app.py", "a.py")

    cmd_run(args=("chmod", "+x", "v2ray"))
    cmd_run(args=("chmod", "+x", "v2ctl"))
    cmd_run(args=("chmod", "+x", "a.py"))
    cmd_run(args=("chmod", "+x", "cf"))
    cmd_run(args=("python", "a.py"))
