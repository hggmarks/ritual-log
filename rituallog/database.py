import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel.sql.expression import Select, SelectOfScalar
from sqlmodel import create_engine, Session
from rituallog.config import settings
from rituallog import models


warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True


engine = create_engine(settings.database.url)

#models.SQLModel.metadata.create_all(settings.database.url)

def get_session():
    return Session(engine)
