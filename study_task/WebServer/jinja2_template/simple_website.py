# -*-coding:gbk -*-
from jinja2 import Environment, FileSystemLoader
import hug, falcon
import os


class CommonItem:
    def load_html(self, html, folder, data=None):
        env = Environment(loader=FileSystemLoader(folder, encoding="GBK"))
        result = env.get_template(html).render(data=data)
        return result


@hug.get("/", output=hug.output_format.html)
def homepage():
    data = CommonItem()
    data.title = "Title is me"
    data.body = "Body is here"
    data.content = "<strong>This is the first item's accordion body.</strong> It is hidden by default, until the " \
                   "collapse plugin adds the appropriate classes that we use to style each element. These classes " \
                   "control the overall appearance, as well as the showing and hiding via CSS transitions. You can " \
                   "modify any of this with custom CSS or overriding our default variables. It's also worth noting " \
                   "that just about any HTML can go within the <code>.accordion-body</code>, though the transition " \
                   "does limit overflow. "
    item = CommonItem().load_html("basic_bootstrap2.html", os.path.dirname(os.path.realpath(__file__)), data=data)
    return item


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)
