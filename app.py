from model import Boat, BoatRace, User, BoatLog, dbconnect
from flask import request, Flask, jsonify, render_template, send_from_directory
from talk_to_core import addBoatinCore, startBoatinCore, setCourseinCore


def getOrAddUser(user_input):
    session = dbconnect()
    try:
        user = session.query(User).filter(User.email == user_input["email"]).one()
    except:
        user = User()
        user.name = user_input["name"]
        user.email = user_input["email"]
    session.close()
    return user


def addBoatRace(session, race_input):
    race = BoatRace()
    race.name = race_input["name"]
    race.startLat = race_input["startLat"]
    race.startLon = race_input["startLon"]


def addBoat(boat_input):
    # Get or create user
    user = getOrAddUser(boat_input)
    # Database
    session = dbconnect()
    boat = Boat()
    boat.name = boat_input["boat"]["name"]
    boat.started = boat_input["boat"]["started"]
    boat.boatType = boat_input["boat"]["boatType"]
    boat.desiredCourse = boat_input["boat"]["desiredCourse"]
    boat.isActive = boat_input["boat"]["isActive"]
    boat.boatFlags = boat_input["boat"]["boatFlags"]
    boat.race = addBoatRace(session, boat_input["boat"]["race"])
    boat.user = user
    session.add(boat)
    session.commit()
    session.flush()
    # Core
    addBoatinCore(boat.name, boat_input["boat"]["race"]["startLat"], boat_input["boat"]["race"]["startLon"], boat.boatType, boat.boatFlags, boat.id)
    return boat.id


def getStatus(boatName):
    session = dbconnect()
    status = session.query(BoatLog).filter(BoatLog.boatName == boatName).order_by(BoatLog.time.desc()).first()
    status = status.__dict__
    status.pop("_sa_instance_state")
    return status


def getTrack(boatName):
    session = dbconnect()
    logs = session.query(BoatLog).filter(BoatLog.boatName == boatName).all()
    print(logs)
    output = []
    for log in logs:
        output.append([log.lat, log.lon])
    return output



# Start flask stuff
app = Flask(__name__)

@app.route('/')
def root():
    return render_template("huws_map.html")


@app.route('/status/<boatName>')
def status(boatName):
    return jsonify(getStatus(boatName))


@app.route('/track/<boatName>')
def track(boatName):
    output = getTrack(boatName)
    return jsonify(output)

@app.route('/addBoat', methods=['POST'])
def add_boat():
    return {"boatId": addBoat(request.json)}

# Static Files
@app.route('/img/<path:path>')
def img(path):
    return send_from_directory('img', path)


@app.route('/assets/<path:path>')
def assets(path):
    return send_from_directory('assets', path)




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


data = {
    "name": "Uncle Bob",
    "email": "bobby@foo.com",
    "boat": {
        "name": "myboat2",
        "boatType": 1,
        "started": 1,
        "desiredCourse": "180",
        "isActive": 1,
        "boatFlags": 0,
        "race": {
            "name": "Challenger Deep",
            "startLat": 11.373333,
            "startLon": 142.591667
        }
    }
}

###
#session = dbconnect()
#newUser = addUser(session, data)
#newBoat = addBoat(session, data["boat"], newUser)
#session.commit()
###