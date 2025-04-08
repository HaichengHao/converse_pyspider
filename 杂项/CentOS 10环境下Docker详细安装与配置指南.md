 

#### CentOS 10环境下Docker详细安装与配置指南

##### 引言

随着[云计算](https://so.csdn.net/so/search?q=%E4%BA%91%E8%AE%A1%E7%AE%97&spm=1001.2101.3001.7020)和微服务架构的迅猛发展，Docker作为一种轻量级的容器技术，已经成为现代软件开发和运维中不可或缺的工具。本文将为您提供一份详尽的指南，帮助您在CentOS 10系统上成功安装和配置Docker及其相关组件，包括Docker Compose和私有Docker镜像仓库。

##### 一、准备工作

在开始安装之前，请确保您的CentOS系统满足以下条件：

1.  **操作系统版本**：CentOS 10或更高版本，64位系统。
2.  **内核版本**：至少为3.10。
3.  **网络连接**：确保您的系统能够连接到互联网，因为安装过程中需要从远程仓库下载软件包。

###### 1.1 卸载旧版本Docker（可选）

如果您之前安装过Docker，建议先卸载旧版本以避免冲突。执行以下命令卸载旧版本的Docker：

```csharp
sudo yum remove docker \docker-client \docker-client-latest \docker-common \docker-latest \docker-latest-logrotate \docker-logrotate \docker-selinux \docker-engine-selinux \docker-engine \docker-ce
```

##### 二、安装Docker

接下来，我们将逐步安装最新的Docker CE（社区版）。

###### 2.1 检查网络连接

确保您的系统能够访问互联网：

```cobol
ping 163.com
```

如果能够收到回复，说明网络连接正常。

###### 2.2 安装必要的依赖

安装一些必要的工具：

```undefined
sudo yum install -y yum-utils
```

###### 2.3 添加Docker仓库

添加Docker的官方仓库，以便能够下载最新版本的Docker：

```cobol
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
```

###### 2.4 更新本地镜像源并安装Docker CE

更新本地镜像源并安装Docker CE：

```sql
sudo yum update -ysudo yum install -y docker-ce docker-ce-cli containerd.io
```

##### 三、启动Docker服务

安装完成后，启动Docker服务：

```sql
sudo systemctl start docker
```

为了确保Docker在系统启动时自动运行，执行以下命令：

```bash
sudo systemctl enable docker
```

###### 3.1 关闭防火墙（推荐）

为了避免端口冲突，建议关闭防火墙：

```vbscript
sudo systemctl stop firewalldsudo systemctl disable firewalld
```

##### 四、配置[Docker镜像](https://so.csdn.net/so/search?q=Docker%E9%95%9C%E5%83%8F&spm=1001.2101.3001.7020)加速

使用国内镜像加速器以提高下载速度。以阿里云镜像加速器为例，编辑Docker配置文件：

```cobol
sudo mkdir -p /etc/dockersudo tee /etc/docker/daemon.json <<-'EOF'{  "registry-mirrors": ["https://your_mirror.aliyuncs.com"]}EOF
```

重启Docker服务使配置生效：

```undefined
sudo systemctl daemon-reloadsudo systemctl restart docker
```

##### 五、安装Docker Compose

Docker Compose用于定义和运行多个容器的应用场景。安装Docker Compose：

```cobol
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-composesudo chmod +x /usr/local/bin/docker-compose
```

验证Docker Compose是否安装成功：

```sql
docker-compose --version
```

##### 六、搭建私有Docker镜像仓库

私有Docker镜像仓库可以帮助您更好地管理和分发镜像。以下是两种搭建方法：

###### 6.1 简化版镜像仓库

使用Docker官方提供的Registry镜像：

```cobol
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

###### 6.2 带图形界面的镜像仓库

使用Portus搭建带图形界面的镜像仓库：

```cobol
docker run -d -p 3000:3000 --restart=always --name portus portus/portus:latest
```

##### 七、配置Docker信任私有仓库

为了让Docker信任您的私有仓库，需要配置证书。生成自签名证书并配置Docker：

```cobol
openssl req -newkey rsa:4096 -nodes -sha256 -keyout domain.key -x509 -days 365 -out domain.crtsudo mkdir -p /etc/docker/certs.d/your_private_registry:5000sudo cp domain.crt /etc/docker/certs.d/your_private_registry:5000/ca.crt
```

重启Docker服务使配置生效：

```undefined
sudo systemctl restart docker
```

##### 八、总结

通过以上步骤，您已经在CentOS 10系统上成功安装并配置了Docker及其相关组件。Docker的强大功能将帮助您更高效地进行软件开发和运维工作。希望本文对您有所帮助，祝您使用愉快！

##### 常见问题与解决方案

1.  **问题**：安装Docker时提示依赖包缺失。 **解决方案**：确保已安装`yum-utils`并更新系统。
    
2.  **问题**：Docker服务无法启动。 **解决方案**：检查防火墙设置，确保端口未被占用。
    
3.  **问题**：镜像下载速度慢。 **解决方案**：配置国内镜像加速器。
    

##### 额外资源

*   Docker官方文档：[https://docs.docker.com](https://docs.docker.com/ "https://docs.docker.com")
*   阿里云容器镜像服务：[https://cr.console.aliyun.com](https://cr.console.aliyun.com/ "https://cr.console.aliyun.com")
*   Docker社区论坛：[https://forums.docker.com](https://forums.docker.com/ "https://forums.docker.com")

希望这些资源能进一步帮助您深入了解和使用Docker。

本文转自 <https://blog.csdn.net/u010204749/article/details/144780887?ops_request_misc=%257B%2522request%255Fid%2522%253A%25226fc4baafa2f9b4d06894c737ffbd2a71%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=6fc4baafa2f9b4d06894c737ffbd2a71&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduend~default-1-144780887-null-null.142^v102^pc_search_result_base8&utm_term=centos10%E5%AE%89%E8%A3%85docker&spm=1018.2226.3001.4187>，如有侵权，请联系删除。