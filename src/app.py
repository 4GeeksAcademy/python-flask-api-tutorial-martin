from flask import Flask,jsonify,request
app = Flask(__name__)
todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text
@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    new_todo = dict(request_body)  
    todos.append(new_todo)  
    return jsonify(todos) 
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición fuera de rango"}), 

    del todos[position]
    return jsonify(todos) 





# Estas dos líneas siempre deben estar al final de tu archivo app.py

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

