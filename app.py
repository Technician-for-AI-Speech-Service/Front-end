from flask import Flask, jsonify, Blueprint, redirect, request, render_template, send_from_directory, session, url_for, flash
from flask_mysqldb import MySQL
import pymysql
import pandas as pd
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter
import secrets
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_hex(16)


# connection = pymysql.connect(host='',  port = 3307, user = ) # 아래와 동일

app.config['MYSQL_HOST'] = 'project-db-stu3.smhrd.com'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'Insa4_IOTB_final_3'
app.config['MYSQL_PASSWORD'] = 'aischool3'
app.config['MYSQL_DB'] = 'Insa4_IOTB_final_3'

mysql = MySQL(app)

@app.route('/')
def main():
    return render_template("/main/index.html")


@app.route('/user/registerForm')
def registerForm():
    return render_template('/user/register.html')

@app.route('/user/mypage')
def mypageForm():
    if 'user' in session:
        return render_template('/user/mypage.html')

@app.route('/user/loginForm')
def loginForm():
    return render_template('/user/login.html')

# 로그인 처리
@app.route('/user/login', methods = ['POST'])
def login():
    user_Id = request.form.get('user_Id')
    user_Pwd = request.form.get('user_Pwd')
    
    cur = mysql.connection.cursor()
    query = "SELECT * FROM t_User where user_Id = %s and user_Pwd = %s"
    cur.execute(query, (user_Id, user_Pwd))
    result = cur.fetchone()
   
    mysql.connection.commit()
    cur.close()
from flask import Flask, jsonify, Blueprint, redirect, request, render_template, send_from_directory, session, url_for, flash
from flask_mysqldb import MySQL
import pymysql
import pandas as pd
import numpy as np
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_paginate import Pagination, get_page_parameter
import secrets
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = secrets.token_hex(16)


# connection = pymysql.connect(host='',  port = 3307, user = ) # 아래와 동일

app.config['MYSQL_HOST'] = 'project-db-stu3.smhrd.com'
app.config['MYSQL_PORT'] = 3307
app.config['MYSQL_USER'] = 'Insa4_IOTB_final_3'
app.config['MYSQL_PASSWORD'] = 'aischool3'
app.config['MYSQL_DB'] = 'Insa4_IOTB_final_3'

mysql = MySQL(app)

@app.route('/')
def main():
    return render_template("/main/index.html")


@app.route('/user/registerForm')
def registerForm():
    return render_template('/user/register.html')

@app.route('/user/loginForm')
def loginForm():
    return render_template('/user/login.html')

# 로그인 처리
@app.route('/user/login', methods = ['POST'])
def login():
    user_Id = request.form.get('user_Id')
    user_Pwd = request.form.get('user_Pwd')
    
    cur = mysql.connection.cursor()
    query = "SELECT * FROM t_User where user_Id = %s and user_Pwd = %s"
    cur.execute(query, (user_Id, user_Pwd))
    result = cur.fetchone()
   
    mysql.connection.commit()
    cur.close()
    
    if result:
        (user_Name, user_Id, user_Phone, user_Pwd, user_Gender, user_Disability, 
        user_Year, user_Region, user_Phone1, user_Phone2, user_Phone3, user_Date, 
        user_PostNumber, user_Address, user_Details) = result

        # flash('로그인 완료', category='success')
        
        keys = ['user_Name', 'user_Id', 'user_Phone', 'user_Pwd', 'user_Gender', 'user_Disability', 
                'user_Year', 'user_Region', 'user_Phone1', 'user_Phone2', 'user_Phone3', 'user_Date', 
                'user_PostNumber', 'user_Address', 'user_Details']
        user = dict(zip(keys, result))
        session['user'] = user
        flash('로그인 완료', category = 'success')

        return jsonify({'message': 'success', 'user_Name': user_Name}), 200
    else:
        return jsonify({'message': 'failed'}), 401
        

            
# 회원가입 처리
@app.route('/user/register', methods = ['POST'])
def register():
    user_Name = request.form.get('user_Name')
    user_Id = request.form.get('user_Id')
    user_Phone1 = request.form.get('user_Phone1')
    user_Phone2 = request.form.get('user_Phone2')
    user_Phone3 = request.form.get('user_Phone3')
    user_Pwd = request.form.get('user_Pwd')
    user_Gender = request.form.get('user_Gender')
    user_Disabilty = request.form.get('user_Disabilty')
    user_Date = request.form.get('user_date')
    user_PostNumber = request.form.get('user_PostNumber')
    user_Address = request.form.get('user_Address')
    user_Details = request.form.get('user_Details')
    
@app.route('/user/logout')
def logout():
    session.pop('user',None)
    # session.clear()
    flash('로그아웃 완료', category='success')
    return redirect('/')

# 실행
if __name__ == '__main__':
    app.run(debug=True)