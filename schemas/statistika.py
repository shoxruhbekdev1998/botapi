from pydantic import BaseModel
from typing import Optional,List

class StatistikaBase(BaseModel):

    topic_name:str
    question_name:str
    answer_a: Optional[int]=None
    answer_b: Optional[int]=None
    answer_c: Optional[int]=None
    answer_d: Optional[int]=None
    answer_e: Optional[int]=None
    answer_f: Optional[int]=None

class StatistikaCreate(StatistikaBase):
    pass

class StatistikaUpdate(StatistikaBase):
    id:int
    status:bool
