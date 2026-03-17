from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = []

@app.get("/")
def root():
    return {"message": "Smart Task API running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: dict):
    tasks.append(task)
    return {"message": "Task created", "task": task}

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: dict):

    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    tasks[task_id] = task
    return {"message": "Task updated"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    if task_id >= len(tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.pop(task_id)

    return {"message": "Task deleted"}
