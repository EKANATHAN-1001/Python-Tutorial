from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'student'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route("/")
def home():
    con = mysql.get_db().cursor()
    sql = 'select * from IT'
    con.execute(sql)
    res = con.fetchall()
    return render_template('index.html',datas=res)
if(__name__ == '__main__'):
    app.run(debug=True)