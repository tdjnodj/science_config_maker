#coding=utf-8
print('支持以下内核:')
print('1.trojan-go')
print('2.hysteria')
print('3.tuic')
print('4.mieru')
print('-----------------------')
n = ''
type = int(input('请选择:'))
if type == 1: # trojan-go
    server = input('服务器地址：')
    port = input('服务器端口：')
    p = input('trojan密码:')
    sni = input('服务名称指示(sni):')
    mux = input('多路复用开启(1:true 2:false)，默认1:')
    if mux != 1 and mux != 2:
        mux = 1
    if mux == 1:
        concurrency = int(input('多路复用数:'))
        if concurrency == n:
            concurrency = 8
        idle_timeout = int(input('链接保活时长:'))
        if idle_timeout == n:
            idle_timeout = 60
    ws = input('ws开启(1.true 2.false)，默认2:')
    if ws != 1 and ws != 2:
        ws = 1
    if ws == 1:
        path = input('输入ws路径(以"/"开头):')
        host = input('ws主机（默认为sni）:')
        if host == "":
            host = sni
    
    # 生成配置
    print('')
    print('{')
    print('    "run_type": "client",')
    print('    "local_addr": "%s",' % server )
    print('    "local_port": %s,' % port )
    print('    "remote_addr": "127.0.0.1",')
    print('    "remote_port": 1080,')
    print('    "password": [')
    print('        "%s"' % p)
    print('    ],')
    print('    "ssl": {')
    print('        "sni": "%s"' % sni)
    print('    },')
    print('    "mux": {')
    if ws == 1:
        print('        "enabled": true,')
    else:
        print('        "enabled": false,')
    print('        "concurrency": %d,' % concurrency)
    print('        "idle_timeout": %d' % idle_timeout)
    print('       },')
    print('    "websocket": {')
    if ws == 1:
        print('        "enabled": true,')
    else:
        print('        "enabled": false,')
    print('        "path": "%s",' % path)
    print('        "host": "%s"' % host)
    print('    }')
    print('}')
    print('')
    print('命令：')
    print('./trojan-go -config config.json')

if type == 2: # hysteria
    server = input('服务器地址：')
    port = input('服务器端口(支持端口跳跃)：')
    protocol = input('传输类型（1.udp 2.faketcp 3.wechat-video）:')
    up = int(input('上传速度（单位:Mbps）:'))
    down = int(input('下载速度(单位:Mbps）:'))
    alpn = input('alpn(建议为h3):')
    server_name = input('服务器名称：')
    insecure = int(input('跳过证书验证？（1.跳过2.不跳过）'))
    obfs = input('混淆密码(obfs,不等于字符串验证密钥')
    auth_str = input('字符串验证密钥(不支持base64):')

    # 生成配置
    print('{')
    print('  "server": "%s:%s",' % (server, port))
    if protocol == 1:
        print('  "protocol": "udp",')
    if protocol == 2:
        print('  "protocol": "faketcp",')
    if protocol == 3:
        print('  "protocol": "wechat-video",')
    print('')
    print('  "obfs": "%s",' % obfs)
    print('  "up_mbps": %d,' % up)
    print('  "down_mbps": %d,' % down)
    print('  "socks5": {')
    print('    "listen": "127.0.0.1:1080"')
    print('  },')
    print('  "auth_str": "%s",' % auth_str)
    print('  "alpn": "%s",' % alpn)
    print('  "server_name": "%s",' % server_name)
    if insecure == 1:
        print('  "insecure": true')
    else:
        print('  "insecure": false')
    print('}')
    print('')
    print('命令:')
    print('./hysteria -c config.json')

# tuic
if type == 3:
    server = input('服务器地址：')
    port = input('服务器端口：')
    sni = input('服务器名称指示（sni）:')
    token = input('密码(token):')
    udp_relay_mode = input('流量传输模式[1.udp 2.quic(推荐)]')
    rtt = input('0-rtt握手恢复（1.开启2.关闭）:')
    congestion_controller = input('拥塞控制算法（1.cubic 2.new_reno 3.bbr 推荐）')

# 生成配置
    print('{')
    print('    "relay": {')
    print('        "server": "%s",' % sni)
    print('        "port": %s,' % port)
    print('        "token": "%s",' % token)
    print('')
    print('        "ip": "%s",' % server)
    if udp_relay_mode == 1:
        print('        "udp_relay_mode": "udp",')
    else:
        print('        "udp_relay_mode": "quic",')
    print('        "heartbeat_interval": 10000,')
    print('        "alpn": ["h3"],')
    if rtt == 1:
        print('        "reduce_rtt": true,')
    else:
        print('        "reduce_rtt": false,')
    print('        "request_timeout": 8000,')
    print('        "max_udp_relay_packet_size": 1500')
    print('    },')
    print('    "local": {')
    print('        "port": 1080,')
    print('')
    print('        "ip": "127.0.0.1"')
    print('    },')
    print('    "log_level": "info"')
    print('}')
    print('')
    print('命令:')
    print('./tuic -c config.json')

# mieru
if type == 4:
    us = input('用户名：')
    p = input('密码：')
    address = input('服务器地址(ipv6不需要加括号)：')
    domain = input('服务器域名(没有请不要添加):')
    port = int(input('服务器端口：'))
    protocol = int(input('模式(1.TCP 2.UDP):'))
    mtu = int(input('mtu(1280-1500):'))

    # 生成配置
    print('')
    print('{')
    print('    "profiles": [')
    print('        {')
    print('            "profileName": "default",')
    print('            "user": {')
    print('                "name": "%s",' % us)
    print('                "password": "%s"' % p)
    print('            },')
    print('            "servers": [')
    print('                {')
    print('                    "ipAddress": "%s",' % address)
    print('                    "domainName": "%s",' % domain)
    print('                    "portBindings": [')
    print('                        {')
    print('                            "port": %d,' % port)
    if protocol == 1:
        print('                            "protocol": "TCP"')
    else:
        print('                            "protocol": "UDP"')
    print('                        }')
    print('                    ]')
    print('                }')
    print('            ],')
    print('            "mtu": %d' % mtu)
    print('        }')
    print('    ],')
    print('    "activeProfile": "default",')
    print('    "rpcPort": 1081,')
    print('    "socks5Port": 1080,')
    print('    "loggingLevel": "INFO",')
    print('    "socks5ListenLAN": false')
    print('}')
    print('')
    print('命令：')
    print('mieru stop && mieru apply config config.json && mieru start')
