from flask import Flask,render_template,request,redirect,url_for
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    instructors = ['mani','rajagopal']
    name = 'Tom'
    return render_template('index.html',names=instructors,name=name)

@app.route('/name')
def name():
    names = ['Tom','John']
    name='Tom'
    return render_template('name.html', names=names, name=name)

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/name/<person>')
def retname(person):
    return f"The name is {person}"

@app.route('/name/<int:num>')
def retnum(num):
    return  f"Square of {num} is {num*num}"


@app.route('/contacts')
def contact():
    return render_template('first_form.html')

@app.route('/data')
def data():
    first = request.args.get('first')
    last = request.args.get('last')
    return f"First:{first}, Last:{last}"

@app.route('/data2')
def data2():
    first=request.args.get('first')
    last=request.args.get('last')
    return f"FirstName:{first}, LastName: {last}"


toys = ['lego', 'catan', 'disney']


@app.route('/toys', methods=["GET","POST"])
def toys_get():
    if request.method == "POST":
        toys.append(request.form['name'])
        ##return redirect(url_for('toys_get'))
    return render_template('toys_index.html', toys=toys)

@app.route('/toys/new')
def toys_new():
    return render_template('toys_new.html')

@app.route('/toys_db', methods=["GET","POST"])
def toys_get_db():
    if request.method == "POST":
        toysadd(request.form['name'])
    return render_template('toys_index_db.html', toys=getalltoys())

@app.route('/toys/new_DB')
def toys_new_DB():
    return render_template('toys_new_db.html')

def connect():
    constring = "host='localhost' dbname='users'"
    c=psycopg2.connect(constring)
    return c

def getalltoys():
    conn = connect()
    cur=conn.cursor()
    cur.execute("select toyid,toyname from toys")
    toys=cur.fetchall()
    cur.close()
    conn.close()
    return toys

def toysadd(toyname):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"Insert into toys (toyname) values ('{toyname}')")
    conn.commit()
    cur.close()
    conn.close()