# mtxcms
zappa + aws + rest 后端。



# 问题排查：

1: .venv ，虚拟环境会影响实际部署， 如果出现莫名奇妙的问题，优先考虑重建虚拟环境。
```bash
rm -rdf .venv && python3.9 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt 
```


## 开发环境

sudo apt-get install -y rpm
pip3 install wheel

## 打包命令

```bash
# python3 setup.py sdist bdist_wheel
# exe 包
$ python setup.py bdist_wininst

# rpm 包
$ python setup.py bdist_rpm

# egg 包
$ python setup.py bdist_egg

# 生成多个格式的进制包
$ python setup.py bdist

# python setup.py bdist_wheel
```

## 安装
# 将模块安装至系统全局环境
$ python setup.py install

# 在系统环境中创建一个软链接指向包实际所在目录
$ python setup.py develop

# 卸载
$ python setup.py develop --uninstall
$ python setup.py develop -u

## 发布命令
```bash
python3 setup.py sdist bdist_wheel
twine upload -u mattwin -p "xIl1*yingzi606" dist/*

```


## 参考项目：
- https://github.com/fei-ke/clash-tproxy

# 关于网络部分


## 快速启动(生产版)
```bash
docker pull csrep/mtproxy

# 局域网网关（网络出口）
export GATEWAY_IP=192.168.43.1
# 网段
export DEFAULT_CIDR=192.168.43.0/24
# 创建docker 网络适配器名
export NETWORK_NAME=macvlanname
export DEFAULT_IP=192.168.43.6
export DEFAULT_GATEWAY=192.168.43.1
# 网卡接口名称
export DEFAULT_IF=eth0
export USE_TPROXY=1
# 设置网卡的扎混模式
sudo ip link set ${DEFAULT_IF} promisc on
# 创建docker 网络适配器(一次性)
#docker network create -d macvlan --subnet=${LAN_CIDR} --gateway=${GATEWAY_IP} -o parent=${INTERFACE} ${NETWORK_NAME}
docker run -it \
    --name mtproxy_gateway \
    --cap-add=NET_ADMIN \
    --restart unless-stopped \
    --network ${NETWORK_NAME} \
    --ip ${DEFAULT_IP} \
    csrep/mtproxy
```

## 重要备注
- 实际实践发现， docker-compose 中的网络配置macvlan以及网卡杂混模式下，另外的客户端IP的设置就算没有严格配置网段的，都能通过clash配置的网关正确处理流量连接外网。
  这个特性非常方便。可以在clash中配置规则，根据元IP网段来规划出站路径。