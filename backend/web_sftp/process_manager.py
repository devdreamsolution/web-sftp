import multiprocessing
from typing import List

import web_sftp.helpers.connections


class ProcessManager:
    """Manager for spawning new processes"""
    _processes = {}
    _host_info = {}
    _progress_dict = {}

    def __init__(self, host: str, username: str, password: str, remotedir: str = None):
        self._host_info['host'] = host
        self._host_info['username'] = username
        self._host_info['password'] = password
        self._host_info['remotedir'] = remotedir

        manager = multiprocessing.Manager()
        self._progress_dict = manager.dict()

    def get(self, file: str, outdir: str):
        p = multiprocessing.Process(target=self._get_file, args=(self._progress_dict, file, outdir, self._host_info))
        self._processes[file] = p
        p.start()
        p.join()

    def _get_file(self, pd: dict, file: str, outdir: str):
        def update_dict(current: int, remaining: int, d: dict, key: str): d[key] = [current, remaining]

        with web_sftp.helpers.connections.conn_sftp(self._host_info) as sftp:
            sftp.get(remotepath=file, callback=lambda x, y: update_dict(x, y, pd, file),
                     localpath=outdir)

    def get_file_list(self) -> List[str]:
        with web_sftp.helpers.connections.conn_sftp(self._host_info) as sftp:
            return sftp.listdir()

    def track_progress(self) -> dict:
        return self._progress_dict
