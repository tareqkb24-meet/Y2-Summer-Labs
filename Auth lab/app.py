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
  "databaseURL":"https://auth-lab-7d39f-default-rtdb.firebaseio.com/"

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
        user = {
                'email': email,
                'password': password,
                'full_name': request.form['full_name'],
                'username': request.form['username']
            }
        login_session['user'] = user
        uid = login_session['user']['uid']
        ref.child('Users').child(uid).set(user)

        
        login_session['quotes'] = []
        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            return redirect('/home')

        except Exception as e:
            error = "Auth failed"
            print(e)
            return render_template("error.html")
    else:
    
        return render_template('signup.html')


@app.route('/signin', methods=['GET','POST'])
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
    auth.signOut()
    login_session['user']=None
    return redirect(url_for('signin'))



@app.route('/home', methods=['POST','GET'])
def home():
    if request.method == 'POST':
        quote = request.form['quote']
        quote = {
                'text': email,
                'said_by': password,
                'uid': uid
            }
            
            
            
        ref.child('Quotes').child('username').set(quote)

        login_session.modified = True
        return redirect(url_for('thanks'))
    else:
        return render_template("home.html")


@app.route('/thanks',methods=['POST','GET'])
def thanks():
    return render_template('thanks.html')

@app.route('/display',methods=['POST','GET'])
def display():
    how = db.child("quote").get().val()
    return render_template('display.html', quotes=how)

@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)