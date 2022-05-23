# conftest.py的内容
import pytest


@pytest.fixture(scope="function", autouse=True)  # 使用了装饰器pytest.fixture. 生效范围是function
# 故每个方法之前之后都会运行它。并且会自动使用。当autouse=True时，我们在测试方法的传入参数里可以省略这个fixture的方法名。
def foo():
    print("***function setup***")
    yield 10     # yield的语句会在测试方法执行完成后被执行
    print("***function teardown***")

