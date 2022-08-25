import hug


@hug.get('/echo', versions=1)
def echo(text):
    return text


@hug.get('/echo', versions=range(2, 5))
def echo(text):
    return f"Echo:{text}"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
