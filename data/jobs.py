import datetime
import sqlalchemy
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Jobs(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    """
    id
    team_leader (id) (id руководителя, целое число)
    job (description) (описание работы)
    work_size (hours) (объем работы в часах)
    collaborators (list of id of participants) (список id участников)
    start_date (дата начала)
    end_date (дата окончания)
    is_finished (bool) (признак завершения)"""
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    user = orm.relationship('User')

    def __repr__(self):
        return f"{self.id}\t-\t{self.job}"
