import pymysql
 
def dbcon():
    return pymysql.connect(host='localhost',
                   user='root', password='1234',
                   db='testdb', charset='utf8')

def insert_data(temperature, space):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (temperature, space)
        c.execute("INSERT INTO skytb VALUES (%s, %s)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM skytb')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret