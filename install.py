import base64

if __name__ == '__main__':
    with open("app.py", "rb") as f:
        with open("cloudfoundry/app.py", "wb") as fa:
            fa.write(base64.b64encode(f.read()))
            fa.close()
        f.close()

    with open("xray", "rb") as f:
        with open("cloudfoundry/source.py", "wb") as fa:
            fa.write(base64.b64encode(f.read()))
            fa.close()
        f.close()