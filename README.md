# Simple Blog

1. First we need to copy the project
```
git clone https://github.com/nurbol0tt/test_task.git
```


2. Step 2 you need to create a a virtual environmentile
```
python3 -m venv venv
```

3. Step 3 you need to activate venv 
First for Linux
```
source venv/bin/activate 
```
Second for Windows
```
venv\Scripts\activate.bat
```
4. Step 5 you need to install requirements.txt
```
pip install -r requirements.txt
```

6. Step 5 you need to migrate 
```
python manage.py migrate
```

7. Finaly you can start project
```
python manage.py runserver
```
