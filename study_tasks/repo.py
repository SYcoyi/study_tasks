"""


"""


from api.repositories.traffic import Traffic
from core.rest_client import RestClient


class Repos(RestClient):  # 定义了一个Repos类，是RestClient的子类
    def __init__(self, api_root_url, **kwargs):  # 初始化该子类，和父类有着不同的参数表：一个固定参数，一个关键字参数 **kwargs 键值对
        super(Repos, self).__init__(api_root_url, **kwargs)
        self.traffic = Traffic(self)    # 子级别的放在这里定义
    # def list_your_repos(self, visibility=None, affiliation=None, type=None, sort=None, direction=None,
    #                     per_page=None, page=None, since=None, before=None):
    #     params = {'visibility': visibility,
    #               'affiliation': affiliation,
    #               'type': type,
    #               'sort': sort,
    #               'direction': direction,
    #               'per_page': per_page,
    #               'page': page,
    #               'since': since,
    #               'before': before
    #               }
    #     return self.get("/user/repos", params=params)

    def list_your_repos(self, **kwargs):
        """
        列出你的repository，官方用法在这里：https://docs.github.com/cn/rest/repos/repos#list-repositories-for-the-authenticated-user
        """
        return self.get('/user/repos', **kwargs)

    def list_user_repo(self, username, **kwargs):
        """
        官方文档地址：https://docs.github.com/cn/rest/repos/repos#list-repositories-for-a-user
        :param username:
        :param kwargs:
        :return:
        """
        return self.get("/user/{}/repos".format(username), **kwargs)

    def list_org_repo(self, org, **kwargs):
        """
        列出一个org下的所有repo
        文档https://docs.github.com/cn/rest/repos/repos#list-organization-repositories
        """
        return self.get("/orgs/{}/repos".format(org, **kwargs))

    def list_public_repos(self, **kwargs):
        """
        https://docs.github.com/en/rest/repos/repos#list-public-repositories
        """
        return self.get("/repositories", **kwargs)