from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/uday')
def uday():
    return "This is uday"
@app.route('/vasu')
def vasu():
    return "This is vasu"
@app.route('/suni')
def suni():
    return "This is Vasunitha"

@app.route('/user/<name>')
def user(name):
    if name == 'uday':
        return redirect(url_for('uday'))
    if name == 'vasu':
        return redirect(url_for('vasu'))
    if name == 'suni':
        return redirect(url_for('suni'))

if __name__ == '__main__':
    app.run()
