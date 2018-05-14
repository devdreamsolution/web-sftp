import pysftp
import configuration

# for testing purpose only
server = configuration.read_from_config()[0]
username = server['username']
password = server['password']
host = server['host']

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None


# Callback method should return the current progress when called through API
# srv.get('', callback=lambda x,y: print("{} transfered/ {} to go".format(x,y)))


def get_files():
    with pysftp.Connection(host=host, username=username, password=password, cnopts=cnopts) as sftp:
        sftp.chdir('files/')

        return sftp.listdir()
