Docker 是一个开源应用容器


# Linux 下安装

`sudo apt install docker.io`

安装好之后每次需要 `sudo` 才能使用，为了省去麻烦，将用户添加到 docker 用户组中

如果没有用户组 则 `sudo groupadd docker`

将当前用户添加到 `docker` 用户组 `sudo gpasswd -a $USER docker`

***


批量全部删除容器

docker rm `docker ps -a |awk '{print $1}' | grep [0-9a-z]`

运行 `docker run -it 容器名`

查看运行的容器 `docker ps`

打开并且映射端口 `docker run -it -p xxxx:yyyy` 镜像名

查看某个容器占用的端口 `docker port 容器id`

查看所有已经创建的容器 `docker ps -a`

****

获取image `docker pull`

创建image `docker build`

删除contianer `docker rm`

删除 image `docker rmi`

在host和container之间拷贝文件 `docker cp`

保存为新的image `docker commit`


****
Dockerfile

创建一个 Dockerfile

编辑 Dockerfile

输入以下代码

```
FROM alpine:latest
MAINTAINER xbf
CMD echo "hello docker"
```

`docker build -t hello_docker . `

-t 参数为给这个镜像一个标签名，名为 hello_docker



***

`docker logs 容器名`   显示出容器控制台的标准输出