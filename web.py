from flask import Flask

app = Flask(__name__)

@app.route("/fwb/info")
def index():
    return "镇江气象服务中心"

if __name__ == '__main__':
    app.run()
