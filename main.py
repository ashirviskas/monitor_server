from screenshotter import ScreenShotter
from flask import Flask, render_template

ss = ScreenShotter()

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def main():
    ss.do_screenshot()
    return render_template('main.html')


@app.route("/img.png")
def screenshot():
    ss.do_screenshot()
    return open('static/screenshot.png', 'rb').read()

app.run()