from fastapi import APIRouter,Depends,HTTPException
from pydantic.datetime_parse import date

from db import Base,engine,get_db

from sqlalchemy.orm import Session

from routes.auth import get_current_active_user
from schemas.users import UserCurrent

Base.metadata.create_all(bind=engine)
from functions.statistika import add_statistikas, all_satatistikas, update_statistikas, delete_statistikas
from schemas.statistika import *

router_statistika = APIRouter()

@router_statistika.post('/add')
def add_statistika(form:StatistikaCreate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if add_statistikas(form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")


@router_statistika.get('/',status_code=200)
def get_statistika(id:int=0,topic_name:str=None,question_name:str=None,from_date:str=None,end_date:str=None,page:int=1,limit:int=5,status:bool=None,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

        return all_satatistikas(db=db,status=status,id=id,topic_name=topic_name,question_name=question_name,from_date=from_date,end_date=end_date,page=page,limit=limit)



@router_statistika.put('/update',)
def update_statistika(form:StatistikaUpdate,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):

    if update_statistikas(id=form.id,form=form,db=db):
        raise HTTPException(status_code=200, detail="Amaliyot muvofaqqiyatli bajarildi")

@router_statistika.delete('/del',)
def delete_statistika(id:int,db: Session = Depends(get_db),current_user: UserCurrent = Depends(get_current_active_user)):
    return delete_statistikas(id=id,db=db)



