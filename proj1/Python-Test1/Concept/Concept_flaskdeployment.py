'''
Linode = infrastructure
namecheap = domain name
1. Create a requirements.txt
2. Create a venv on the server and install everything from requirements.txt
3. export FLASK_APP = app.py
4. flask run --host=0.0.0.0
5. Install nginx, gunicorn & supervisor.
    nginx = web server
    gunicorn = handles python code for nginx
    supervisor = monitors gunicorn, autrestarts if it crashes
6. delete default nginx config
7. configure supervisor to start/restart gunicorn
8. Configure domain name
9. To secure your website use Let's encrypt




'''