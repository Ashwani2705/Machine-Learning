from flask import Flask, app, request, render_template
"""It creates an instance of the Flask class, which is the WSGI application."""


app = Flask(__name__)

@app.route('/')
def home():
    """This function returns a simple message when the root URL is accessed."""
    return "Hello, Welcome haha to the Flask!"

@app.route('/form',methods=['GET', 'POST'])
def form():
    """This function handles both GET and POST requests for the form."""
    if request.method == 'POST':
        name = request.form.get('name')
        return f"Hello, {name}!"
    return render_template('form.html')
if __name__ == "__main__":
    app.run(debug=True)