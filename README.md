# Django_recruitment笔记
##Django的适用场景
* 网站管理系统
    * 博客
    * CMS
    * wiki
* 企业内部管理系统
    * CRM & ERP
    * 报表系统
    * OA
* 运维管理系统 [开源项目1](https://github.com/voilet/cmdb) [开源项目2](https://github.com/open-cmdb/cmdb)
    * CMBD(配置管理数据库)
    * 发布管理
    * 脚本管理等
* 其他需要对数据进行维护的系统

##Django的优缺点
* 优点
    * python 实现 代码整洁
    * 第三方类库丰富
    * 自带后台管理系统 能够快速开发
    * 内置安全框架
    * 高复用度
* 缺点
    * 单体应用-不适合并行开发
    * 不适合高并发项目

##Django的MTV架构

##安装Django
1.下载并安装Anaconda  

2.命令行安装Django  
  > conda install django

3.创建项目  
  > djangon-admin startproject recruitment  
  
4.启动项目
  > python ./manage.py runserver 0.0.0.0:8080  
  
5.数据库配置  
####创建sql脚本，记录数据模型的变化、 生成数据库表
> python manage.py makemigrations  
> python manage.py migrate  

6.创建超级管理员
> python manage.py createsuperuser
