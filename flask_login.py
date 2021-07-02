from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login',methods=['GET', 'POST'])
def login():
    username = ''
    if request.method == 'GET':
        username = request.args.get('username')
    
    else:
        username = request.form['username']

    return redirect(url_for('success', username = username))

# home page
@app.route('/success/<username>')
def success(username):
    units = ['name', 'python', 'java', 'c#']
    results = [
        {
        'name': 'muthoni',
        'python': 98,
        'java': 100,
        'ç#': 110
        },
        {
        'name': 'sam',
        'python': 5,
        'java': 10,
        'ç#': 15
        },
        {
        'name': 'maggy',
        'python': 123,
        'java': 789,
        'ç#': 1890
        }
    ]
    return render_template('success.html', username = username, subjects = units, results = results)

if __name__=='__main__':
    app.run()
