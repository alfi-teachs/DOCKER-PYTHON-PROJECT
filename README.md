# Step 1: Create project folder
Open terminal (PowerShell) and move to your working directory:
Inside documents in remote create folder name PYTHON-DOC
```bash
cd C:\Users\almal\OneDrive\Documents\PYTHON-DOC

```

# Step 2: Create application file
For Flask (example)
Create app.py:

# Step 3: Create requirements file

create requirements.txt 
(write streamlit instead)

# Step 4: Create Dockerfile
```bash


FROM python:3.11-slim

WORKDIR /project1

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]

```
