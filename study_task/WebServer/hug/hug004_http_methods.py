import hug


@hug.get()    # 对应 http中的get方法
def hello_world():
    return "Hello"


@hug.post(output=hug.output_format.json)   # 指定了返回值类型是hug自带的数据类型中的json类型  hug提供的可以把结果自动转换成json字符串的快捷方式（语法糖）
def hello_user(name, age):
    return {name: age}


@hug.put()
def hello_put(name="Anonymity", age="18"):
    return {name: age}


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
