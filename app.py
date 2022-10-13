from dataclasses import dataclass
from docutils import ApplicationError
from flask import Flask, redirect, url_for, render_template, request, flash
import pymysql
import pandas as pd
from tables import Description
import webbrowser
from datetime import datetime
app = Flask(__name__)
TEMPLATES_AUTO_RELOAD = True


@app.route('/newinfo', methods=['POST'])
def newinfo():
    if request.method == "POST":
        location = request.form.get("location")
        type = request.form.get("type")
        #dt = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        mydatabase = pymysql.connect(host='localhost', user='root', port=3307,
                                     passwd='', database='store_form')
        mycursor = mydatabase.cursor()
        query = "insert into store_info(location,JobType) values(%s,%s);"
        try:
            mycursor.execute(query, (location, type))
        except Exception as e:
            return render_template('Error.html', Error=e)
        mydatabase.commit()
        mydatabase.close()
    return redirect(url_for('insert'))


@app.route('/loadnew2', methods=['GET', 'POST'])
def loadnew2():
    return render_template('info.html')


@app.route('/newjd', methods=['POST'])
def newjd():
    if request.method == "POST":
        Role = request.form.get("job_role")
        Practice = request.form.get("practice")
        Description = request.form.get("Description")
        Skills = request.form.get("Skills")
        Nice = request.form.get("Nice")
        dt = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        mydatabase = pymysql.connect(host='localhost', user='root', port=3307,
                                     passwd='', database='store_form')
        mycursor = mydatabase.cursor()
        query = "insert into store_role(Job_Role,Practice,Job_Description,Mandatory_Skills,Nice_To_Have_Skills,CreatedDate) values(%s,%s,%s,%s,%s,%s);"
        try:
            mycursor.execute(
                query, (Role, Practice, Description, Skills, Nice, dt))
        except Exception as e:
            return render_template('Error.html', Error=e)
        mydatabase.commit()
        mydatabase.close()
    return redirect(url_for('insert'))


@app.route('/loadnew', methods=["GET", "POST"])
def loadnew():
    return render_template('jd.html')


@app.route('/database', methods=['POST'])
def database():

    if request.method == "POST":
        JobID = request.form.get("JobID")
        Role = request.form.get("Role")
        Practice = request.form.get("Practice")
        exp = request.form.get("exp")
        location = request.form.get("location")
        JobType = request.form.get("JobType")
        JobDescription = request.form.get("des")
        Skills = request.form.getlist("skills")
        Skills = '\r\n\r\n'.join(map(str, Skills))
        NiceSkills = request.form.getlist("skills2")
        NiceSkills = '\r\n\r\n'.join(map(str, NiceSkills))
        WhyWavelabs = request.form.get("selprograms2")
        FindUs = request.form.get("findus")
        mydatabase = pymysql.connect(host='localhost', user='root', port=3307,
                                     passwd='', database='jd_form')
        mycursor = mydatabase.cursor()
        try:

            query = "insert into JobRole(JobID,JobRole) values(%s,%s);"
            mycursor.execute(query, (JobID, Role))
        except Exception as e:
            return render_template('Error.html', Error=e)
        try:
            query = "insert into JobDetails(JobID,YOE,Location,Type) values(%s,%s,%s,%s);"
            mycursor.execute(query, (JobID, exp, location, JobType))

        except Exception as e:
            return render_template('Error.html', Error=e)
        try:
            query = "insert into JobSkills(JobID,Description,Skills,NiceSkills) values(%s,%s,%s,%s);"
            mycursor.execute(
                query, (JobID, JobDescription, Skills, NiceSkills))

        except Exception as e:
            return render_template('Error.html', Error=e)
        try:
            query = "insert into SpatialDetails(JobID,WhyWavelabs,FindUs) values(%s,%s,%s);"
            mycursor.execute(query, (JobID, WhyWavelabs, FindUs))
        except Exception as e:
            return render_template('Error.html', Error=e)
        try:
            query = "insert into Practice(JobID,Practice) values(%s,%s);"
            mycursor.execute(query, (JobID, Practice))
        except Exception as e:
            return render_template('Error.html', Error=e)
        mydatabase.commit()
        mydatabase.close()
    return redirect(url_for('insert'))


@app.route('/data', methods=['GET', 'POST'])
def data():
    JobID = request.form.get('JobID')
    Role = request.form.get('Role')
    Practice = request.form.get('Practice')
    mydatabase = pymysql.connect(
        host='localhost', user='root', port=3307,
        passwd='', database='store_form')

    mycursor = mydatabase.cursor()

    # There you can add home page and others. It is completely depends on you

    mycursor.execute('SELECT * FROM store_role')
    rows = mycursor.fetchall()
    df = pd.DataFrame(rows)
    L1 = {}
    L2 = {}
    Description = {}
    for i in range(df.shape[0]):
        if df.iloc[i, 0] == Role:

            description = df.iloc[i, 2]
            Description[Role] = description
            s = df.iloc[i, 3]
            l = s.split('\r\n\r\n')
            L1[df.iloc[i, 0]] = l
            if df.iloc[i, 4] == 'empty':
                l2 = ''
            else:
                s2 = df.iloc[i, 4]
                l2 = s2.split('\r\n\r\n')
            L2[df.iloc[i, 0]] = l2
    mycursor.execute('SELECT * FROM store_info')
    rows = mycursor.fetchall()
    df = pd.DataFrame(rows)
    L3 = []
    L4 = []
    for i in range(df.shape[0]):
        if df.iloc[i, 0] not in L3:
            L3.append(df.iloc[i, 0])
        if df.iloc[i, 1] not in L4:
            L4.append(df.iloc[i, 1])

    return render_template('form.html', JobID=JobID, Role=Role, Practice=Practice, Description=Description, data=L1, data2=L2, location=L3, JobType=L4)
    mydatabase.close()


@app.route('/')
def insert():

    mydatabase = pymysql.connect(
        host='localhost', user='root', port=3307,
        passwd='', database='store_form')

    mycursor = mydatabase.cursor()

    # There you can add home page and others. It is completely depends on you

    mycursor.execute('SELECT * FROM store_role')
    rows = mycursor.fetchall()
    df = pd.DataFrame(rows)
    Role = []
    Practice = []
    for i in range(df.shape[0]):
        if df.iloc[i, 0] not in Role:
            Role.append(df.iloc[i, 0])
        if df.iloc[i, 1] not in Practice:
            Practice.append(df.iloc[i, 1])
    mydatabase.close()
    return render_template('insert.html', Role=Role, Practice=Practice)


@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


if __name__ == '__main__':
    app.run(debug=True)
