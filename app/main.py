from typing import Union, List, Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Depends

from app.connection.database import engine,sessionLocal
from sqlalchemy.orm import Session




app = FastAPI()

def get_db():
    db = sessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependancy = Annotated[Session, Depends(get_db)]




# @app.post("/questions/")


# async def create_questions(question: QuestionBase, db: db_dependancy):
#     db_question = models.Questions(question_text=question.question_text)
#     db.add(db_question)
#     for choices in question.choices:
#         db_choice = models.Choices(choice_text=choice.choice_text, is_correct=choice.is_correct, question_id=db_question.id)
#         db.add(db_choices)

#     db.commit()

