from sqlalchemy.exc import SQLAlchemyError
from database.users.models import Users

def create_user(session, name, email, password, user_id, created_at):
    try:
        obj = Users(name=name, email=email, password=password, id=user_id, created_at=created_at)
        session.add(obj)
        session.commit()
        return obj
    except SQLAlchemyError as e:
        session.rollback()
        error = str(e.__dict__['orig'])
        print(error)
        return error


def get_users(session):
    try:
        users = session.query(Users).all()
        return Users.serialize_users(users)
    except SQLAlchemyError as e:
        session.rollback()
        error = str(e.__dict__['orig'])
        print(error)
        return []