import hug


class APIUser(object):
    """A minimal example of a rich User object"""

    def __init__(self, user_id, api_key):
        self.user_id = user_id
        self.api_key = api_key


# 判断传入的api_key是否合法
def api_key_verify(api_key):
    magic_key = "5F00832B-DE24-4CAF-9638-C10D1C642C6C"
    if api_key == magic_key:
        return APIUser("user_foo", api_key)
    else:
        return None


api_key_authentication = hug.authentication.api_key(api_key_verify)


@hug.get("/key_authenticated", requires=api_key_authentication)
def basic_auth_call(user: hug.directives.user):
    return f"Successfully authenticated with user:{user.user_id}"


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
