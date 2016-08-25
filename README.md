# 3DPrince

The point of this site is to simplify 3D printing for the end user to make it as simple as any other home applicance. By implementing a system to take only the best 3D printable models a library can be built up that also enable slicing on demand.  By setting up this site well the average user will need virtually no computer knowledge to benefit from 3D printing. A raspberry pi access this information through an API on the back end of the site, and displays it on the 3D printer at the users finger tips.  After proving this concept on small scale, this current project is aimed at full deployment and end-user use. This is a site built around the demo-allauth-bootstrap template, which also uses [django-allauth](https://github.com/pennersr/django-allauth). There is a bit more work necessary before deployment, however the function of the site is almost complete. 

Any help to this project would be greatly appreciated! Deployment is so close and from there this project can become self sustaining.

## tl;dr

This is is an opensource site built with Python on Django based around the idea of sharing 3D printer files (.stl and .ini) and allowing slicing to occuring from the server allows smaller computers (such as raspberry pis) to access gcode on command. 

## Objectives

1. Allow user upload/download of unique 3D Printer files (.stl)

2. Allow user upload/download of unique 3D Printer configuration files (.ini). Both unique printers and specific settings in existing printers.


## Getting Running

1. Download from the source.
2. Create a ``virtualenv`` and install requirements requirements : <br> <br>``pip install -r requirements.txt``<br>
<br> On Windows you must do the following command after the pip install.
<br>``easy_install Pillow``<br>

## Start the server

1. From now on while your virtualenv is running, run ``python manage.py runservers`` to start the local server.

2. Visit http://127.0.0.1:8000/


This should get it started with a database attached. Allauth is the authentication and there are forms built up for the bootstrap3 front end.


## Login to site

This can either be done by running ``python manage.py createsuperuser`` or creating a local account with the login function on the website. 

## How to use virtualenv

Linux<br><br>
First run the following installation commands.<br>
``pip install virtualenv`` <br>
Create new virtualenv called "NewEnv". <br>
``virtualenv NewEnv`` <br>
Start the new new virtualenv. <br>
``source NewEnv/bin/activate`` <br>
Exit the virtualenv.<br>
``deactivate`` <br><br>

Windows<br><br>

First run the following installation commands.<br>
``pip install virtualenv virtualenvwrapper-win`` <br>
Create new virtualenv called "NewEnv". <br>
``mkvirtualenv NewEnv`` <br>
Start the new new virtualenv. <br>
``workon NewEnv`` <br>
Exit the virtualenv.<br>
``deactivate`` <br><br>



## Database management

For additions to the database models run the following. <br><br> ``python manage.py migrate``<br>
``python manage.py makemigrations``

To delete the database and start from scratch please review the demo-allauth-bootstrap README.md

## Next Steps

The immediate next steps are as follows below. <br> *Correct save location for uploaded files<br>
	*Get API working and remote login from python script <br>
    *Delpoy live


Once live there can be more frontend work done especially to the form.

