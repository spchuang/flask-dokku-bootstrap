import os
from .constants import INSTANCE_FOLDER_PATH

class BaseConfig(object):

   PROJECT = "app" 
   
   # Get app root path, also can use flask.root_path.
   PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
   
   DEBUG = False
   TESTING = False
   
   ADMINS = ['youremail@yourdomain.com']
   
   # http://flask.pocoo.org/docs/quickstart/#sessions
   SECRET_KEY = 'secret key'
   

class DefaultConfig(BaseConfig):

   # Enable protection agains *Cross-site Request Forgery (CSRF)*
   WTF_CSRF_ENABLED = True
   
   # Statement for enabling the development environment
   DEBUG = True
   
   
   # Enable protection agains *Cross-site Request Forgery (CSRF)*
   WTF_CSRF_ENABLED = True
   
   # Secret key for signing cookies
   SECRET_KEY = 'development key'
   
   # Define the database
   DB_CONFIG = {
 
   }
   
   SQLALCHEMY_ECHO = False
   SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s"%(DB_CONFIG['USER'], DB_CONFIG['PASS'],DB_CONFIG['HOST'],DB_CONFIG['DB'])

