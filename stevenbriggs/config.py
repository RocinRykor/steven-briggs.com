import os
import datetime


basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'stevenbriggs'
DB_USER = 'stevenbriggs'


class Config():
    SECRET_KEY = "#CHANGED AND REDACTED#" 
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{SECRET_KEY}@' \
                              f'localhost/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Comment out the following when going live
    SEND_FILE_MAX_AGE_DEFAULT = datetime.timedelta(seconds=0)
