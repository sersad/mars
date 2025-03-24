import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # должность
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # профессия
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # адрес
    email = sqlalchemy.Column(sqlalchemy.String,
                              index=True, unique=True, nullable=True)  # электронная почта

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # хэшированный пароль
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)  # дата изменения
    jobs = orm.relationship('Jobs', back_populates='user')

    # departments = orm.relationship("Department", back_populates='user')

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return f"""id:{self.id}, name:{self.name}, email:{self.email}"""
