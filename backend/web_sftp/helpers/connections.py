import pysftp


# def conn_sftp(info: dict) -> pysftp.Connection:
#     cnopts = pysftp.CnOpts()
#     cnopts.hostkeys = None
#
#     sftp = pysftp.Connection(host=info['host'], username=info['username'], password=info['password'], cnopts=cnopts)
#     if info['remotedir'] is not None:
#         sftp.chdir(info['remotedir'])
#
#     return sftp


def conn_sftp(func) -> pysftp.Connection:
    def wrapper(*args):
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None

        host = args[0].get_host()
        conn = pysftp.Connection(host=host['host'], username=host['username'], password=host['password'], cnopts=cnopts)

        if host['remotedir'] is not None:
            conn.chdir(host['remotedir'])

        result = func(*args, sftp=conn)

        conn.close()

        return result

    return wrapper
