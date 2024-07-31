from flask import Flask,render_template,request,url_for,redirect
from flask import session as login_session
import pyrebase





app = Flask(__name__,template_folder = "templates",static_folder='static')



Config = {

  "apiKey": "AIzaSyAMv8YO5m-D4nijKrEw-0QaAOVe9OhttPc",
  "authDomain": "auth-lab-7d39f.firebaseapp.com",
  "projectId": "auth-lab-7d39f",
  "storageBucket": "auth-lab-7d39f.appspot.com",
  "messagingSenderId": "728865669574",
  "appId": "1:728865669574:web:3a201be064582dbefe32c7",
  "measurementId": "G-42XPB93DRR", 
  "databaseURL":"https://fittnesweb-default-rtdb.europe-west1.firebasedatabase.app/"

}
   
app.config['SECRET_KEY'] = 'super_secret_key'




firebase = pyrebase.initialize_app(Config)
db =firebase.database()
auth = firebase.auth()
@app.route('/signup', methods=['GET', 'POST']) 
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['fullname']
        username = request.form['Username']
        
        
        try:

            user = auth.create_user_with_email_and_password(email, password)
            login_session['user'] = user
            login_session['quotes'] = []
           
            return redirect(url_for('home'))

        except:
            error = "Auth failed"
            print(error)
            return render_template("error.html")
    
    
    return render_template('signup.html')




@app.route("/signin", methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        try:
            user  = auth.sign_in_with_email_and_password(email, password) 

            login_session['user'] = user
            login_session['quotes'] = []

        
            return redirect('/home')
        except:
            error = "Auth failed"
            print(error)
            return render_template("error.html")
    else:
        return render_template('signin.html')
@app.route('/signout',methods=['POST','GET'])
def signout():
  login_session['user']=None
  auth.current_user= None
  return redirect(url_for('signin'))

@app.route('/getstart', methods=['POST', 'GET'])
def get_started():
  return render_template('get.html')
@app.route('/first', methods=['GET', 'POST'])
def first():

  return render_template('first.html')
@app.route('/second', methods=['POST', 'GET'])
def second():

  return render_template('second.html')
@app.route('/second_engine', methods=['POST', 'GET'])
def second_engine():
    calories = request.form['calories']
    calories_gain = request.form['calories_gain' ]
    calorie={
    'calories_burnt': calories ,
    'calories_gain': calories_gain
  }
    UID = login_session['user']["localId"]
    db.child("users").child(UID).child("calories").set(calorie)
    com = db.child("users").child(UID).child("calories").get().val()
    calorie1={
    'calories_burnt': int(com['calories_burnt'])+int(calories) ,
    'calories_gain': int(com['calories_gain'])+int(calories_gain)
  }
    db.child("users").child(UID).child("calories").update(calorie1)
    # com2 += db.child("users").child(UID).child("calories_gain").get().val()
  # login_session['calories_gain'] = calories_gain
    my_cals = db.child("users").child(UID).child("calories").get().val()
    return render_template("second_engine.html" , cals = my_cals)


@app.route('/home', methods=['POST','GET'])
def home():
    return render_template("/home.html")
@app.route('/orginal', methods=['POST','GET'])
def orginal():
    return render_template("/orginal.html")           
            

# def combine():

#     com = db.child("users").child(UID).child("calories").get().val()
#     com+=
#     return com2


@app.route('/submit', methods=['POST'])
def submit():



   
    weight = request.form.get('weight')
    height = request.form.get('height')

  

    
    return redirect(url_for('firstengine'))

@app.route('/firstengine', methods=['POST', 'GET'])
def firstengine():
  
    age = request.form.get('age')
    weight = float(request.form.get('weight'))
    height = int(request.form.get('height'))
    gender = request.form.get('gender')
    activity_level = float(request.form.get('activity_level'))

    
    bmr = calculate_bmr(age, weight, height, gender)
    tdee = calculate_tdee(bmr, activity_level)

    
    calorie_intake = int(tdee)  

    
    food_schedule = f"Recommended daily calorie intake: {calorie_intake} calories."

    return render_template('recommendation.html', recommendation=food_schedule)    

def calculate_bmr(age, weight, height, gender):
    if gender == 'male':
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif gender == 'female':
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    else:
        bmr = 0  
    return bmr
def calculate_tdee(bmr, activity_factor):
    tdee = bmr * activity_factor
    return tdee


if __name__ == '__main__':
    app.run(debug=True)