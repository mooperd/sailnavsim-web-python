from log_model import dbconnect, BoatLog
from flask import Flask, jsonify, render_template, send_from_directory

app = Flask(__name__)


def get_status(boatName):
    session = dbconnect()
    status = session.query(BoatLog).filter(BoatLog.boatName == boatName).order_by(BoatLog.time.desc()).first()
    status = status.__dict__
    status.pop("_sa_instance_state")
    return status


def get_track(boatName):
    session = dbconnect()
    logs = session.query(BoatLog).filter(BoatLog.boatName == boatName).all()
    print(logs)
    output = []
    for log in logs:
        output.append([log.lat, log.lon])
    return output


@app.route('/')
def root():
    return render_template("huws_map.html")


@app.route('/status/<boatName>')
def status(boatName):
    return jsonify(get_status(boatName))


@app.route('/track/<boatName>')
def track(boatName):
    output = get_track(boatName)
    return jsonify(output)

# Static Files
@app.route('/img/<path:path>')
def img(path):
    return send_from_directory('img', path)


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)