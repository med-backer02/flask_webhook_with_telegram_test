from flask import Flask
import telebot

app=Flask(__name__)


@app.route('/')
def index():
    return "<h1>Test flask app</h1>"

if __name__=='__main__':
    app.run()