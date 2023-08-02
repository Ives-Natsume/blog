from flask import Flask
app = Flask(__name__)


@app.route('/')
def root():
    return '<a href= "/tools">Tools<br>' \
           '<a href= "/new">nothing here<br>'


@app.route('/new')
def new():
    return 'nothing here<br>' \
           '<a href= "/">Back<br>'


@app.route('/tools')
def tools():
    return '<a href="/tools/typhoon">Typhoon Info<br>' \
           '<a href="/tools/picture">Picture Adaptor<br>' \
           '<a href= "/">Back<br>'


@app.route('/tools/typhoon')
def typhoon():
    return '<a href= "https://www.natyphoon.top/">Natyphoon<br>' \
           '<a href= "http://www.dapiya.net:1234">Dapiya<br>' \
           '<a href= "/">Back<br>'


@app.route('/tools/picture')
def pic():
    return '<a href= "https://waifu2x.udp.jp/index.zh-CN.html">Waifu2X(default)<br>' \
           '<a href="https://bigjpg.com/">Bigjpg(faster but weaker)<br>' \
           '<a href= "/">back<br>'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5050)
