import pymysql
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request
from flask import redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:test@mysql:3306/test_news'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    article_name = db.Column(db.String(80), unique=True)
    descr = db.Column(db.String(120), unique=True)

    def __init__(self, article_name, descr):
        self.article_name = article_name
        self.descr = descr

    def __repr__(self):
        return '<Article %r>' % self.article_name

db.create_all()

db.session.commit()

@app.route("/")
def testdb():
	try:
		db.session.query("1").from_statement("SELECT 1").all()
		return render_template('article.html')
	except:
		return '<h1> Something is broken </h1>'


@app.route('/article',methods=['POST'])
def article():
	_title = request.form['inputTitle']
	_description = request.form['inputDescription']

	print('Title is %s'%_title)
	print('Description is %s'%_description)
	
	new_article=Article(_title,_description)
	db.session.add(new_article)
	db.session.commit()

	return redirect('/')




if __name__ == "__main__":
    app.run(host = '0.0.0.0',debug=True)

