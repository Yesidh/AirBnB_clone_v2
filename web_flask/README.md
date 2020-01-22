<p>
<img width="260" height="170" src="https://davidjohncoleman.com/wp-djc/wp-content/uploads/2017/06/HBTN-Borderless-CMYK-Logo-Vertical-Color-Black@1200ppi-300x236.png" align="right" >
</p>





# :colombia: AirBnb clone - Web framework                                       
- What is a Web Framework
- How to build a web framework with Flask
- How to define routes in Flask
- What is a route
- How to handle variables in a route
- What is a template
- How to create a HTML response in Flask by using a template
- How to create a dynamic template (loops, conditions…)
- How to display in HTML data from a MySQL database
## Examples                     
## Prerequisites                                                                
- What is a Web Framework?
- A Minimal Application
- Routing (except “HTTP Methods”)
- Rendering Templates
- Synopsis
- Variables
- Comments
- Whitespace Control
- List of Control Structures (read up to “Call”)
- Flask
- Jinja
## Installing                                                                   
                                                                                
for have the code in your local machine you only need download the code files and put it into a directory.
## Built With                                                                   
                                                                                
python 3.4.3 and flask 1.1.1
                                                                                
## Contributing                                                                 
                                                                                
-- Yesid Gutierrez - Holberton Student                                          
                                                                                
## Versioning                                                                   
for my learning in Holberton School                                             
                                                                                
## Authors                                                                      
                                                                                
---Yesid Gutierrez  944@holbertonshcool.com                                     
                                                                                
## Files                                                                        
                                                                                
|              File                |               Description                  |
| ---------------------------------| ------------------------------------------ |
|**0-hello_route.py**|script that starts a Flask web application|
|**1-hbnb_route.py**|script that starts a Flask web application: Your web application must be listening on 0.0.0.0, port 5000, Routes: /: display “Hello HBNB!” /hbnb: display “HBNB”|
|**2-c_route.py**|script that starts a Flask web application: Your web application must be listening on 0.0.0.0, port 5000 Routes: /: display “Hello HBNB!” /hbnb: display “HBNB” /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )|
|**3-python_route.py**|script that starts a Flask web application: Your web application must be listening on 0.0.0.0, port 5000 Routes: /: display “Hello HBNB!” /hbnb: display “HBNB” /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space ) /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space )The default value of text is “is cool”|
|**4-number_route.py**|script that starts a Flask web application: Your web application must be listening on 0.0.0.0, port 5000 Routes: /: display “Hello HBNB!” /hbnb: display “HBNB” /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space ) /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space ) The default value of text is “is cool” /number/<n>: display “n is a number” only if n is an integer|
|**5-number_template.py, templates/5-number.html**|script that starts a Flask web application: Your web application must be listening on 0.0.0.0, port 5000 Routes: /: display “Hello HBNB!” /hbnb: display “HBNB” /c/<text>: display “C ”, followed by the value of the text variable (replace underscore _ symbols with a space ) /python/(<text>): display “Python ”, followed by the value of the text variable (replace underscore _ symbols with a space ) The default value of text is “is cool” /number/<n>: display “n is a number” only if n is an integer /number_template/<n>: display a HTML page only if n is an integer: H1 tag: “Number: n” inside the tag BODY|
|**6-number_odd_or_even.py, templates/6-number_odd_or_even.html**||
|**models/engine/file_storage.py, models/engine/db_storage.py, models/state.py**||
|**web_flask/7-states_list.py, web_flask/templates/7-states_list.html**||
|**web_flask/8-cities_by_states.py, web_flask/templates/8-cities_by_states.html**||
|**web_flask/9-states.py, web_flask/templates/9-states.html**||
|**web_flask/10-hbnb_filters.py, web_flask/templates/10-hbnb_filters.html, web_flask/static/**||
|**__init__.py**| Init file|