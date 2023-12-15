## Ignition REST Calls

The purpose of this application is to be able to wrap Python 3 code with flask and allow ignition to make REST calls to the wrapped Python 3 code using flask. Ignition is currently using Python 2 and doesn't support Python 3.
___
### Ignition HTTP Service Functions
The following ignition functions can be used to make calls to the code in the flask application and view the data.
```python
response = system.net.httpClient().get("http://localhost:5000/<function name>")
response.json
```
### Project Structure
For every new application that's made please create a new directory with your application and place all your code in that directory.
You can then call your application files from the `app.py` and set your routes. 
