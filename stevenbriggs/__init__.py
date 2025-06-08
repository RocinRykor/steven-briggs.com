import os
import sys
from . import app

db = app.db

# This site was started on 2020-03-25

basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(basedir)

application = app.application
