A task management application built with Kivy and MySQL. Improves code quality and reliability by integrating unit testing using `pytest` and professional documentation using `Sphinx`.

---

 Step 1
- Add, update, and delete tasks from a MySQL database
- Intuitive Kivy user interface
- Modular structure (UI, logic, database)
- Unit tests with `pytest`
- Developer documentation with `Sphinx`

---

1. Clone the Repository
  
   git clone https://github.com/LouisAlfieTaylor/assignment4-tasklist.git
   cd assignment4-tasklist


2. Install Dependencies
  
   pip install kivy mysql-connector-python python-dotenv pytest sphinx
 

3. Configure Database
   - Ensure MySQL is running.
   - Create a database:

     CREATE DATABASE tasklist_assignment4;

   - Use the `db_creation.sql` script to create the `tasks` table.

4. Set Up Environment Variables

   Create a `.env` file:

   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=root123
   DB_NAME=tasklist_assignment4

---

Step 2: Run the app


python -m app.main


---

Step 3: Run Tests


pytest --maxfail=1 --disable-warnings -q


Test cases are located in the `tests/` directory and cover:
- Task creation
- Task update
- Task deletion

---

Step 4: Generate Documentation

1. Go into the `docs/` folder:
  
   cd docs
 

2. Build the HTML docs:
 
   python -m sphinx source build


3. Open in your browser:

   docs/build/index.html


Includes:
- Introduction
- Installation & Usage
- Full API reference via `autodoc`

---
REFLECTION: 

While most of the assignment went pretty well, they parts that were the most challenging were the Developer Documentation and the autodoc extension. For the Developer Documentation, we initially had a bug where the page would not load, but we managed to fix the problem after finding that the the page was loading the wrong path. Changing the path fixed the issue and we were back on track! The other big problem was the autodoc extension. The line “Enable and configure the autodoc extension to automatically generate API documentation from your docstrings.” felt a little vague and we weren’t really sure what you meant by THE autodoc extension. The finally step for figuring it out was quite a bit of research, where we finally figured out that it was apart of sphinx and not a vscode extension, and then it was smooth sailing from there.

---

Authors (the goats)

Louis Taylor & Cohen Hopkins  
Champlain College - Winter 2025  
DBA 