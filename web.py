from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/fwb/info")
def index():
    return render_template("index.html")

# @app.route("/register/get",methods=["GET"])
# def register_get():
#     return render_template("register_get.html")

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        print("全部内容：", request.form)
        print("姓名：", request.form.get("name"))
        print("擅长方向：", request.form.getlist("youshi"))
        return "注册成功"

# @app.route("/register/content",methods=["POST"])
# def register_result():
#     #1、当使用get方法时可以采用(request.args)
#     #1、 print(request.args)
#     #2、使用post方法时，request.form方式进行访问
#     print("全部内容：",request.form)
#     print("姓名：",request.form.get("name"))
#     print("擅长方向：",request.form.getlist("youshi"))
#     return "注册成功"

if __name__ == '__main__':
    app.run()
