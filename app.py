from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world from Liam in 3308!'

if __name__ == '__main__':
    app.run()