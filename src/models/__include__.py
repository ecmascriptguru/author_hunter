import datetime
from datetime import timedelta
from sqlalchemy import desc, asc, or_, func
from flask_sqlalchemy import SQLAlchemy
from flask_login import current_user
from string import Formatter

db = SQLAlchemy()
session = db.session
