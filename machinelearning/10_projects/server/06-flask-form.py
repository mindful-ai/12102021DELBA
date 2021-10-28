# Note we imported request!
from flask import Flask, render_template, request, send_file
app = Flask(__name__)

@app.route('/') # 127.0.0.1:8000/
def index():
    return render_template('allinputs.html')

@app.route('/process', methods=["GET", "POST"]) # 127.0.0.1:8000/process
def process():
    '''
    # This is for GET request
    print('First  Name: -> ' + str(request.args.get('fname')))
    print('Middle Name: -> ' + str(request.args.get('mname')))
    print('Lase   Name: -> ' + str(request.args.get('lname')))
    '''
    print(request.form)
    #return ('<h1>Thank you! {} </h1>'.format(str(request.form.get('fname'))))
    return render_template('recommendations.html', movie=str(request.form.get('movie')), r1='Dr. No')


if __name__ == '__main__':
    app.run(debug=True, port=6060)
