'''
Created on 19/1/2015

@author: PC28
'''
from flaskext.mysql import MySQL
from flask import Flask

class DBcon():
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        pass
    
    def conexion(self):
        mysql = MySQL()
        app = Flask(__name__)
        app.config['MYSQL_DATABASE_USER'] = 'python1'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'teamoismael'
        app.config['MYSQL_DATABASE_DB'] = 'ventas1'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)
                
        return mysql        