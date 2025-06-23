from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s"
})
db = SQLAlchemy(metadata=metadata)


from .user import User
from .guest import Guest
from .episode import Episode
from .appearance import Appearance
