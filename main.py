import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def main_page():
    return 'The prophecy has been foretold'

if __name__ == '__main__':
    listen_address = os.environ.get('APP_HOST')
    listen_port = os.environ.get('APP_PORT')
    if listen_port and listen_address != None:
        app.run(host=listen_address, port=listen_port)
    else:
        print('Required varibles are not set. Exiting.')
        sys.exit(1)