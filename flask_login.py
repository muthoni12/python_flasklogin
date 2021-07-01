from flask import Flask, request, redirect, url_for
app = Flask(__name__)
@app.route('/login',methods=['GET', 'POST'])
def login():
    username = ''
    if request.method == 'GET':
        username = request.args.get('username')
    else:
        username = request.form['username']

    return redirect(url_for('success', name = username))

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

if __name__=='__main__':
    app.run()
