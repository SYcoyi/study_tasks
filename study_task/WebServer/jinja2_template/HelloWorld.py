from jinja2 import Template


template = Template('Hello {{name}} and {{name2}}!')  # 新建了一个字符串模板，还可以从文件中来建立模板等
print(template.render(name="World", name2="ZhuHai"))
print(template.render(name="Coyi", name2="Wonderful Life"))    # 使用的是关键字参数作为上下文来完成渲染
print(template.render({"name": "Coyi", "name2": "Wonderful Life"}))   # 使用的是字典作为上下文来完成渲染

"""
Template 为模板类
{{name}}双大括号括起来的内容是占位符。里面可以写任意的python变量以及Jinja2支持的表达式
render方法是渲染。这里即是“往模板(template)里面渲染（render）一些变量(占位符)（{{name}}），渲染进去的变量称之为上下文(context)””
一次渲染多个变量，这些变量共同组成了这次渲染的上下文。
"""