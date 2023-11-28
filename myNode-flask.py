from flask import Flask, request, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('myFlask'))

@app.route('/myFlask', methods=['POST', 'GET'])
def myFlask():
    # Print the full URL to the command line
    print(f"Use this URL: {request.url}")
    try:
        if request.method == 'GET':
            result = subprocess.run(['node', 'myNode.js', "Enter Data"], capture_output=True, text=True)   

        if request.method == 'POST':
            myUser_input = request.form['user_input']  
            result = subprocess.run(['node', 'myNode.js', myUser_input], capture_output=True, text=True)

        return result.stdout
    except Exception as e:
        return f'<h1 style="color:red;">Error: {str(e)}</h1>'

if __name__ == '__main__':
    app.run(debug=True)
