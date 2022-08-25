import falcon
import hug


@hug.post("/hello")
def hello(request, response):
    response.data = {"message": "Hello world!"}
    response.append_header("token", "mock")
    response.append_header("token", "mock2")  # 此句为添加，在token值中又增加了一个字符串mock2
    response.status = falcon.HTTP_400         # 所以说响应码是自定义的，不过建议还是按照http的规范来定义
    if request.headers.get("USER"):
        # response.headers["token"] = "mock-token"    # 这句话没用,无法进行变更
        response.set_header("token", "mock-token")     # 此写法为变更header
        return "hello," + request.headers["USER"] + ".token:" + response.headers["token"]
    return "hello"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
