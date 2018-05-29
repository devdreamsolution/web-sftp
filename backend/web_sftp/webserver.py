import json
import flask
import flask_cors
import configuration
import web_sftp.sftp_manager


def setup_server():
    app = flask.Flask(__name__)
    flask_cors.CORS(app, resources={r"*": {"origins": "*"}})

    login = configuration.read_from_config()
    sftp = web_sftp.sftp_manager.SftpManager(login['host'], login['username'], login['password'], login['remotedir'])

    @app.route('/', methods=['GET'])
    def index():
        return 'root'

    @app.route('/login', methods=['POST'])
    def login():
        return 'login'

    @app.route('/files', methods=['GET'])
    def files():
        """Return files list from remote host"""
        return json.dumps(sftp.get_file_list())

    @app.route('/get', methods=['GET'])
    def get():
        # sftp.get_file('file name')
        return 'add to download queue'

    @app.route('/progress', methods=['GET'])
    def progress():
        return json.dumps(sftp.get_progress())

    @app.route('/put', methods=['POST'])
    def put():
        return 'put to upload queue'

    @app.route('/settings')
    def settings():
        return 'settings'

    app.run(debug=True)
