import pickle
from flask import request
from flask import jsonify
import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_my_ip():
    timestamp = datetime.datetime.utcnow()
    ip  = request.remote_addr
    with open(f'apps/last_beat/{request.remote_addr}', 'wb') as file:
        file.write(pickle.dumps(timestamp))
        file.write(pickle.dumps(ip))
    ip = jsonify({'ip': request.remote_addr}), 200
    print('ip:', request.remote_addr)
    return ip

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)                                                                                                                                                                     