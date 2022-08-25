"""
基础鉴权の服务端实现
"""
import hug
authentication = hug.authentication.basic(hug.authentication.verify("user1", "mypassword"))
# 看方法内部逻辑可知此处返回的是False 或者预期与结果相符的user_name   此处的"user1", "mypassword"是服务端预期的可以鉴权通过的用户名密码


@hug.get("/public")
def public_api_call():
    return "Needs no authentication."


@hug.get("/authenticated", requires=authentication)
def basic_auth_api_call(user: hug.directives.user):  # 定义了一个参数user，并且指定该user参数的类型为user
    return f"Successfully authenticated with user: {user}"


"""
basic鉴权是hug支持的鉴权方式之一，是通过hug directive机制实现的鉴权。
相当于只要使用hug.authentication.basic和requires=authentication这样的句式，hug就自动帮我们做了basic鉴权校验。

代码注解：
第二行：authentication的值等于hug.authentication.basic的返回值
而basic方法的参数是hug.authentication.verify方法的返回值
verify方法的参数是服务端写死的预期的合法的用户名和密码

hug.authentication.basic 和 hug.authentication.verify这两个方法是hug提供的功能
功能是：检查用户输入的用户名密码是否等于合法的用户名密码。
实现是：将用户传过来的值做解码再和合法值做对比，或者对合法值做编码，再和用户传过来的值做对比。
用户的值怎么传过来的呢？是使用hug.directives.user机制把值传过来。
而预期的值是什么呢？就是hug.authentication.verify("user1", "mypassword")里面写死的这个user和password
也就是说，basic这个方法里面，就有了预期值和用户值，然后再做解码或编码来进行对比，将对比结果返回。正确则返回username，错误则为False。
"""

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
