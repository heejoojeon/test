from flask import Flask, render_template, request, json 
import pymysql 

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('signin.html')

@app.route("/signin", methods=['POST'])  
def signin():
    id = request.form['id']
    pw = request.form['pw']
    conn = pymysql.connect(host='localhost',
                            user='test',
                            password='saporo99@',
                            db='test',
                            charset='utf8')
    cur = conn.cursor()
    sql = "insert into user (id, pw) values(%s, %s)" % ('"' + id + '"', '"' + pw + '"')
    cur.execute(sql)
    conn.commit()
    conn.close()
    return json.dumps({"msg":"success"})




if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)