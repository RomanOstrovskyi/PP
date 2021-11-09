from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/hello-world-2')
def indx():
    return "Hello world 2"

if __name__ == "__main__":
    app.run()