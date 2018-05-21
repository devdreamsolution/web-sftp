import json
import os
import flask
import flask_cors

import web_sftp.sftp_manager


def setup_server():
    app = flask.Flask(__name__)
    cors = flask_cors.CORS(app, resources={r"*": {"origins": "*"}})

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

    @app.route('/get', methods=['GET'])
    def get():
        return 'add to download queue'

    @app.route('/progress', methods=['GET'])
    def progress():
        # return instance.get_progress()
        return 'progress'

    @app.route('/put', methods=['POST'])
    def put():
        return 'put to upload queue'

    @app.route('/settings')
    def settings():
        return 'settings'

    app.run()
