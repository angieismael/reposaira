'''
created  on 19/1/2015

@Author: PC28
'''

from flaskext.mysql import MySQL
from flask import Flask

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'python1'
app.config['MYSQL_DATABASE_PASSWORD'] = 'teamoandres'
app.config['MYSQL_DATABASE_DB'] = 'ventas1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

con=mysql.connect().cursor()
con.execute("select * from personas")
report=con.fetchall()
print report
