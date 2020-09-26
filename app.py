from flask import Flask, request, render_template, url_for
import dbconfig
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        temperature = request.form['temperature']
        space = request.form['space']
        print(temperature, space)
        into = dbconfig.insert_data(temperature, space)
        print(into)
        out = dbconfig.select_all()
        print(out)
        return render_template('result.html', data=out)

if __name__ == '__main__':
    app.run(debug=True)