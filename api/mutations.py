from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Todo


@convert_kwargs_to_snake_case
def resolve_create_todo(obj, info, description, due_date):
    due_date = datetime.strptime(due_date, '%d-%m-%Y').date()
    todo = Todo(
        description=description, due_date=due_date
    )
    db.session.add(todo)
    db.session.commit()
    return todo.to_dict()


@convert_kwargs_to_snake_case
def resolve_mark_done(obj, info, todo_id):
    todo = Todo.query.get(todo_id)
    todo.completed = True
    db.session.add(todo)
    db.session.commit()
    return todo.to_dict()


@convert_kwargs_to_snake_case
def resolve_delete_todo(obj, info, todo_id):
    todo = Todo.query.get(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return {"success": True}
    else:
        return {"success": False}


@convert_kwargs_to_snake_case
def resolve_update_due_date(obj, info, todo_id, new_date):
    todo = Todo.query.get(todo_id)
    if todo:
        todo.due_date = datetime.strptime(new_date, '%d-%m-%Y').date()
    db.session.add(todo)
    db.session.commit()
    return todo.to_dict()
