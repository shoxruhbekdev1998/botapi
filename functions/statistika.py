from fastapi import HTTPException
from models.statistika import Statistika
from utils.pagination import pagination


def all_satatistikas(topic_name,question_name, id, from_date, end_date, page, limit, db, status):
    statistikas = db.query(Statistika).filter(Statistika.id >= 0)

    if topic_name:
        statistikas = statistikas.filter(Statistika.topic_name == topic_name)
    if question_name:
        statistikas = statistikas.filter(Statistika.question_name == question_name)
    if id:
        statistikas = statistikas.filter(Statistika.id == id)

    if from_date and end_date:
        statistikas = statistikas.filter(Statistika.date >= from_date, Statistika.date <= end_date)

    if status == True:
        statistikas = statistikas.filter(Statistika.status == status)

    elif status == False:
        statistikas = statistikas.filter(Statistika.status == status)

    else:
        statistikas = statistikas.filter(Statistika.id >= 0)

    return pagination(form=statistikas, page=page, limit=limit)


def statistika_adding(topic_name, question_name, answer_a, answer_b, answer_c, answer_d, answer_e, answer_f, db):
    statistikas = db.query(Statistika).filter(Statistika.topic_name == topic_name,Statistika.question_name == question_name).first()
    if statistikas is None:
        statistikas = Statistika(
            topic_name=topic_name,
            question_name=question_name,
            answer_a=0,
            answer_b=0,
            answer_c=0,
            answer_d=0,
            answer_e=0,
            answer_f=0
        )
        db.add(statistikas)



    answers = ['answer_a', 'answer_b', 'answer_c', 'answer_d', 'answer_e', 'answer_f']
    for answer in answers:
        if locals().get(answer) is not None:
            new_answer = getattr(statistikas, answer) + locals().get(answer)
            db.query(Statistika).filter(Statistika.topic_name == topic_name).update({
                getattr(Statistika, answer): new_answer
            })

    db.commit()
    return {"data": "Statistika update base"}


def add_statistikas(form, db):
    statistika_adding(
        topic_name=form.topic_name,
        question_name=form.question_name,
        answer_a=form.answer_a,
        answer_b=form.answer_b,
        answer_c=form.answer_c,
        answer_d=form.answer_d,
        answer_e=form.answer_e,
        answer_f=form.answer_f,
        db=db
    )

    return {"data": "Statistika add base"}

def update_statistikas(id, form, db):
    if one_statistika(id=form.id, db=db) is None:
        raise HTTPException(status_code=400, detail="Bunday raqamli answer yo'q")

    db.query(Statistika).filter(Statistika.id == id).update({
        Statistika.topic_name: form.topic_name,
        Statistika.question_name: form.question_name,
        Statistika.answer_a: form.answer_a,
        Statistika.answer_b: form.answer_b,
        Statistika.answer_c: form.answer_c,
        Statistika.answer_d: form.answer_d,
        Statistika.answer_e: form.answer_e,
        Statistika.answer_f: form.answer_f,
    })
    db.commit()


def one_statistika(id, db):
    return db.query(Statistika).filter(Statistika.id == id).first()


def delete_statistikas(id, db):
    db.query(Statistika).filter(Statistika.id == id).update({
        Statistika.status: False
    })

    db.commit()
    return {"data": "Malumot o'chirildi"}


