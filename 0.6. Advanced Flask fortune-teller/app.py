from flask import Flask,render_template,request,url_for,redirect
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("hello.html")
    else:
        month = request.form['birthday']
        return redirect(url_for('fortune',x=month ))


fortune_list=["You will find money in the pocket of a coat you haven't worn in years.",
"Your car will magically avoid potholes today.",
"You will discover the secret to perfect microwave popcorn.",
"A typo in your favor will lead to an amusing email exchange.",
"You'll impress everyone with your flawless dance moves at an unexpected event.",
"A bird will mistake you for a Disney princess and serenade you.",
"Your pet will learn a new trick that will leave you in stitches.",
"You will accidentally match outfits with a stranger and become temporary best friends.",
"You'll find the last slice of pizza hidden in the fridge, untouched and waiting for you.",
"Your phone will autocorrect a serious message into a hilarious meme, and everyone will love it."]

@app.route('/fortune_telling/<birthM>')
def fortune(x):
    
    birthLength = len(x)
    finalFortune = fortune_list[5]
    if birthLength<10:
        finalFortune = fortune_list[birthLength-1]
    return render_template("fortune.html", fortune = finalFortune)




    
if __name__ == '__main__':
    app.run(debug=True)
