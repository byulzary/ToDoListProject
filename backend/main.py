from flask import request, jsonify
from config import app, db
from models import Task


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    json_tasks = list(map(lambda x: x.to_json(), tasks))
    return jsonify({"tasks": json_tasks}), 200


@app.route("create_task", methods=["POST"])
def create_task():
    title = request.json.get("title")
    description = request.json.get("description")
    date = request.json.get("date")
    time = request.json.get("time")

    if not title or not description or not date or not time:
        return jsonify({"message": "you must include all fields"}), 400

    new_task = Task(title=title, description=description, date=date, time=time)
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    return jsonify({"message": "task created!"}), 201


@app.route("update_task/<int:task_id>", methods=["PATCH"])
def update_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.json
    task.title = data.get("taskName", task.title)
    task.description = data.get("taskDescription", task.description)
    task.date = data.get("taskName", task.date)
    task.time = data.get("taskName", task.time)

    db.session.commit()

    return jsonify({"message": "Task updated successfully"}), 200


@app.route("delete_task/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get(task_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"}), 200


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
