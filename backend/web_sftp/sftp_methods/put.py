import multiprocessing
import sftp_methods


class SftpPut(multiprocessing.Process):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn

    def run(self):
        """something"""
