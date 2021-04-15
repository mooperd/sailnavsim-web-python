from model import Boat, BoatRace, User, dbconnect

def addUser(session, user_input):
    user = User()
    user.name = user_input["name"]
    user.email = user_input["email"]


def addBoatRace(session, race_input):
    race = BoatRace()
    race.name = race_input["name"]
    race.startLat = race_input["startLat"]
    race.startLon = race_input["startLon"]


def addBoat(session, boat_input, user):
    # Try and get the Country from the database. If error (Except) add to the database.
    boat = Boat()
    boat.name = boat_input["name"]
    boat.started = boat_input["started"]
    boat.boatType = boat_input["boatType"]
    boat.desiredCourse = boat_input["desiredCourse"]
    boat.isActive = boat_input["isActive"]
    boat.boatFlags = boat_input["boatFlags"]
    boat.race = addBoatRace(session, boat_input["race"])
    boat.user = user
    session.add(boat)
    session.commit()


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

session = dbconnect()
newUser = addUser(session, data)
newBoat = addBoat(session, data["boat"], newUser)
session.commit()
