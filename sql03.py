#coding=utf-8
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager,Shell
from sqlalchemy import Column, String, create_engine, MetaData
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
manager = Manager(app) #先抄教程，不是很懂
engine = create_engine('sqlite:////temp/test.db',convert_unicode=True)
metadata = MetaData(bind=engine)


def make_shell_context(): #用shell命令主动导入特定对象，注册make_context回调函数
    return dict(app=app, db=db, Role=Role, Weatherapi=Weatherapi)
manager.add_command("shell", Shell(make_context=make_shell_context))



class Weatherapi(db.Model):#weatherapi表定义为模型 Weatherapi
    __tablename__ = 'weatherapi'
    id = db.Column(db.Integer, primary_key=True) #设为True，此列为表的主键
    onlinetime = db.Column(db.String(64), unique=True,index=True) #列类型为日期
    cityname = db.Column(db.String(64), unique=True,index=True) #列类型为变长字符串
    weather = db.Column(db.String(64), unique=True,index=True) #列类型为变长字符串
    temp = db.Column(db.Float(64), unique=True,index=True) #列类型为浮点数
    wind = db.Column(db.Float(64), unique=True,index=True) #列类型为浮点数

def __init__(self, onlinetime,cityname,weather,temp,wind):
    self.onlinetime = onlinetime
    self.cityname = cityname
    self.weather = weather
    self.temp = temp
    self.wind = wind

    def __repr__(self):
        return '< Weatherapi %r>' %(self.onlinetime, self.cityname,
                self.weather, self.temp, self.wind)

def insertweatherapi(data):
    data = fetchAPI(cityname)
    onlinetime = data[0],
    cityname = data[1],
    weather = data[2],
    temp = data[3],
    wind = data[4]
    con = engine.connect()
    con.execute(weatherapi.insert(onlinetime = 'data[0]',cityname = 'data[1]',
                weather = 'data[2]',temp = 'data[3]',wind = 'data[4]'))

    db.session.add(weatherapi)
    db.session.commit()
