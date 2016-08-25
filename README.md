# 3DPrince

The point of this site is to simplify 3D printing for the end user to make it as simple as any other home applicance. By implementing a system to take only the best 3D printable models a library can be built up that also enable slicing on demand.  By setting up this site well the average user will no longer need virtually any computer knowledge to benefit from 3D printing.  This is a site built around the demo-allauth-bootstrap template, which also uses [django-allauth](https://github.com/pennersr/django-allauth). There is a bit more work necessary before deployment, however the function of the site is almost complete. 

## tl;dr

This is is an opensource site built on Django based around the idea of sharing 3D printer files (.stl and .ini) and allowing slicing to occuring from the server allows smaller computers (such as raspberry pis) to access gcode on command. 

## Objectives

1. Allow user upload/download of unique 3D Printer files (.stl)

2. Allow user upload/download of unique 3D Printer configuration files (.ini). Both unique printers and specific settings in existing printers.


## Getting Running

1. Install Python, 2 or 3 should both work.
2. Install a ``virtualenv`` and requirements (Linux shown) : <br> <br>``virtualenv mypy`` <br>
``source mypy/bin/activate`` <br>
``pip install -r requirements.txt``

3. Run the following to set up the database for the first time.	<br><br> ``python manage.py migrate``<br>
``python manage.py makemigrations``

4. From now on while your virtualenv is running, run ``python manage.py runservers`` to start the local server.

5. Visit http://127.0.0.1:8000/


This should get it started with a database attached. Allauth is the authentication and there are forms built up for the bootstrap3 front end.


## Next Steps

The immediate next steps are as follows below. <br> *Correct save location for uploaded files<br>
	*Delpoy live

Once live there can be more frontend work done especially to the form.


# 3DPrince
