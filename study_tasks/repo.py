"""


"""


from api.repositories.traffic import Traffic
from core.rest_client import RestClient


class Repos(RestClient):  # ������һ��Repos�࣬��RestClient������
    def __init__(self, api_root_url, **kwargs):  # ��ʼ�������࣬�͸������Ų�ͬ�Ĳ�����һ���̶�������һ���ؼ��ֲ��� **kwargs ��ֵ��
        super(Repos, self).__init__(api_root_url, **kwargs)
        self.traffic = Traffic(self)    # �Ӽ���ķ������ﶨ��
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
        �г����repository���ٷ��÷������https://docs.github.com/cn/rest/repos/repos#list-repositories-for-the-authenticated-user
        """
        return self.get('/user/repos', **kwargs)

    def list_user_repo(self, username, **kwargs):
        """
        �ٷ��ĵ���ַ��https://docs.github.com/cn/rest/repos/repos#list-repositories-for-a-user
        :param username:
        :param kwargs:
        :return:
        """
        return self.get("/user/{}/repos".format(username), **kwargs)

    def list_org_repo(self, org, **kwargs):
        """
        �г�һ��org�µ�����repo
        �ĵ�https://docs.github.com/cn/rest/repos/repos#list-organization-repositories
        """
        return self.get("/orgs/{}/repos".format(org, **kwargs))

    def list_public_repos(self, **kwargs):
        """
        https://docs.github.com/en/rest/repos/repos#list-public-repositories
        """
        return self.get("/repositories", **kwargs)