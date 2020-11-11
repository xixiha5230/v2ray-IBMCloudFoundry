#!/bin/bash
SH_PATH=$(cd "$(dirname "$0")";pwd)
cd ${SH_PATH}

create_mainfest_file(){
    echo "进行配置。。。"
    read -p "请输入你的应用名称：" IBM_APP_NAME
    echo "应用名称：${IBM_APP_NAME}"
    read -p "请输入你的应用内存大小(默认256)：" IBM_MEM_SIZE
    if [ -z "${IBM_MEM_SIZE}" ];then
    IBM_MEM_SIZE=256
    fi
    echo "内存大小：${IBM_MEM_SIZE}"
    UUID=`cat /proc/sys/kernel/random/uuid`
    echo "您的UUID：${UUID}"
    read -p "请输入您的WebSocket路径：" WSPATH
    echo "您的WebSocket路径：${WSPATH}"
    
    cat >  ${SH_PATH}/IBMCloudFoundry/cloudfoundry/manifest.yml  << EOF
    applications:
    - path: .
      name: ${IBM_APP_NAME}
      random-route: true
      memory: ${IBM_MEM_SIZE}M
EOF

    cat >  ${SH_PATH}/IBMCloudFoundry/cloudfoundry/web/config.json  << EOF
    {
        "inbounds": [
            {
                "port": 8080,
                "protocol": "vmess",
                "settings": {
                    "clients": [
                        {
                            "id": "${UUID}",
                            "alterId": 4
                        }
                    ]
                },
                "streamSettings": {
                    "network":"ws",
                    "wsSettings": {
                        "path": "${WSPATH}"
                    }
                }
            }
        ],
        "outbounds": [
            {
                "protocol": "freedom",
                "settings": {}
            }
        ]
    }
EOF
    echo "配置完成。"
}

clone_repo(){
    echo "进行初始化。。。"
    rm -rf IBMCloudFoundry
    git clone -b test https://github.com/xixiha5230/IBMCloudFoundry
    cd IBMCloudFoundry/cloudfoundry/web
    chmod 0755 ./*
    cd ${SH_PATH}/IBMCloudFoundry/cloudfoundry
    echo "初始化完成。"
}

install(){
    echo "进行安装。。。"
    cd ${SH_PATH}/IBMCloudFoundry/cloudfoundry
    ibmcloud target --cf
    echo "N"|ibmcloud cf install
    ibmcloud cf push
    DOMAIN=`ibmcloud cf app $IBM_APP_NAME | grep routes | cut -f2 -d':' | sed 's/ //g'`
    echo "安装完成。"
    echo "您的 UUID：${UUID}"
    echo "您的 WebSocket路径：${WSPATH}"
    VMESSCODE=$(base64 -w 0 << EOF
    {
      "v": "2",
      "ps": "IBMCloudFoundry",
      "add": "${DOMAIN}",
      "port": "443",
      "id": "${UUID}",
      "aid": "4",
      "net": "ws",
      "type": "none",
      "host": "",
      "path": "${WSPATH}",
      "tls": "tls"
    }
EOF
    )
	echo "配置链接："
    echo vmess://${VMESSCODE}

}

clone_repo
create_mainfest_file
install
exit 0
