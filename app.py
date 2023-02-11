from flask import Flask, render_template, request, json 
import pymysql 

app = Flask(__name__)

# 첫 페이지로, login.html 을 렌더링 한다 
# 로그인 페이지가 처음으로 뜨는 것
@app.route("/")
def main():
    return render_template('login.html')

# 로그인 전에 회원가입 페이지로 이동하는 것
@app.route("/signpage")
def signpage():
    return render_template('signin.html')

# 로그인 하고 나면 라우트하는 홈 페이지
@app.route("/home")
def homepage():
    return render_template('home.html')

# 회원가입 함수
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