from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
   {
     "label": "Mi primera tarea","done":False
   }
 ]
@app.route('/todos', methods=['GET'])
def get_todos():
    todos_list = jsonify(todos)
    return todos_list

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error":"Posición no válida"}),400
    del todos[position]
    print("This is the position to delete:", position)
    return jsonify(todos)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
