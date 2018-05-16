import pysftp


def conn_sftp(info: dict) -> pysftp.Connection:
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None

    sftp = pysftp.Connection(host=info['host'], username=info['username'], password=info['password'], cnopts=cnopts)
    if info['remotedir'] is not None:
        sftp.chdir(info['remotedir'])

    return sftp
