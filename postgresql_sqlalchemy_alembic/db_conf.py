from sqlalchemy import create_engine, MetaData, insert, select, update, delete
from sqlalchemy import Table, Column, VARCHAR, Integer, Boolean
from sqlalchemy.orm import Session
from postgresql_sqlalchemy_alembic.models import TodoCreate, Todo
from typing import Annotated

engine = create_engine('postgresql://test_user_sql:admin_password@localhost/stepik_test')
metadata = MetaData()

todo = Table('todo', metadata,
             Column('id', Integer, primary_key=True),
             Column('title', VARCHAR(60)),
             Column('description', VARCHAR(160)),
             Column('completed', Boolean)
             )

def get_connection():
    return engine.connect()

def add_todo(todo_create: TodoCreate):
    with Session(engine) as session:
        result  = session.execute(insert(todo), todo_create.model_dump())
        session.commit()
    return {"id": result.inserted_primary_key[0], **result.last_inserted_params()}

def get_todo(todo_id: int):
    with Session(engine) as session:
        result = session.execute(select(todo).where(todo.c.id == todo_id)).mappings().first()
        return result

def update_todo(todo_id: int, todo_data: TodoCreate) -> Annotated[int, 'length of updated todo']:
    with Session(engine) as session:
        result = session.execute(update(todo).values(todo_data.model_dump()).where(todo.c.id == todo_id))  # c = column
        session.commit()
    return result.last_updated_params() if result.rowcount else 0

def delete_todo(todo_id: int) -> Annotated[int, 'count of deleted row']:
    with Session(engine) as session:
        result = session.execute(delete(todo).where(todo.c.id == todo_id))
        session.commit()
    return result.rowcount()
