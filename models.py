import imp
from sqlalchemy import Integer,Column,String,Boolean
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    id = Column(Integer,Primary_key=True)
    username = 