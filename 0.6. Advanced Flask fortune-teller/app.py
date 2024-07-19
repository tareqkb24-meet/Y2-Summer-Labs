from flask import Flask,render_template,request,url_for,redirect
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("hello.html",)
    else:
        birthmonth = request.form['birthday']
        return redirect(url_for('fortune', birthmonth=birthmonth),'<h1>I’m not sure what will happen to you, but it will be one of the following three things:</h1>')

@app.route('/fortune2')
def fortune2():
    return render_template("fortune2.html")
    

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
@app.route('/fortune_telling/<birthmonth>')
def fortune(birthmonth):
    birthLength = len(birthmonth)
    finalFortune = fortune_list[9]
    if birthLength<10:
        finalFortune = fortune_list[birthLength-1]
    return render_template("fortune.html", fortune = finalFortune)


@app.route('/indecisive')
def indecisive():
    fortunelist2=["You will find money in the pocket of a coat you haven't worn in years.",
"Your car will magically avoid potholes today.",
"You will discover the secret to perfect microwave popcorn.",
"A typo in your favor will lead to an amusing email exchange.",
"You'll impress everyone with your flawless dance moves at an unexpected event.",
"A bird will mistake you for a Disney princess and serenade you.",
"Your pet will learn a new trick that will leave you in stitches.",
"You will accidentally match outfits with a stranger and become temporary best friends.",
"You'll find the last slice of pizza hidden in the fridge, untouched and waiting for you.",
"Your phone will autocorrect a serious message into a hilarious meme, and everyone will love it."]
    
    indecisive_fortunes = random.sample(fortunelist2, 3)
    return render_template('indecisive.html', fortunes=indecisive_fortunes)



if __name__ == '__main__':
    app.run(debug=True)
