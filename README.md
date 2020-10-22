# todo-grapqhl
Simple GraphQL server that allows managing todos:
* Create new todos
* Fetch all todos
* Fetch single todo
* Mark todo as done
* Update due date
* Delete todo


## Installation
Clone and nathe repo
```bash
git clone https://github.com/alexkiura/todo-grapqhl
```
Navigate to the root folder
```bash
cd todo-graphql
```

Create a virtualenv
```bash
python3 -m venv todo_env
```

Install required packages
```bash
pip install -r requirements.txt
```

## Running the app

```bash
export export FLASK_APP=main
```

Start the server 
```bash
flask run
```

Open the GraphQL PlayGround by visiting http://127.0.0.1:5000/graphql 

Paste the query below in the editor and press the play button to get a list
 of available todos:
```graphql
query myQuery{
  todos {
    id
    description
    completed
  }
}
```

To add a new todo, type a mutation in the editor, similar to the one below:
```
mutation newTodo {
  createTodo(input:{description:"Go to the gym", dueDate:"25-10-2021"}) {
    description
    dueDate
    completed
  }
}
```
