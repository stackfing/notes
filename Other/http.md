# HTTP 请求消息

## 请求行 Request Line:

第一行叫`请求行`，请求行的语法是： `request-method-name request-URI HTTP-version`

request-method-name: http 请求定义了一些请求方法，例如： GET,POST,HEAD,OPTIONS

request-URI:指定请求的资源

HTTP-version:现在有两个版本正在使用： HTTP/1.0 and HTTP/1.1

例如以下都是请求行：
```
GET /test.html HTTP/1.1
HEAD /query.html HTTP/1.0
POST /index.html HTTP/1.1
```


## 请求头 Request Headeers

请求头以`名称:值`的形式出现，可以有多个值，用逗号分割

例如：
```
Host: www.xyz.com
Connection: Keep-Alive
Accept: image/gif, image/jpeg, */*
Accept-Language: us-en, fr, cn
```

# HTTP 响应消息

## 状态行 Status Line

第一行叫`状态行`，状态行的语法是：
`HTTP-version status-code reason-phrase`

HTTP-version: HTTP 版本号

status-code: 3 位数的状态码

reason-phrase： 对状态码的简短解释

例如以下都是状态行：
```
HTTP/1.1 200 OK
HTTP/1.0 404 Not Found
HTTP/1.1 403 Forbidden
```
## 响应头 Reponse Header

与请求头一样，响应头也是以`名称:值`的形式出现，可以有多个值，用逗号分割

以下是例子：
```
Content-Type: text/html
Content-Length: 35
Connection: Keep-Alive
Keep-Alive: timeout=15, max=100
```

# HTTP 请求方法

## GET

GET 是最常见的 HTTP 请求方法，客户端可以使用 GET 请求方法来从 HTTP 服务器请求一些资源

在请求行中大小写敏感，所以必须是大写的 `GET`