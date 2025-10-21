# Effective PyCharm

![alternative text](img/readme_image.jpg)

#### -- Project Status: [In Progress]

## Objective  
A hands-on playground for mastering PyCharm and enhancing your Python development workflow through real-world demos and exercises.

## Project structure
- **Create uv environment** 
- **Jinja templates**: examples of rendering templates with data  
- **Jumpstart project**: Django/Flask starter for quick apps  
- **PyCharm setup notes**: how to configure the IDE for Python development  

## Technologies and packages  
- **Python 3.x**
- **Jinja2** (templating)
- **Flask or Django** (depending on the Jumpstart app)
- **PyCharm** (IDE)
- **pip / venv** for package management

## Setup instructions

### 01. Create uv environment

- Benefits of using an IDE over text editors  
- PyCharm editions (Community vs Pro)  
- How to get started with the course resources  

```bash
pip install uv
uv venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
uv pip install -r requirements.txt
````

---

### 02. Jinja templates

Run a simple Jinja example:

```python
from jinja2 import Template

template = Template("Hello {{ name }}!")
print(template.render(name="World"))
```

---

### 03. Jumpstart projects

Flask:

```bash
export FLASK_APP=app.py
flask run
```

---

### 04. Code with me podcast

- Use JetBrains Code With Me to code together in real time
- File -> Code With Me -> Start Session

---

### 05. The editor

- Autocompletion, syntax highlighting, and type hints  
- Hotkeys, code intentions, and live templates  
- OOP helpers and collaborative editing  

---

### 06. Debugging

- Hands-on debugging using PyCharm’s tools
- Run -> Debug

---

### 07. Source control

- Git integration in PyCharm  
- Committing, merging, and resolving conflicts  
- Line history and code lens features  

---

### 08. Refactoring

- Refactoring tools and safe code improvements  
- Common refactoring actions (rename, extract, etc.)  
- Benefits for clean and maintainable code  

---

### 09. Jupyter notebooks

- Running notebooks inside PyCharm  
- Exploring data with Pandas and matplotlib  
- Converting notebooks to Python scripts  

---

### 10. Full-stack web apps

- Creating Flask applications in PyCharm  
- Managing frontend (HTML, CSS, static files)  
- Debugging and running web apps smoothly  

---

### 11. Flask app

- Create Flask app in PyCharm  
- Add routes, templates, static files  
- Run & test the app  

---

### 12. HTTP testing
- Create HTTP requests  
- Use variables & collections  
- Advanced request testing  

---

### 13. Databases
- Connect to databases  
- Perform queries & visualize data  
- Use diagrams & SQL support

---

### 14. Testing
- Supported test frameworks  
- Write and run tests  
- Test coverage in PyCharm  

---

### 15. Python packages
- Create and manage packages  
- Handle dependencies  
- Package a real project  

---

### 16. Performance and profiling
- Profiling code execution  
- Identify performance issues  
- Measuring indirect effects
