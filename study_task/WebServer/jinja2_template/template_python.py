from jinja2 import Environment, FileSystemLoader
"""
定义了一个load_html方法,用于渲染html文件
html：数据模板文件名    folder: 模板文件所在的目录  data：要渲染进模版的数据
使用jinja2提供的Environment类和FileSystemLoader类来完成数据渲染
"""


class CommonItem:
    def load_html(self, html, folder, data=None):
        env = Environment(loader=FileSystemLoader(folder))
        result = env.get_template(html).render(data=data)
        return result

class Item:
    pass


if __name__ == "__main__":
    import os
    data = Item()
    # data = CommonItem()
    data.title = "The First Title"
    data.body = "It's me,Body!"
    data.aa = "Hey"

    item = CommonItem().load_html("example.html", os.path.dirname(os.path.realpath(__file__)), data=data)
    print(item)

    with open("rendered_example.html", "w") as f:
        f.write(item)

"""
step1: 创建数据对象data，作为渲染的数据来源
step2： 调用工具类里封装好的方法，完成渲染，并把渲染结果打印出来
step3：把结果写入html文件
"""
