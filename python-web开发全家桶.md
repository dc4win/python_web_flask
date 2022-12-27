# django+前端+数据库

```
— 前端开发：html、css、js
— web框架: 接收请求并处理
— MySQL数据库: 存储数据
```

## 快速上手：基于Flask  Web框架快速搭建网站

### 1、安装flask模块

```python
pip install flask
```

### 2、创建新项目python_web_flask

### 3、flask试运行

```python
from flask import Flask

app = Flask(__name__)

@app.route("/fwb/info")
def index():
    return "镇江气象服务中心"

if __name__ == '__main__':
    app.run()
    
#-运行出现问题：cannot import name ‘Markup‘ from ‘jinja2‘
#-解决方式：pip install flask==2.1.2（限定flask版本）
```

运行结果：![image-20221227193222651](images/image-20221227193222651.png)

![image-20221227202642367](images/image-20221227202642367.png)

## 深入学习：