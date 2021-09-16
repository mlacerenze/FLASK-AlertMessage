from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField 
from wtforms.validators import DataRequired # para que no quede vacio el campo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secreyKey'

class Form(FlaskForm):
  name = StringField('Name', validators=[DataRequired()])
  btn = SubmitField('Send')  

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/message', methods=['GET', 'POST'])
def message():
  form = Form()
  if form.validate_on_submit():
    flash('Hello, ' + form.name.data + '! Thanks for send us your information.')
    return redirect(url_for('message'))
  return render_template('message.html', form=form)

# @app.route('/route_name')
# def method_name():
#     pass

if __name__ == '__main__':
  app.run(debug= True, port= 8000)