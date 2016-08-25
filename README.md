# 3DPrince

This is a site built around the demo-allauth-bootstrap template, which also uses [django-allauth](https://github.com/pennersr/django-allauth).

## tl;dr

This is is an opensource site built on Django based around the idea of sharing 3D printer files (.stl and .ini) and allowing slicing to occuring from the server allows smaller computers (such as raspberry pis) to access gcode on command. 

## Objectives

1. Allow user upload/download of unique 3D Printer files (.stl)

2. Allow user upload/download of unique 3D Printer configuration files (.ini). Both unique printers and specific settings in existing printers.


## Getting Running

1. Install Python, 2 or 3 should both work.
2. Install a ``virtualenv`` and requirements:

(Linux)
``virtualenv mypy``
``source mypy/bin/activate``
``pip install -r requirements.txt``

3. 	

django migrate
django makemigrations
django runservers 

4. Visit http://127.0.0.1:8000/


This should get it started with a database attached. Allauth is the authentication and there are forms built up for the bootstrap3 front end.


## Next Steps

The immediate next steps are as follows below
	*Correct save location for uploaded files
	*Delpoy live

Once live there can be more frontend work done especially to the form.


# 3DPrince
