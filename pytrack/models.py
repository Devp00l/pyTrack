# -*- coding: utf-8 -*-
from peewee import BooleanField, CharField, DateTimeField, ForeignKeyField, PrimaryKeyField
from peewee import Model, OperationalError, SqliteDatabase

DATABASE = 'pyTrack_db.sqlite'
db = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = db


class Project(BaseModel):
    """
    ORM model of the Project table
    """
    id = PrimaryKeyField(null=False)
    name = CharField(unique=True)
    selected = BooleanField(default=0)
    status = BooleanField(default=0)
    duration = CharField(default='0:00:00')


    class Meta:
        db_table = 'projects'


class Log(BaseModel):
    """
    ORM model of the Log table
    """
    id = PrimaryKeyField(null=False)
    project = ForeignKeyField(Project, related_name='logs')
    start_time = DateTimeField(null=True)
    stop_time = DateTimeField(null=True)

    class Meta:
        db_table = 'logs'

if __name__ == '__main__':
    try:
        Project.create_table()
    except OperationalError:
        print('Project table already exists!')

    try:
        Log.create_table()
    except OperationalError:
        print('Log table already exists!')
