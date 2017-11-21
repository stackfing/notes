
# 暂未分类

显示运行的进程 `ps` `ps -ax`  查看所有进程 `ps -ef`

杀死进程 `kill -9 pid` -9 是强制杀死

添加到 sudo 组 编辑 /etc/sudoers 在 cmnd alias specification 添加：`root    ALL=(ALL:ALL) ALL`

从本地拷贝文件到远程服务器 `scp file username@139.199.169.119:/home/filepath`

终端中添加显示 git 分支
```
## 添加git分支
function parse_git_dirty {
  [[ $(git status 2> /dev/null | tail -n1) != "nothing to commit, working directory clean" ]] && echo "*"
  }
function parse_git_branch {
    git branch --no-color 2> /dev/null | sed -e '/^[^*]/d' -e "s/*\(.*\)/[\1$(parse_git_dirty)]/"
}
export PS1='\u@\h:\[\e[1;36m\]\w\[\e[2;33m\]$(parse_git_branch)\[\e[0m\]$ '
```
***其中\[\e[2;33m\]是颜色***

在后台运行命令 `command &` 例如 : `java -jar maven.war &`

## 设置交换分区

* free -h 查看内存

* dd if=/dev/zero of=/swapfile bs=1024k count=4096 创建一个4g 交换文件
* mkswap /swapfile 格式化成交换文件的格式
* swapon /swapfile 启用该文件作为交换分区的文件
* /swapfile swap swap defaults 0 0 写入/etc/fstab文件中，让交换分区的设置开机自启
* sudo sysctl vm.swappiness=15 临时修改重启注销失效， 查看：cat /proc/sys/vm/swappiness
* 永久修改：/etc/sysctl.conf 文件中设置开始使用交换分区的触发值： vm.swappiness=10 表示物理内存剩余10% 才会开始使用交换分区

建议，笔记本的硬盘低于 7200 转的不要设置太高的交换分区使用，大大影响性能，因为交换分区就是在硬盘上，频繁的交换数据

***

## 修改源

`sudo gedit /etc/apt/sources.list`

修改成功后更新

`sudo apt update`