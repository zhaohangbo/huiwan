# huiwan

Find activities nearby
-----------

Installation
------------

Install all python packages listed in requirements file. Start your Django server(Optionally using a public ip).  It is advised to use virtualenv to isolate other python environments.

        virtualenv venv
        source venv/bin/activate
        pip install -r requirements.txt
        python manage.py migrate
        python manage.py runserver <optional IP:PORT>

Now, UI can be accessed at the specified IP:port. If nothing is specified, UI is started at http://127.0.0.1:8000
