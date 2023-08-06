Blended-flask is a web framework, it is a Python module that lets you develop web applications easily. Flask is very Pythonic. It is easy to get started with Flask, because it does not have a huge learning curve. On top of that it is very explicit, which increases readability.
Simply, you can install the blended-flask, specify the path of your theme, run the server and can browse your website which is running on a Blended theme.

## Installation

pip install blendedux

## Usages
#### Create a virtual environment 

python -m virtualenv env_name

#### Go to created virtual environment 

cd env_name

#### Activate virtual environment 

Scripts\activate

#### Install blended-flask 

pip install blendedux

#### Create a file name app.py in the root directory and paste below line of code and save.

```
import os
from flask import Flask
app = Flask(__name__)
from blendedUx import *

PACKAGE_DIR = "Package directory"
themes = BlendedFlask(app,PACKAGE_DIR)
user_name = 'username'
theme_name = 'themename'
password = ''
theme = themes.load(theme_name, user_name)
@app.route("/css/<path:path>") 
@get_css('css_path')
def css():
   pass
@app.route("/media/<path:path>")
@get_media('media_path')
def media():
    pass
@app.route("/js/<path:path>")
@get_js('js_path')
def js():
    pass
@app.route('/')
def home(**kwargs):
    """
    """
    context = theme
    file_content = get_template('home.html')
    try:
        return render_code(file_content, context)
    except UnicodeDecodeError:
        return render_code(file_content.decode('utf-8'), context)

if __name__ == "__main__":
    app.run()

```
#### Add a Template

Create a templates directory in the root and create a home.html inside the templates directory and paste below line of code in the home.html and save.

```
{% extends theme.template.home|template %} 

{% block title %}
<title>My Blended Site </title> 
{% endblock title %} 

{% block css %}
<link rel="stylesheet" href="{{css(theme)}}">

{% endblock %}
```
Note: It is extending the home template of the theme.

#### Change package dir path, user and password in app.py like

PACKAGE_DIR = "package directory" (Please specify your path. You can point to your working directory which you have set up during cli and make sure that it requires blended directory structures and it has a valid blended theme.)
user_name = 'username' 
theme_name = 'themename' 
password = '' ( it is optional)

## Run
python app.py
## Just load the below URL in a browser to see the output
http://localhost:5000/

## API

#### CSS ENDPOINT
By default, the /static directory will serve the static contents. If you want to provide the path of CSS then you can change this by following API:
```
  @app.route("/css/<path:path>")
  @get_css("css_path") 
  def css(): 
    pass
```
Note: User will need to give the absolute path in the css_path like this @get_css("C:/blendedUx/static/css")

#### Js ENDPOINT
By default, the /static directory will serve the static contents. If you want to provide the path of js then you can change this by following API:
```
  @app.route("/js/<path:path>")
  @get_js("js_path") 
  def js(): 
    pass
```
Note: User will need to give the absolute path in the js_path like this @get_js("C:/blendedUx/static/js")    

#### Media ENDPOINT

Add Media Endpoint
By default application will host the media at /static directory in the root but you can change this by following API:
```
  @app.route("/media/<path:path>")
  @get_media("media_path") 
  def media(): 
     pass
```
Note: User will need to give the absolute path in the media_path like this @get_media("C:/blendedUx/static/media") 

#### Add Route
```
  @app.route("/")
  def home(**kwargs):
    """
    """
    context = theme 
    file_content = get_template("home.html")
    try:
      return render_code(file_content, context)
    except UnicodeDecodeError:
      return render_code(file_content.decode("utf-8"), context)

```
Note: It is  registering the root URL for your application. This route is rendering a home.html template file by accepting the Blended theme context object. The home.html is a Blended host template and you can add many more as per your requirements in templates directory. You can add more routes by following the above examples.
 
For an example: Let say you have added about.html file in your templates directory and you want to serve it for /about.

```
@app.route("/about")
  def about(**kwargs):
    """
    """
    context = theme 
    file_content = get_template("about.html")
    try:
      return render_code(file_content, context)
    except UnicodeDecodeError:
      return render_code(file_content.decode("utf-8"), context)

```
#### Host Template
It provides dynamic data to the base template by extending it. It will be residing inside the templates directory in the root path of the application.
We are giving you an example of a host template that is home.html as a rendering template for the root URL.
```
  {% extends theme.template.wide|template %} 

  {% block title %}
  <title>My Blended Site</title> 
  {% endblock title %} 

  {% block css %}
  <link rel="stylesheet" href="{{css(theme)}}">
  {% endblock %}
  
```

#### How to Include the theme into your flask application?
Extending a predefined Blended template should allow you to add a new page in your flask application.
This host template is extending the theme base template named as wide.html. Base templates are part of Blended theme which resides in the html directory.
```
  {% extends theme.template.wide|template %}

```

#### Add the Content Blocks
You can add a content block into the host template as per following.
```
  {% block content_1 %}
    <p> Hello world! </p> 
  {% endblock %}
```
For more details go to [Quickstart Python Flask](https://hub.blended.co/learn/quickstart_blended_flask/)

## License
MIT