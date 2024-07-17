from flask import Flask,render_template,request,url_for,redirect
import random

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/home', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("hello.html")
    else:
        month = request.form['birthday']
        return redirect(url_for('fortune',birthM=month ))


fortune_list=["Great opportunities await you in the near future. Stay alert and be ready to seize them.",
"A journey of a thousand miles begins with a single step. Take that first step with confidence.",
"Your creativity and hard work will soon be recognized and rewarded.",
"Unexpected financial gains are coming your way. Prepare wisely.",
"Love and happiness will surround you this year. Embrace it with an open heart.",
"Challenges will test your resilience, but they will also strengthen your character.",
"A new friendship will bring joy and positivity into your life.",
"Health and vitality will be your allies in achieving your goals this season.",
"Trust your instincts in making decisions; they will lead you in the right direction.",
"Generosity towards others will bring you inner peace and fulfillment."]

@app.route('/fortune_telling/<birthM>')
def fortune(birthM):
    
    birthLength = len(birthM)
    finalFortune = fortune_list[9]
    if birthLength<10:
        finalFortune = fortune_list[birthLength-1]
    return render_template("fortune.html", fortune = finalFortune)




    
if __name__ == '__main__':
    app.run(debug=True)