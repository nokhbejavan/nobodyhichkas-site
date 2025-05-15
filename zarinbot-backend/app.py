from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Backend is running.'

if __name__ == '__main__':
    app.run()