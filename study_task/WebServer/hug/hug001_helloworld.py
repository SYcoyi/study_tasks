import hug


@hug.get('/helloworld')  # 用装饰器的方式定义这是一个http get方法的实现， url后缀是/helloworld
def helloworld():
    return "hello world!"


"""
'/helloworld' 通过装饰器的方式加在了helloworld()这个方法上。这里的'/helloworld'就是网页访问时的路径（路由路径）
第一行在web开发框架中叫做routing（路由），路由的意思就是把http的url定向到某个具体的python方法上。
换句话说，这一行规定了下面的这个方法的返回值作为这个url的响应。
第二行定义了方法名，方法名可以和路由路径的url不同
"""

if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
