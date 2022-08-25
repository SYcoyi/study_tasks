from jinja2 import Template
#
#
# class CommonItem:
#     pass
#
#
# data = CommonItem()
# data.name = "Python"
# print(data)            # <__main__.CommonItem object at 0x00C2C4F0>
# print(data.name)       # Python
# # print(data['name'])   # TypeError: 'CommonItem' object is not subscriptable（不可下标访问）
#
# template = Template("Hello {{data['name']}}")     # 变量里的属性可以用中括号[]来访问（Jinja2和python里的表达式是不一样的，所以可以这么访问）
# print(template.render(data=data))
#
# template = Template("Hello {{data.name}}")        # 变量里的属性可以用点号.来访问
# print(template.render(data=data))
# print()
#
# # Filter语法
# template = Template('Hello {{name | lower}}')
# print(template.render(name="World"))
# print(template.render(name="Python"))
#
# template = Template("Hello {{name | join('&')}}")
# print(template.render(name=["World", "Python"]))
# print()
#
# # 不使用filter而是直接改变变量
# template =  Template('Hello {{name}}')
# print(template.render(name="World".lower()))
# print(template.render(name="PYTHON".lower()))
# print(template.render(name='&'.join(['World', 'Python'])))
#

# # for循环---列表循环
# source = """
# <h1>Members</h1>
# <ul>
# {% for user in users %}
#  <li>{{user.username|e}}</li>
# {% endfor %}
# </ul>
# """
#
#
# class CommonItem:
#     pass
#
#
# user1 = CommonItem()
# user2 = CommonItem()
# user1.username = "WORLD"
# user2.username = "PYTHON&"
#
# template = Template(source)
# print(template.render(users=[user1, user2]))
# print()
# print()
#
# """
# {% for user in users %}
#  <li>{{user.username|e}}</li>
# {% endfor %}
# 这三行是用来做循环，|e  是filter，用来对html做转换，把特殊字符转换成安全的html。因为有些字符直接放在html里会无法正确显示，会被自动转译。
# 而上下大括号的两行是Jinja语法，在for后面加上endfor来结束循环体。
# """
#
# # for循环---字典循环
# source = """
# <dl>
# {% for key,value in my_dict.items() %}
#   <dt>{{key|e}}</dt>
#   <dd>{{value|e}}</dd>
# {% endfor %}
# </dl>
# """
# template = Template(source)
# print(template.render(my_dict={"name1": "World", "name2": "Python"}))
# print()

# # if分支
# source = """
# {% if users %}
# <ul>
# {% for user in users %}
#   <li>{{user.username|e}}</li>
# {% endfor %}
# </ul>
# {% endif %}
# """
#
#
# class CommonItem:
#     pass
#
#
# user1 = CommonItem()
# user2 = CommonItem()
# user1.username = "WORLD"
# user2.username = "PYTHON%&^*&)("
#
# template = Template(source)
# print(template.render(should_be_users=[user1, user2]))  # 无输出
# print(template.render(users=[user1, user2]))
# print()


# if else分支
source = """
<ul>
{% for user in users %}
    {% if user.username == "World" %}
    <li>Hello {{user.username|e}}</li>
    {% elif user.username == "Python" %}
    <li>I Love {{user.username|e}}</li>
    {% else %}
    <li>It is {{user.username|e}}</li>
    {% endif %}
{% endfor %}
</ul>
"""


class CommonItem:
    pass


user1 = CommonItem()
user2 = CommonItem()
user3 = CommonItem()
user1.username = "World"
user2.username = "Python"
user3.username = "Coyi @_@"

template = Template(source)
print(template.render(users=[user1, user2, user3]))
print()
