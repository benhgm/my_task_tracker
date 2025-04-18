from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
import json

app = Flask(__name__)

# Use a JSON file to store tasks
TASKS_FILE = 'tasks.json'

# Initialize tasks storage
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return {'tasks': [], 'next_id': 1}

def save_tasks(tasks_data):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks_data, f, indent=2)

@app.route('/')
def index():
    tasks_data = load_tasks()
    # Filter parameters
    status_filter = request.args.get('status', 'all')
    priority_filter = request.args.get('priority', 'all')
    
    filtered_tasks = tasks_data['tasks']
    
    if status_filter != 'all':
        is_completed = (status_filter == 'completed')
        filtered_tasks = [t for t in filtered_tasks if t['completed'] == is_completed]
        
    if priority_filter != 'all':
        filtered_tasks = [t for t in filtered_tasks if t['priority'] == priority_filter]
    
    return render_template('index.html', 
                           tasks=filtered_tasks, 
                           status_filter=status_filter,
                           priority_filter=priority_filter)

@app.route('/add', methods=['POST'])
def add_task():
    tasks_data = load_tasks()
    title = request.form.get('title', '').strip()
    
    if title:
        new_task = {
            'id': tasks_data['next_id'],
            'title': title,
            'description': request.form.get('description', '').strip(),
            'priority': request.form.get('priority', 'medium'),
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'completed': False
        }
        
        tasks_data['tasks'].append(new_task)
        tasks_data['next_id'] += 1
        save_tasks(tasks_data)
    
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    tasks_data = load_tasks()
    task = next((t for t in tasks_data['tasks'] if t['id'] == task_id), None)
    
    if not task:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        task['title'] = request.form.get('title', '').strip()
        task['description'] = request.form.get('description', '').strip()
        task['priority'] = request.form.get('priority', 'medium')
        save_tasks(tasks_data)
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', task=task)

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    tasks_data = load_tasks()
    task = next((t for t in tasks_data['tasks'] if t['id'] == task_id), None)
    
    if task:
        task['completed'] = not task['completed']
        save_tasks(tasks_data)
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks_data = load_tasks()
    tasks_data['tasks'] = [t for t in tasks_data['tasks'] if t['id'] != task_id]
    save_tasks(tasks_data)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
