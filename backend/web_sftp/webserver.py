import flask
import json


def setup_server():
    app = flask.Flask(__name__)

    @app.route('/', methods=['GET'])
    def index():
        return 'root'

    @app.route('/login', methods=['POST'])
    def login():
        return 'login'

    @app.route('/files', methods=['GET'])
    def files():
        """Return files list from remote host"""
        # return json.dumps(instance.get_file_list())
        return 'files'

    @app.route('/get', methods=['POST'])
    def get():
        return 'add to download queue'

    @app.route('/put', methods=['POST'])
    def put():
        return 'put to upload queue'

    @app.route('/settings')
    def settings():
        return 'settings'

    app.run()
