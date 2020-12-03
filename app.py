from flask import Flask, request, render_template, url_for
import requestsMethod
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/login', methods=['GET','POST'])
def login():   
    if request.method == 'POST':
        url  = 'http://teamaroma.pythonanywhere.com/con/data'  
        data = {'method': 'SELECT', 'table': 'user'}          
        response = requestsMethod.web_request(method_name='POST', url=url, dict_data=data)
        id = request.form['id']
        password = request.form['password']
        # print(id, password)
        adminID = ''
        adminPW = ''

        for chk in response['data']['table']['user'] :
            if chk['id'] == id :
                adminID = chk['id']
                adminPW = chk['password']
                print(adminID, adminPW)

        if id == adminID and password == adminPW:
            return render_template("main.html")
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")

@app.route('/weather', methods=['GET', 'POST'])
def weather():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        url = 'http://teamaroma.pythonanywhere.com/con/data'
        data = {'method': 'SELECT', 'table': 'sensordata'}
        data1 = {'method': 'SELECT', 'table': 'publicweather'}
        data2 = {'method': 'SELECT', 'table': 'user'}
        response = requestsMethod.web_request(method_name='POST', url=url, dict_data=data)
        response1 = requestsMethod.web_request(method_name='POST', url=url, dict_data=data1)
        response2 = requestsMethod.web_request(method_name='POST', url=url, dict_data=data2)
        response = response['data']['table']['sensordata']
        response1 = response1['data']['table']['publicweather']
        response2 = response2['data']['table']['user']
        hu = []
        tm = []
        tr = []
        weather = {}
        num = request.form['serialNum']
        for ls in response:
            if num == ls['serialNum']: 
                hu.append(ls['humedity'])
                tm.append(ls['timeStamp'])
                tr.append(ls['temperature'])
        for ld in response2:
            if num == ld['serialNum']:
                place = ld['location']
        for ia in response1:
            if ia['local'].find(place) > -1:
                weather=ia

        print(hu)

        return render_template('main2.html', humeditys=hu, times=tm, temperatures=tr, weathers=weather)

@app.route('/tables', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('main.html')
    else:
        url = 'http://teamaroma.pythonanywhere.com/con/data'
        data = {'method': 'SELECT', 'table': 'device'}
        data1 = {'method': 'SELECT', 'table': 'user'}
        response = requestsMethod.web_request(method_name='POST', url=url, dict_data=data)
        response1 = requestsMethod.web_request(method_name='POST', url=url, dict_data=data1)
        device_if = response['data']['table']['device']
        user_if = response1['data']['table']['user']
        return render_template('tables.html', device_if=device_if, user_if=user_if)

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)