#coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, create_engine
from sqlalchemy import ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from flask import Flask, request, render_template
from api import fetchAPI
import os

basedir = os.path.abspath(os.path.dirname(__file__))  #初始化数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, "data.sqlite")

app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  #不追踪对象修改发信号，减少内存占有

db = SQLAlchemy(app)  # db对象是SQLAlchemy类的实例，表示程序使用的数据库

class Role(db.Model): #将roles表定义为模型 Role
    _tablename_ = 'roles'#设为True，此列为表的主键
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    weatherapi = db.relationship('Weatherapi',backref='role')
    # 第一个参数表明关系另一段是Weatherapi模型，backref参数向Weatherapi模型添加role属性定义反向关系
    def _repr_(self):
        return '<Role %r>' %self.name

class Weatherapi(db.Model):#weatherapi表定义为模型 Weatherapi
    _tablename_ = 'weatherapi'
    id = db.Column(db.Integer, primary_key=True) #设为True，此列为表的主键
    onlinetime = db.Column(db.String(64), unique=True,index=True) #列类型为日期
    cityname = db.Column(db.String(64), unique=True,index=True) #列类型为变长字符串
    weather = db.Column(db.String(64), unique=True,index=True) #列类型为变长字符串
    temp = db.Column(db.Float(64), unique=True,index=True) #列类型为浮点数
    wind = db.Column(db.Float(64), unique=True,index=True) #列类型为浮点数
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    #‘role_id’参数表明这列的值是roles表中行的id值


    def _repr_(self):
        return '<onlinetime %s, cityname %s, weather %s, temp %s, wind %s>' % (self.onlinetime,
                self.cityname, self.weather, self.temp, self.wind)
