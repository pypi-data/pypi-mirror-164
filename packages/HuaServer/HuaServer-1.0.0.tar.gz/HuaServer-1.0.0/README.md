Hello，大家好。我是张恒华。  
这是一个极简风格的Web框架，取名为Hua(华)。  
本框架旨在帮助后端初学者更快速地入门后端，轻松上手。  
只要你懂一点Python，那么你就能开发后端接口。

## 安装

使用 `pip install HuaServer` 安装

## 检查是否安装成功  

终端输入：`pip show HuaServer`  
正确输出相关信息即为安装成功  

或者 Python 控制台运行：
```python
>>> import HuaServer
>>> HuaServer.__version__
```
正确输出版本号即为安装成功  

## 编写第一个 API

```python
import HuaServer

def handle(body):
    data = {
        "name": "张恒华",
        "age": 21
    }
    return data

HuaServer.bind("/test", handle)
HuaServer.run()
```

执行代码，服务启动，前端使用POST方法通过接口 `http://localhost:6316/test` 可获取到如下JSON数据。  
```json
{
  "code": 200,
  "message": "[HuaServer] 请求成功",
  "data": {
    "name": "张恒华",
    "age": 21
  }
}
```

是不是很简单呢，功能很多，使用文档正在编写中，敬请期待

后续将扩展 `日志模块`、`WebSocket模块`、`DAO模块`
