from flask_restful import Api
from constants import *
from api import *


BASE_ROUTE = "/user"
USER_ID_ROUTE = f"{BASE_ROUTE}/<string:user_id>"
SHOW_FRIEND_WORKOUTS_ROUTE = "/follow-list/<string:user_id>/<string:follow_id>"
ADD_WORKOUT_ROUTE = "/workouts/<string:user_id>"
LIST_WORKOUTS_ROUTE = "/workouts/<string:user_id>"
FOLLOW_FRIEND_ROUTE = "/follow-list/<string:user_id>"


ROUTES = {
    REGISTER_USER: BASE_ROUTE,
    GET_USER: USER_ID_ROUTE,
    REMOVE_USER: USER_ID_ROUTE,
    LIST_USERS: "/users",
    FOLLOW_FRIEND: FOLLOW_FRIEND_ROUTE,
    SHOW_FRIEND_WORKOUTS: SHOW_FRIEND_WORKOUTS_ROUTE,
    ADD_WORKOUT: ADD_WORKOUT_ROUTE,
    LIST_WORKOUTS: LIST_WORKOUTS_ROUTE,
    FOLLOW_FRIEND: FOLLOW_FRIEND_ROUTE
}

METHODS = {
    REGISTER_USER: POST,
    GET_USER: GET,
    REMOVE_USER: DELETE,
    LIST_USERS: GET,
    FOLLOW_FRIEND: PUT,
    SHOW_FRIEND_WORKOUTS: GET,
    ADD_WORKOUT: PUT,
    LIST_WORKOUTS: GET,
    FOLLOW_FRIEND: PUT
}

RESOURCES = {
    REGISTER_USER: RegisterUser,
    GET_USER: GetUser,
    REMOVE_USER: RemoveUser,
    LIST_USERS: ListUsers,
    FOLLOW_FRIEND: FollowFriend,
    SHOW_FRIEND_WORKOUTS: ShowFriendWorkouts,
    ADD_WORKOUT: AddWorkout,
    LIST_WORKOUTS: ListWorkouts,
    FOLLOW_FRIEND: FollowFriend
}
   

def init_routes(api: Api) -> None:
    for [api_name, resource] in RESOURCES.items():
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])