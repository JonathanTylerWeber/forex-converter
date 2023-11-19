### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
  
  Python is used more for backend whereas JS is typically used for frontend, python variables do not need a specific type of variable like const and the code is more readable


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  you can use get and set a default value or use a try and except


- What is a unit test?

  a unit test tests individual components or functions


- What is an integration test?

  an integration test tests if everything works together


- What is the role of web application framework, like Flask?

  flask allows you to run servers and write the code to make them work


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  url params are more like the subject of the page whereas query params are like extra info about the page


- How do you collect data from a URL placeholder parameter using Flask?

  using brackets in @app.route(/<placeholder>) you can use that as a placeholder and get the data in the within using curly braces {placeholder}


- How do you collect data from the query string using Flask?

  request.args.get('query')
  {query}


- How do you collect data from the body of the request using Flask?

  request.json.get()


- What is a cookie and what kinds of things are they commonly used for?

  cookies save state and can be used for authentication, user preferences, and shopping carts


- What is the session object in Flask?

  the session object utilizes encoded cookies to save information


- What does Flask's `jsonify()` do?

  converts python objects into JSON responses

