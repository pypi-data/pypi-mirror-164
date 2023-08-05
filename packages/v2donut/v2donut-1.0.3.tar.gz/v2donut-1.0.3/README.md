# v2donut

自动获取、设置延迟最低的 V2Ray 节点

[![Pypi Version][pypi-image]][pypi-url]

执行 `v2donut init` 初始化程序配置, 接下来修改订阅地址和 V2Ray 配置文件所在路径:

```json
{
  "url": "这里填写你的订阅地址",
  "v2conf": "这里填写你的 V2Ray 配置文件所在路径",
  "count": 4,
  "timeout": 0.8,
  "socks_port": 1080,
  "http_prot": 1081
}
```

> v2donut 配置文件在 /用户主页/v2donut.json

接下来启动 v2donut:

```bash
v2donut
```

随后将在控制台输出以下结果:

```bash
Ping 香港1 [xg1.localhost.com], 时间=24.23ms
Ping 香港2 [xg2.localhost.com], 时间=16.37ms
最快的服务器是 香港2 [xg2.localhost.com], 时间=16.37ms
```

[pypi-image]: https://badge.fury.io/py/v2donut.svg
[pypi-url]: https://pypi.org/project/v2donut/