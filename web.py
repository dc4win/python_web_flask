from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/fwb/info")
def index():
    return render_template("index.html")

@app.route("/register/get",methods=["GET"])
def register_get():
    return render_template("register_get.html")

@app.route("/register/post",methods=["POST"])
def register_post():
    return render_template("register_post.html")

@app.route("/register/")
if __name__ == '__main__':
    app.run()
