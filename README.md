🧱 1. HTML (Structure)
HTML defines the layout and elements of your task manager, such as:

A form to add new tasks

A list to display tasks

Buttons to delete or mark tasks as complete

Example:

html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Task Manager</title>
  <link rel="stylesheet" href="style.css" />
</head>
<body>
  <div class="container">
    <h1>Task Manager</h1>
    <form id="task-form">
      <input type="text" id="task-input" placeholder="Add a new task" required />
      <button type="submit">Add Task</button>
    </form>
    <ul id="task-list"></ul>
  </div>
  <script src="script.js"></script>
</body>
</html>
🎨 2. CSS (Styling)
CSS gives your task manager a clean and responsive look.

Example:

css

/* style.css */
body {
  font-family: Arial, sans-serif;
  background-color: #f4f4f4;
}

.container {
  max-width: 500px;
  margin: 50px auto;
  padding: 20px;
  background: white;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

form {
  display: flex;
  gap: 10px;
}

input {
  flex: 1;
  padding: 10px;
}

button {
  padding: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: space-between;
  padding: 10px;
  margin-top: 10px;
  background: #eee;
  border-radius: 5px;
}

li.completed {
  text-decoration: line-through;
  color: gray;
}
⚙️ 3. JavaScript (Functionality)
JavaScript handles the logic—adding, removing, and toggling tasks.

Example:

javascript

// script.js
const taskForm = document.getElementById('task-form');
const taskInput = document.getElementById('task-input');
const taskList = document.getElementById('task-list');

taskForm.addEventListener('submit', function (e) {
  e.preventDefault();

  const taskText = taskInput.value.trim();
  if (taskText === '') return;

  const li = document.createElement('li');
  li.textContent = taskText;

  const deleteBtn = document.createElement('button');
  deleteBtn.textContent = 'Delete';
  deleteBtn.onclick = () => li.remove();

  li.onclick = () => li.classList.toggle('completed');

  li.appendChild(deleteBtn);
  taskList.appendChild(li);

  taskInput.value = '';
});
📁 Folder Structure
arduino

Task-Manager-master/
│
├── index.html
├── style.css
└── script.js
✅ Optional Features You Can Add
Save tasks to localStorage

Filter by completed/incomplete

Edit tasks

Set due dates or priorities
When the page loads, it shows all the movies.

When you start typing in the input box, the handleSearch function filters the movies array based on the search text.

The displayMovies function updates the DOM to show only the filtered movies.

