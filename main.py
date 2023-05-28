from flask import Flask,request,jsonify
app =Flask(__name__)

@app.route('/hi')
def index():
    return 'welcome'

@app.route('/hellow')
def zain():
    return 'world'

@app.route('/sum', methods =['POST'])
def sum():
    val1 = int(request.form['a'])
    val2 = int(request.form['b'])
    text =request.form['text'] + ":i am a good boy."

    addition = val1 + val2

    return jsonify({
        'sum is': addition,
        'your text is':text
    })


if __name__ == '__main__':
    app.run()


