from werkzeug import generate_password_hash, check_password_hash
from flask.ext.login import UserMixin

from ..helpers import JsonSerializer, get_current_time
from ..extensions import db
from . import constants as USER
from .constants import STRING_LEN, PW_STRING_LEN

class UserJsonSerializer(JsonSerializer):
    __json_public__ = ['id', 'email', 'user_name']
    __json_modifiers__ = {
      'role_code' : ['role', (lambda code : USER.USER_ROLE[code])]
    }
    
    
class User(db.Model, UserMixin, UserJsonSerializer):

   __tablename__ = "user"
   def __repr__(self):
      return '<User %r>' % (self.user_name)
      
   id            = db.Column(db.Integer, primary_key = True)
   first_name    = db.Column(db.String(STRING_LEN), nullable=False)
   last_name     = db.Column(db.String(STRING_LEN), nullable=False)
   user_name     = db.Column(db.String(STRING_LEN),  index = True, unique = True, nullable=False)
   email         = db.Column(db.String(STRING_LEN), index = True, unique = True, nullable=False)
   created_on    = db.Column(db.DateTime, nullable=False, default = get_current_time)
   
   # ================================================================
   # User Password
   
   _password = db.Column('password', db.String(PW_STRING_LEN), nullable=False)
   
   def _get_password(self):
      return self._password

   def _set_password(self, password):
      self._password = generate_password_hash(password)
   
   password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))
   
   def check_password(self, password):
      
      if self.password is None:
         return False
      return check_password_hash(self.password, password)
        
   # ================================================================
   # User role
   
   role_code = db.Column(db.SmallInteger, default=USER.USER, nullable=False)
   
   @property
   def role():
      return USER.USER_ROLE[self.role_code]
   
   
   def is_admin(self):
      return self.role_code == USER.ADMIN
   
   # ================================================================
   # User status
   
   status_code = db.Column(db.SmallInteger, default=USER.INACTIVE)
   
   @property
   def status(self):
      return USER.USER_STATUS[self.status_code]
   
   # ================================================================
   # Class methods

   @classmethod
   def authenticate(self, login, password):
      user = self.query.filter(db.or_(User.user_name == login, User.email == login)).first()
      print user
      if user:
         authenticated = user.check_password(password)
      else:
         authenticated = False
      
      return user, authenticated
   
   @classmethod
   def authenticate_fb(self, fb_id):
      user = self.query.filter(fb_id=fb_id).first()
      return user
   