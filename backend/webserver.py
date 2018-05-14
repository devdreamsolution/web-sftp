import flask
import json
import sftp_server

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'fiiiiisk'


@app.route('/login', methods=['POST'])
def login():
    return 'login stuff'


@app.route('/files', methods=['GET'])
def files():
    return json.dumps(sftp_server.getFiles())


@app.route('/download', methods=['POST'])
def download():
    return 'add to download queue'


@app.route('/settings')
def settings():
    return 'settings'


app.run()
