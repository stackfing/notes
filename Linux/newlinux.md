# 装机必备
`sudo apt install git imwheel`


服务器搭建ss

`wget --no-check-certificate -O shadowsocks.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh`

`chmod +x shadowsocks.sh`

`./shadowsocks.sh 2>&1 | tee shadowsocks.log`


VSCode vue 插件： vetur

vetur 插件格式化 template 问题：
将 vscode 配置文件 vetur.format.defaultFormatter.html:none 修改为 js-beautify-html
