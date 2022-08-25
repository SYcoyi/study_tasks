import hug


@hug.get('/greet/{event}')  # {}这里是url内嵌参数
def greet(event: str):   # 指定了参数的名称和类型
    greetings = "Happy"
    if event == "Christmas":
        greetings = "Merry"
    if event == "Kwanzaa":
        greetings = "Joyous"
    if event == "wishes":
        greetings = "Warm"
    return f"{greetings} {event}!"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
