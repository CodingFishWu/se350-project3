### 框架
- 前后端完全分离
- 用nginx作路由，调度外部请求
- 用kubernetes作load balance，并管理各种容器
- 整个项目暂定部署到Google Cloud上
- 4台虚拟机集群
- （尚在研究中）

### API
- 采用restFul的API，broker和trader各一套
- 特别注意删除操作，改状态、留数据
- 用Swaggar语法编写，可直接将api.yaml复制到Swaggar编辑器中查看front（这个我会写好）

### 数据库
- 使用google storage的mysql存储
- 不使用任何外键、联级关系等

### 功能点
- 用户注册登录
- 用户查看交易板
- 用户使用3种交易
- 等等（后面补充）

### 后端
- 暂时决定采用grails写后端（首先看一下grails-restapi部分，grails提供了直接生成完整api的框架
- 注意，为了保证分布式的简单和高效，暂时决定不使用session，而是采取登录后随机一个token给cookie，设定expired time，写入Radis。判断是否已登录：即取出token，与Radis中的值对应进行判断
- 后端分为trader和broker，分开实现。

### 前端
- 自由实现
- 前端页面一般分为用户界面(trader)和代理人（broker）

### 分支
- trader-front, broker-front分支为前端页面
- trader-back, broker-back分支为后端逻辑
- master分支为主要框架结构，合并前和我商榷
- config分支来存放kubernetes，dockerfile，nginx配置文件等
