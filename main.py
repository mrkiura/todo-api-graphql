from api import app


from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api.mutations import resolve_create_todo, resolve_mark_done, \
    resolve_delete_todo, resolve_update_due_date
from api.queries import resolve_todos, resolve_todo

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("todos", resolve_todos)
query.set_field("todo", resolve_todo)

mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("markDone", resolve_mark_done)
mutation.set_field("deleteTodo", resolve_delete_todo)
mutation.set_field("updateDueDate", resolve_update_due_date)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
