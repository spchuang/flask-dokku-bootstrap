'''
   Serves Flask static pages (index, login, signup, etc)
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort)
from flask.ext.login import login_required, login_user, current_user, logout_user, confirm_login, login_fresh
from ..extensions import db, login_manager

from ..users.models import User
from ..users.forms import SignupForm, LoginForm


frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index(path=None):
    return render_template('index.html')

    
    #return render_template('index.html')
    

@frontend.route('/signup', methods=['GET', 'POST'])
def signup():
   

   form = SignupForm(next=request.args.get('next'))
   if form.validate_on_submit():
      user = User()
      form.populate_obj(user)

      db.session.add(user)
      db.session.commit()
      return redirect(url_for('frontend.login'))

   return render_template('frontend/signup.html', form=form)
   

@frontend.route('/login', methods=['GET', 'POST'])
def login():
   if current_user.is_authenticated():
        return redirect(url_for('frontend.index'))
        
   form = LoginForm(next=request.args.get('next'))
   
   if form.validate_on_submit():
      user, authenticated = User.authenticate(form.login.data,
                                              form.password.data)                         
      if user and authenticated:
         remember = form.remember_me.data
         if login_user(user, remember=remember):
            return redirect(form.next.data or url_for('frontend.index'))

      else:
         flash(_('Sorry, invalid login'), 'error')
            
   return render_template('frontend/login.html', form=form)


@frontend.route('/logout', methods=['GET'])
def logout():
   session.pop('login', None)
   logout_user()
   return redirect(request.referrer or url_for('frontend.login'))
   
