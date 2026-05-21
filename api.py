from flask_restful import Resource, reqparse
from uuid import uuid4 as generateId

# key will be the user_id
users = {}


create_user_parser = (reqparse.RequestParser()
        .add_argument("name", type=str, required=True)
        .add_argument("age", type=int))
class RegisterUser(Resource):
    def post(self):
        name, age = create_user_parser.parse_args().values()
        id = str(generateId())
        users[id] = {
            "id": id,
            "name": name,
            "age": age,
        }
        return users[id], 200
    
class GetUser(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return { "error": "That user does not exist" }, 404
        return user, 200
    

class RemoveUser(Resource):
     def delete(self, user_id):
        if user_id not in users:
            return { "error": "That user does not exist" }, 404
        del users[user_id]
        return {}, 200
     
    
class ListUsers(Resource):
    def get(self):
        response_list = []
        for user in users.values():
            response_list.append(user)
        return { "users": response_list}, 200
    

create_workout_parser = (reqparse.RequestParser()
        .add_argument("date", type=str, required=True)
        .add_argument("time", type=str, required=True)
        .add_argument("distance", type=str, required=True))


class AddWorkout(Resource):
    def put(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"error": "That user does not exist"}, 404
        workout_data = create_workout_parser.parse_args()
        workout = {
            "date": workout_data["date"],
            "time": workout_data["time"],
            "distance": workout_data["distance"]
        }
   
        if "workouts" not in user:
            user["workouts"] = []
        user["workouts"].append(workout)
        
        return workout, 200
        

class ListWorkouts(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if user is None:
            return {"error": "That user does not exist"}, 404
        workouts = user.get("workouts", [])
        return { "workouts": workouts}, 200
    

follow_parser = (reqparse.RequestParser()
    .add_argument("follow_id", type=str, required=True)
)
class FollowFriend(Resource):
    def put(self, user_id):
        follow_id = follow_parser.parse_args().follow_id
        user = users.get(user_id)
        follow_user = users.get(follow_id)
        if user is None or follow_user is None:
            return {"error": "One or both users do not exist"}, 404
        if "following" not in user:
            user["following"] = set()
        user["following"].add(follow_id)
        return {"following": list(user["following"])}, 200
    

class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):
        user = users.get(user_id)
        friend = users.get(follow_id)
        if user is None or friend is None:
            return {"error": "User or friend not found"}, 404
        if follow_id not in user["following"]:
            return {"error": "You must follow this user to see their workouts."}, 403
        return {"workouts": friend.get("workouts", [])}, 200
