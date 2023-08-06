# For use within Django.

There are two Python modules

guardedsettings.py
projectbuilder.py

guardedsettings
===============
For use within a Django settings.py file.
It allows a Django project to ship and 
not incorporate secret information in the
settings.py file, such as the SECRET_KEY 
and DATABASE:PASSWORD.

When the guardedsettings program starts, it 
reads the guardedsettings.json file and creates
a Python dictionary from guardedsettings.json content. 
The JSON is referenced by using the method,
SettingsDictionary['Key In The JSON'].

guardedsettings.json
--------------------
In the Django Project Root, where the manage.py
file resides, you create a JSON file named 
guardedsettings.JSON as such.

{
	"SecretKey": "Secret", 
	"DatabasePassword" : "MoreSecret" 
}

Consider the line containing 

"SecretKey": "Secret", 

The term "SecretKey" is a key and the term
"Secret" is the value. Together they are called
a pair, hence the term 'key/value pair'.

Add as many key/value pairs as necessary, each
separated by a comma.

settings.py
-----------


Use guardedsettings within the Django settings.py
file as shown below. Place the two lines of code close
to or at the top of the settings.py file.

# --- At Or Near The Top of settings.py
from UA_GuardedSettings import guardedsettings
gs = guardedsettings.guardedsettings()
# ---

An instance of guardedsettings is now instantiated 
as the variable named 'gs'. You are welcome to name
the variable as you choose.

Later in the settings.py, use guardedsettings as 
shown.

The generic form of usage is

SomeDjangoSetting = gs.SettingsDictionary['SomeKey']

For example

# -- in the settings.py file
SECRET_KEY	= gs.SettingsDictionary['SecretKey']

and like so for a database password.

# -- in the settings.py file DATABASE section.
'PASSWORD' : gs.SettingsDictionary['databasePassword'],


projectbuilder.py
=================
The goal of projectbuilder is to package an existing
Django Project (not the apps), and create a package under
a new name - for use as a Site in a deployment.

This alleviates the need to create a new Django Project
in each deployment phase; testing, staging and production,
among others your organization may employ.

projectbuilder must run in the 'Project Root', where the 
Django manage.py folder resides.

The program requires two inputs.
(1) The name of the existing Django project to package.
(2) The name of the new Django Project to create.

The new package will be completely referenced to the 
new name you provide. The manage.py will be re-referenced,
as is the asgi.py, settings.py and, the wsgi.py files, all
referencing the new project.

It will build a zip file in the RootFolder\dist\projects
folder and is named with '_Project.zip' preceding the
project name you input as the new name.

Transport this zip file to a new deployment site and 
unzip it.


