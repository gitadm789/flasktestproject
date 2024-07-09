from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World hi hiiiii hey!'

if __name__ == '__main__':
    app.run(debug=True)
