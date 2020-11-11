import atexit
import os
import json
import base64



if __name__ == '__main__':
    print("test")
    with open("web", "rb") as f:
        encoded_string = base64.b64encode(f.read())

        with open("Output.txt", "w") as text_file:
            text_file.write("%s" % encoded_string)
