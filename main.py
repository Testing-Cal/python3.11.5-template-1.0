from flask import Flask, render_template
import os

app = Flask(__name__)

port = os.getenv('port', 7076)

context = os.getenv('context', '/')

@app.route(context+'/', methods=['GET'])
def greet():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)

