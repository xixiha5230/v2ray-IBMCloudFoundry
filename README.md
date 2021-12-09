# IBMCloudFoundry

## 用途:
在IBMCloudFoundry上搭建v2ray
## 用法:
打开ibm的控制台后运行

0. run ``git clone https://github.com/xixiha5230/IBMCloudFoundry.git`` and ``cd IBMCloudFoundry``

1. edit ``uuid``,``path``,``ibm account``,``ibm password`` and ``app name`` in ``app.py``

2. run ``python install.py``

3. ``cd cloudfoundry``

4. edit ``name`` in ``manifest.yml``

5. deploy app to IBM cloud run:

   ``ibmcloud target --cf``  
   
   ``ibmcloud cf push``

-------------分割线-----------------
 
