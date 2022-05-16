from django.db import models

# Create your models here.
from collections import UserList
from curses import echo
from xmlrpc.client import Boolean
from  sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, MetaData, select, func,BOOLEAN,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship



Base = declarative_base()

class progect(Base):
    __tablename__ = 'progect'
    P_id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    product_backlogs = relationship('product_backlog', back_populates='progect')#one(progect)to many (product_backlog)
    deliverable_tasks= relationship('deliverable_task', back_populates='progect')#one(progect)to many (deliverable_task)
    subtasks = relationship('subtask', back_populates='progect')#one(progect)to many (subtask)
    activity = relationship('activity',back_populates='progect',uselist=False)#one(progect)to one (activity)


class product_backlog(Base):
    __tablename__ = 'product_backlog'
    Pb_id=Column(Integer,primary_key=True)
    P_id = Column(Integer, ForeignKey('progect.P_id'))#foreign key
    pb_title = Column(String)
    pb_priority = Column(Integer)

    progect = relationship('progect', back_populates='product_backlogs')#one(progect) to many (product_backlog)
    deliverable_tasks = relationship('deliverable_task', back_populates='product_backlog')#one(product_backlog) to many (deliverable_task)
    subtasks = relationship('subtask', back_populates='product_backlog')#one(product_backlog) to many (subtask)


class deliverable_task(Base):
    __tablename__ = 'deliverable_task'
    dt_id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    priority = Column(Integer)
    title = Column(String)
    dependency = Column(String)
    #is_force = Column(Boolean(), unique=False, default=True)

    pb_id = Column(Integer, ForeignKey('product_backlog.Pb_id'))#foreign key
    p_id = Column(Integer, ForeignKey('progect.P_id'))#foreign key    

    progect = relationship(progect , back_populates='deliverable_tasks')#one(progect) to many (deliverable_task)
    product_backlog = relationship('product_backlog', back_populates='deliverable_tasks')#one (product_backlog)to many (deliverable_task)
    subtasks = relationship('subtask', back_populates='deliverable_task')#one(deliverable_task) to many (subtask)

class subtask(Base):
    __tablename__ = 'subtask'
    st_id = Column(Integer, primary_key=True)

    dependency = Column(String)
    situation = Column(String)
    description = Column(String)

    p_id = Column(Integer, ForeignKey('progect.P_id'))#foreign key
    pb_id = Column(Integer, ForeignKey('product_backlog.Pb_id'))#foreign key
    dt_id = Column(Integer, ForeignKey('deliverable_task.dt_id'))#foreign key
    act_id = Column(Integer, ForeignKey('activity.act_id'))#foreign key

    progect = relationship(progect, back_populates='subtasks')#one(progect) to many (subtask)
    product_backlog = relationship('product_backlog', back_populates='subtasks')#one(product_backlog) to many (subtask)
    deliverable_task = relationship('deliverable_task', back_populates='subtasks')#one(deliverable_task) to many (subtask)
    activity = relationship('activity', back_populates='subtask', uselist=False)#one(activity) to many (subtask)


class developer(Base):
    __tablename__ = 'developer'
    dev_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    activitys = relationship('activity', back_populates='developer')#one(developer) to many (activity)

class sprint(Base):
    __tablename__ = 'sprint'
    sprint_number = Column(Integer, primary_key=True)
    start_date = Column(DateTime) #date
    end_date = Column(DateTime) #date 
    duration = Column(Integer)

    activitys = relationship('activity', back_populates='sprint')#one(sprint) to many (activity)


class activity(Base):
    __tablename__ = 'activity'
    act_id = Column(Integer, primary_key=True)

    spent_time=Column(Integer)
    day =Column(Integer)
    remaningjob=Column(Integer)

    sprint_number = Column(Integer, ForeignKey('sprint.sprint_number'))#foreign key
    dev_id = Column(Integer, ForeignKey('developer.dev_id'))#foreign key
    st_id = Column(Integer, ForeignKey('subtask.st_id'))#foreign key
    dt_id = Column(Integer, ForeignKey('deliverable_task.dt_id'))#foreign key
    pb_id = Column(Integer, ForeignKey('product_backlog.Pb_id'))#foreign key
    p_id = Column(Integer, ForeignKey('progect.P_id'))#foreign key

    progect=relationship('progect',back_populates='activity')#one(progect) to one (activity)

    sprint = relationship('sprint', back_populates='activities')#one(sprint) to many (activity)
    developer = relationship('developer', back_populates='activities')#one(developer) to many (activity)
    subtasks = relationship('subtask', back_populates='activity',uselist=False)#one(activity) to many (subtask)


