from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/welcome', methods=['POST'])
def welcome():
    name = request.form.get('name')
    return render_template('welcome.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')



