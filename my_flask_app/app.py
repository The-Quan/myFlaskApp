from flask import Flask, render_template, request, redirect, url_for
from post import get_posts, add_posts 
 # Import các hàm từ file posts

app = Flask(__name__)

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    add_posts(title, content)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)