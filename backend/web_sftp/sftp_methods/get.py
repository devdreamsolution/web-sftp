import multiprocessing
import sftp_methods


class SftpGet(multiprocessing.Process):
    def __init__(self, conn: dict, file: str, progress, active_list):
        super().__init__()
        self.conn = conn
        self.file = file
        self.progress = progress
        self.active = active_list

    def _update_progress(self, progress: int, remaining: int):
        self.progress[self.file] = [progress, remaining]

    def run(self):
        with sftp_methods.connect(self.conn) as sftp:
            sftp.get(remotepath=self.file, callback=lambda x, y: self._update_progress(x, y))
            self.active.remove(self.file)
