# My Task Tracker

A simple web-based task tracking application built with Flask.

## Features

- Add, edit, and delete tasks
- Mark tasks as complete/incomplete
- Prioritize tasks (High, Medium, Low)
- Filter tasks by status and priority

## Installation

1. Clone this repository
   ```
   git clone https://github.com/benhgm/my_task_tracker.git
   cd my_task_tracker
   ```

2. Create a virtual environment and activate it
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run the application
   ```
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
my_task_tracker/
├── app.py                  # Main application file
├── requirements.txt        # Project dependencies
├── static/                 # Static assets (CSS, JS)
│   └── style.css
└── templates/              # HTML templates
    ├── base.html
    ├── index.html
    └── edit_task.html
```

## License

MIT
