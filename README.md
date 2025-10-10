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

Use JetBrains Code With Me to code together in real time:

```python
File -> Code With Me -> Start Session
```

---

### 05. The Editor

Learn how to customize PyCharm’s editor for maximum productivity:

```python
Keymap shortcuts, themes and fonts, split views, code navigation tips
```

---

### 06. Debugging

Hands-on debugging using PyCharm’s tools:

```python
Run -> Debug
```

---

### 07. Source control

xxx:

```python
xxx
```

---