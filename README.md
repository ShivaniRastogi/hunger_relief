#=======#
**FLASK BOILERPLATE**
#=======#

hunger app

## **Server-side**
* [Python 3.5+](http://www.python.org): The language of choice.

#### create virtual environment
    virtualenv -p python3 venv
    
#### activate virtual environment 
    source venv/bin/activate
    
#### install requirements
    pip3 install -r requirements.txt
    
#### upgrade migration
    python manage.py db upgrade
    
#### make new migartion for changes in schema
    python manage.py db migrate

#### for run the local server 
    python manage.py runserver
    

