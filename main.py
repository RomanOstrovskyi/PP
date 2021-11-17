from flask import Flask
from blueprint import api_blueprint

app = Flask(__name__)

app.register_blueprint(api_blueprint)

@app.route('/api/v1/hello-world-2')
def indx():
    return "Hello world 2"

if __name__ == "__main__":
    app.run()