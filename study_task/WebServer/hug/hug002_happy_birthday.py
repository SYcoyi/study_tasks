import hug


@hug.get('/happy_birthday')
def happy_birthday(name, age: hug.types.number = 1):  # 定义了两个参数，一个是name，一个是age。“: hug.types.number”是参数age的类型。=1是age的默认值
    return f"Happy {name} Birthday {age}!"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
