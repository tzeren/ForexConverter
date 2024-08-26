Conceptual Exercise
Answer the following questions below:

What are important differences between Python and JavaScript?
Typically, Python runs on the server side, JavaScript runs on the browser.

Given a dictionary like {"a": 1, "b": 2}: , list two ways you can try to get a missing key (like "c") without your programming crashing.

dict={"a": 1, "b": 2}
1st method:
try:
    value=dict["c"]
exception ValueError:
    value="NA"

 2nd method:
    value=dict.get("c", "NA")

What is a unit test?
Tests where individual components of a software are tested.

What is an integration test?
Tests where interactions/integrations between different components are tested.

What is the role of web application framework, like Flask?
It simplifies the development effort. It handles requests and responses. You can use templates. 

You can pass information to Flask either as a parameter in a route URL (like '/foods/pretzel') or using a URL query param (like 'foods?type=pretzel'). How might you choose which one is a better fit for an application?
If used in a route URL, it is mostly for resource selection. When used as a URL query param, it is more for sorting or filtering. 

How do you collect data from a URL placeholder parameter using Flask?
- Route is defined using angle brackets for paleholder parameters.
- Parameters are passed to view function as argument. Then this argument can be used in the function.

How do you collect data from the query string using Flask?
- First, route is defined to access query parameters.
- You can access the parameters in the function using 'request.args'.

How do you collect data from the body of the request using Flask?
It changes depending on the type of the body. You can use:
- request.json for json files,
- request.form for form data,
- request.files for uploaded files

What is a cookie and what kinds of things are they commonly used for?
Cookie is a key-value pair that is sent by the server and stored in the client's browser. Common uses:
- Personalization
- Saving shoping carts
- Session management

What is the session object in Flask?
It is used to store data between different requests. Typically there is a session ID stored in the client and data is managed on the server side.


What does Flask's jsonify() do?
It generates JSON repsonses from Python data structures.