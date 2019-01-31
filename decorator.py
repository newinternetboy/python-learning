# 注册路由回调函数(装饰器)
class MyApp():
    def __init__(self):
        self.func_map = {}

    def register(self, name):
        def func_warpper(func):
            self.func_map[name] = func
            return func
        return func_warpper

    def call_method(self, name=None):
        func = self.func_map.get(name,None)
        if func is None:
            raise Exception("No registered this function")
        return func()

app = MyApp()
@app.register('/')
def main_page_function():
    return "this is main page"

@app.register('/next_page')
def next_page_function():
    return "this is next page"

print(app.call_method('/'))
print(app.call_method('/next_page'))