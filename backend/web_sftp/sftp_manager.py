import multiprocessing
from typing import List

from web_sftp.helpers.connections import conn_sftp


class SftpManager:
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

    # def get(self, file: str, outdir: str):
    #     p = multiprocessing.Process(target=self._get_file, args=(self._progress_dict, file, outdir, self._host_info))
    #     self._processes[file] = p
    #     p.start()
    #     p.join()

    def _get_file(self, file: str, outdir: str, sftp):
        def update_dict(current: int, remaining: int, key: str):
            self._progress_dict[key] = [current, remaining]

        sftp.get(remotepath=file,
                 callback=lambda x, y: update_dict(x, y, file),
                 localpath=outdir)

    @conn_sftp
    def get_file_list(self, sftp) -> List[str]:
        # with web_sftp.helpers.connections.conn_sftp(self._host_info) as sftp:
        data = sftp.listdir()
        return data

    def get_progress(self) -> dict:
        return self._progress_dict

    @conn_sftp
    def get_file(self, file: str, outdir: str, sftp):
        self._get_file(file, outdir, sftp)
        return None

    def get_host(self):
        return self._host_info
