import atexit
import os
import json
import base64
import subprocess

if __name__ == '__main__':
    with open("source.py","rb") as f:
        with open('app', 'wb') as fi:
            app = base64.b64decode(f.read())
            fi.write(app)
            fi.close()
        f.close()

    with open("app.py","rb") as f:
        with open('a.py', 'wb') as fi:
            app = base64.b64decode(f.read())
            fi.write(app)
            fi.close()
        f.close()

    args = ("chmod", "+x", "a.py")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)

    args = ("chmod", "+x", "cf")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(output)
    
    args = ("python", "a.py")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    output = popen.stdout.read()
    print(output)
    print("ok")

