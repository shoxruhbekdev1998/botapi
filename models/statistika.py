import datetime

from sqlalchemy import Column, Integer, String, Boolean,Float,Text,ForeignKey,Date,DateTime,func

from sqlalchemy.orm import relationship

from db import Base


class Statistika(Base):
    __tablename__ = "Statistika"
    id = Column(Integer, primary_key=True,autoincrement=True)
    topic_name = Column(String(30), nullable=True)
    question_name = Column(String(30), nullable=True)

    answer_a = Column(Integer, nullable=True)
    answer_b = Column(Integer, nullable=True)
    answer_c = Column(Integer, nullable=True)
    answer_d = Column(Integer, nullable=True)
    answer_e = Column(Integer, nullable=True)
    answer_f = Column(Integer, nullable=True)

    date = Column(Date(),nullable = True,default=func.now())
    status = Column(Boolean, nullable = True ,default=True)


