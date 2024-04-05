from flask import Flask , render_template
app = Flask(__name__)
@app.route("/")
def home():

    name = "Yashvi" 
    age = "15"
    return render_template('index.html' , name = name , age = age)

@app.route("/mother")
def mother():
    
    name = "mother" 
    age = "35"
    return render_template('mother.html' , name = name , age = age)

@app.route("/father")
def father():

    name = "father" 
    age = "40"
    return render_template('father.html' , name = name , age = age)

@app.route("/friend")
def friend():
    name = "blah" 
    age = "15"
    return render_template('friend.html' , name = name , age = age)

app.run()