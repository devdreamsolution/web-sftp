import multiprocessing
from typing import List
import sftp_methods.get
import sftp_methods.put


class SftpManager:
    """Manager for spawning new processes"""

    def __init__(self, host: str, username: str, password: str, remotedir: str = None):
        self.conn = {
            'host': host,
            'username': username,
            'password': password,
            'remotedir': remotedir
        }

        manager = multiprocessing.Manager()
        self.progress = manager.dict()
        self.active_proc = manager.list()

    def get_file_list(self) -> List[str]:
        """
        Get file list from remote host
        :return: list of files
        """
        with sftp_methods.connect(self.conn) as sftp:
            data = sftp.listdir()

        return data

    def get_progress(self) -> dict:
        """
        Get current progress on downloads and uploads
        :return: dict
        """
        to_return = {}
        for proc in self.active_proc:
            to_return[proc] = self.progress[proc]

        return to_return

    def get_file(self, file: str, outdir: str):
        """
        Get a file from remote host
        :param file:
        :param outdir:
        """
        self.progress[file] = []
        self.active_proc.append(file)
        proc = sftp_methods.get.SftpGet(self.conn, file, self.progress, self.active_proc)
        proc.start()

    def get_host(self):
        """
        Get connection to remote host information
        :return:
        """
        return self.conn
