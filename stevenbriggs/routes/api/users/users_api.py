from sqlalchemy import func

from stevenbriggs.app import db, User


def create_user(user_json):
    """
    Creates a User from the JSON data passed in

    JSON Keys:
    ==========
    name: String (32)
    bio: String (2048)
    race: String (32)
    gender: String (32)
    status: String (64)

    -> User()
    """
    name = user_json['name']
    bio = user_json['bio']
    race = user_json['race']
    gender = user_json['gender']
    status = user_json['status']

    user = User(name=name, bio=bio, race=race, gender=gender, status=status)

    db.session.add(user)
    db.session.commit()

    return user


def get_user(user_id):
    """
    Gets a single User from the database specified by the user_id

    Parameters:
    ===========
    user_id: int

    -> User or None
    """

    user = User.query.filter_by(id=user_id).first()

    return user


def edit_user(user_id, user_json):
    """
    Edits the User to match the user_json

    Parameters:
    ===========
    user_id: int

    JSON Keys:
    ==========
    name: String (32)
    bio: String (2048)
    race: String (32)
    gender: String (32)
    status: String (64)

    -> User or None
    """

    user = get_user(user_id)
    if not user:
        return None

    user.name = json_helper(user_json, "name", user.name)
    user.bio = json_helper(user_json, "bio", user.bio)
    user.race = json_helper(user_json, "race", user.race)
    user.gender = json_helper(user_json, "gender", user.gender)
    user.status = json_helper(user_json, "status", user.status)

    db.session.commit()

    return user


def delete_user(user_id):
    """
    Deletes the User passed in specified by the user_id

    Parameters:
    ==========
    user_id: int

    -> None
    """

    user = get_user(user_id)

    db.session.delete(user)
    db.session.commit()


def random_user():
    """
    Gets a random User from the database

    -> User
    """

    return User.query.order_by(func.random()).first()


def json_helper(json, key, default):
    try:
        return json[key]
    except KeyError:
        return default


def get_bulk(user_limit):
    """
    Creates a multi user object that has x amount of users in it.
    Currently starts at the begining of the database;

    Parameters
    ==========
    characer_limit: int

    -> User(s) JSON
    """
    users = User.query.order_by(User.id.asc).yield_per(user_limit)
    return users


def get_all():
    """
    Creates a multi user object that has all the users in the database

    -> User(s) JSON
    """
    users = User.query.all()
    return users
