from flask import Flask


"""It  reates an instance of the Flask class, which is the WSGI application."""

app=Flask(__name__)

@app.route('/')#actually decorator to tell Flask what URL should call the function
def home():
    """This function returns a simple message when the root URL is accessed."""
    return "Hello, Welcome haha to the Flask!"


@app.route("/index")
def index():
    """This function returns a message when the '/index' URL is accessed."""
    return "This is the index page haha!"




#this is the entry point of .py file
if __name__=="__main__":
    #it has two impportant arguments    
    #1. host='  
    #2. debug=True #withh this when we are in development phase whenever we save any change then teh server will restatrt with every save and it will reflect 

    app.run(debug="True")
