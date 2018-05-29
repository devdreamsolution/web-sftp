import pysftp


def connect(conn_info: dict) -> pysftp.Connection:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    sftp = pysftp.Connection(host=conn_info['host'], username=conn_info['username'],
                             password=conn_info['password'],
                             cnopts=cnopts)
    if conn_info['remotedir'] is not None:
        sftp.chdir(conn_info['remotedir'])

    return sftp
