from falsy.falsy import FALSY

f = FALSY(static_path='test', static_dir='demo/simple/static')
f.begin_api()
f.swagger('demo/simple/spec.yml', ui=True, ui_language='zh-cn', theme='responsive')
f.end_api()
api = f.api
