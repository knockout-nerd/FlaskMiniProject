from flask import Flask,render_template

app = Flask(__name__)

@app.route('/Home')
def homepage():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/create', methods=["GET","POST"])
def create_post():
    return render_template('posts/create.html')

@app.route('/posts')
def posts():
    posts = []
    return render_template('posts/posts.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)