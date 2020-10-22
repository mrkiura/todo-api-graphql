from ariadne import convert_kwargs_to_snake_case

from .models import Todo


def resolve_todos(obj, info):
    todos = [todo.to_dict() for todo in Todo.query.all()]
    return todos


@convert_kwargs_to_snake_case
def resolve_todo(obj, info, todo_id):
    todo = Todo.query.get(todo_id)
    return todo.to_dict()
