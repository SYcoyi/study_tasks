"""
令牌token鉴权の服务端实现
"""
import jwt  # json web token   pip install pyjwt
import hug


def token_verify(token):
    secret_key = "super-secret-key-please-change"
    try:
        return jwt.decode(token, secret_key, algorithms="HS256")  # 使用secret_key作为密钥，然后使用HS256算法来解密用户请求中携带的token
    except jwt.DecodeError:
        return False
# 服务端用secret_key生成了token，所以客户端再把token传回服务端时，服务端就用上面这种办法来校验这个token。
# 因为HS256是对称算法，所以可以通过解密的方式来做token的相互对比。


token_key_authentication = hug.authentication.token(token_verify)
"""
功能是：检查token是否是合法的token。其中token的规则是token_verify的方法来实现的。
hug.authentication.token方法指定了令牌鉴权使用token_verify这个方法来做。
这里的token_key_authentication值其实就是校验通过的用户提供的token值。
这段代码通过用户自定义的方法名token_verify,以及下面的requires=token_key_authentication，达到了对用户请求中的token调用token_verify的效果。
"""


# 用requires调用鉴权
@hug.get("/token_authenticated", requires=token_key_authentication)  # token_key_authentication 就是校验通过的token值
def token_auth_call(user: hug.directives.user):
    return "You are {0}, with data {1}".format(user["user"], user["data"], token_key_authentication)


# Authenticate and return a token
@hug.post("/token_generation")
def token_gen_call(user, password):
    secret_key = "super-secret-key-please-change"
    mockusername = "User2"
    mockpassword = "Mypassword"
    if mockusername == user and mockpassword == password:   # 如果用户名密码与预期的相符，则给这个用户生成一个token
        return {"token": jwt.encode({"user": user, "data": "mydata"}, secret_key, algorithm="HS256")}
    return f"Invalid user and/or password for user: {user}"
# token_gen_call方法：先做了用户名和密码的校验，然后生成了一个token，再返回给用户。


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)

"""
jwt库支持的token生成算法有：
--unsecured
    none(disabled by default for security)
--Symmetric
    HS256
    HS384
    HS512
--Asymmetric
    RS256
    RS384
    RS512
"""
