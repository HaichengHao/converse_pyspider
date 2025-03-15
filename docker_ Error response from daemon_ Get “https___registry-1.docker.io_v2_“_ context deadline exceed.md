 

在执行[docker](https://so.csdn.net/so/search?q=docker&spm=1001.2101.3001.7020) -run 的时候报错，

> docker: Error response from daemon: [Get](https://so.csdn.net/so/search?q=Get&spm=1001.2101.3001.7020) “https://registry-1.docker.io/v2/”: context deadline exceeded (Client.Timeout exceeded while awaiting headers).

刚开始使用的是阿里的[镜像源](https://so.csdn.net/so/search?q=%E9%95%9C%E5%83%8F%E6%BA%90&spm=1001.2101.3001.7020)，但是不行  
所以在网络上找了很多，终于找到有效的镜像源了  
亲测有效！！！

```bash
{
"registry-mirrors": [
"https://docker.nju.edu.cn",
"https://hub.littlediary.cn",
"https://hub.xdark.top",
"https://dockerpull.org",
"https://hub.crdz.gq",
"https://docker.1panel.live",
"https://docker.unsee.tech"
]
}
```

所有命令，可以直接挨个执行
-------------

```bash
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
 {
 "registry-mirrors": [
"https://docker.nju.edu.cn", 
"https://hub.littlediary.cn",
"https://hub.xdark.top",
"https://dockerpull.org",
"https://hub.crdz.gq",
"https://docker.1panel.live",
"https://docker.unsee.tech"
]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker
```

本文转自 <https://blog.csdn.net/qq_45275100/article/details/144636315?ops_request_misc=%257B%2522request%255Fid%2522%253A%252248f10c0a8b2580900be559b5e64821f6%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=48f10c0a8b2580900be559b5e64821f6&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_click~default-2-144636315-null-null.142^v102^pc_search_result_base8&utm_term=Error%20response%20from%20daemon%3A%20Get%20https%3A%2F%2Fregistry-1.docker.io%2Fv2%2F%3A%20context%20deadline%20exceeded%20%28Client.Timeout%20exceeded%20while%20awaiting%20headers%29&spm=1018.2226.3001.4187>，如有侵权，请联系删除。