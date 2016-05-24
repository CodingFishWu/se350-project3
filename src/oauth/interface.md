## OAuth认证服务器的逻辑和接口

#### 数据库
- 最好使用mongoDB，而且写起来比较简单，尤其在这种小程序里面（因为不需要做or映射，拿来即用）（还可以吹逼）
- 表：user,token,code（应该要3张吧...不清楚）

#### 逻辑与接口
1. `get:  /oauth`    这是第一步，用户被重定向到这个url，查看session检查用户是否已经登录，如果已经登录即生成授权码(oauth code，用来获取access token的)，一同重定向到uri上；如果未登录，返回登录界面，登录成功后再做之前的步骤
2. `post: /token`    根据code获取access token,返回token的json信息（规则自定：简单的可以通过对（过期token+时间+随机数）的hash来获得）
3. `get: /user/secret`    根据access token获取用户信息。
4. `post: /expire`    清除session缓存信息和access token（主要用来更换用户重新登录）

#### 参数信息
- code过期时间10min
- session过期时间1天
- token过期时间3天
- 第一步的传入参数：
```
    {
        response_type: "code", //固定
        client_id: "doge" or "fish", //目前决定客户端只有两台，因此限定这两个单词
        redirect_uri: $uri  //我们需要重定向这个功能
    }
```
- 第一步的返回：HTTP/1.1 302 url后面跟上code=XXX
- 第二步的传入参数：
```
    {
        grant_type: "authorization_code" //固定
        code: $code  //上一步的授权码，需检查过期时间
        redirect_uri: $uri
        client_id: XXX
    }
```

- 第二步传回参数：
```
    {
        access_token: XXX //返回token
        token_type: "bearer" //固定
        expires_in:  //过期时间
    }
```
- 第三部传入参数：
```
    {
        token: XXX
    }
```
- 第三部传回参数：
```
    {
        name: XXX
    }
```
#### 备注
以上仅供参考，去看[这篇文章](http://www.ruanyifeng.com/blog/2014/05/oauth_2_0.html)，我们用授权码模式，但是不需要用户点击“确定授权”按钮。