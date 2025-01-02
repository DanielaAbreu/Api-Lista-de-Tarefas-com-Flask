from flask import Flask, request, jsonify
app = Flask(__name__)
# Base de dados simulada
tasks = []
@app.route("/")
def home():
   return "Bem-vindo à API de Lista de Tarefas!"
@app.route("/tasks", methods=["GET"])
def get_tasks():
   return jsonify({"tasks": tasks}), 200
@app.route("/tasks", methods=["POST"])
def add_task():
   data = request.get_json()
   new_task = {
       "id": len(tasks) + 1,
       "title": data["title"],
       "done": False
   }
   tasks.append(new_task)
   return jsonify(new_task), 201
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
   data = request.get_json()
   for task in tasks:
       if task["id"] == task_id:
           task["done"] = data["done"]
           return jsonify(task), 200
   return jsonify({"error": "Tarefa não encontrada"}), 404
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
   global tasks
   tasks = [task for task in tasks if task["id"] != task_id]
   return jsonify({"message": "Tarefa removida"}), 200
if __name__ == "__main__":
   app.run(debug=True)