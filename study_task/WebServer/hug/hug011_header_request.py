import hug


@hug.post("/hello")
def hello(request):
    if request.headers.get('USER'):       # 因为方法中传了参数request，所以可以直接获取header里的信息
        return "hello," + request.headers['USER']
    return "hello"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
