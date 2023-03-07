from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  gender = None
  interest = None
  numbers = [1,2,2,5]
  with open("data.txt","r") as file:
    msg = file.read()
  if request.method == 'POST':
      name = request.form['name']
      gender = request.form['gender']
      interest = ', '.join(request.form.getlist('interest'))
      with open('data.txt', 'a') as file:
        file.write(name + ' ' + gender + ' ' + interest + '\n')
  return render_template('index.html', name=name, gender=gender, interest=interest, intro=msg, nums=numbers)
  
app.run(host='0.0.0.0', port=81)
