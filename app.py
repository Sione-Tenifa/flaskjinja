from flask import Flask, request, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from random import randint, choice, sample 

app = Flask(__name__)
app.config['SECRET_KEY'] = "DEBUG1989"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = ['Amadeasu', 'Chicken Run', "Sandlot"]

@app.route('/movies')
def show_all_movies():
    return render_template('movies.html', movies=MOVIES)

@app.route('/movies/new', methods=["POST"])
def add_movies():
    title = request.form['title']
    # ADD to pretend DB
    MOVIES.append(title)
    return redirect('/movies')



@app.route('/old-home-page')
def redirect_to_home():
    return redirect("/")

@app.route('/')
def home_page():
    return render_template("hello.html")

@app.route('/hello')
def say_hello():
    html = """
    <html>
        <body>
            <h1>Hello!</h1>
            <p> This is the Hello page</p>
        </body>
    </html>
    """
    return html

@app.route('/goodbye')
def say_bye():
    return "Good Bye!"


@app.route('/search')
def search():
    term = request.args["term"]
    return f"<h1> Search results For: {term}</h1>"

@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <h1>Add Comment</h1> 
      <form method="POST">
        <input placeholder="comment" name="comment">
        <input placeholder="unsername" name="username">
        <button>Submit</button>
      </form>
      """

@app.route("/add-comment", methods=["POST"])
def add_comment():
    """Handle adding comment."""
    username = request.form["username"]
    print(request.form)
    comment = request.form["comment"]

    # TODO: save that into a database!

    return f"""
        <h1>SAVED YOUR COMMENT.</h1>
        <ul>
            <li>User name: {username}</li>
            <li>Comment: {comment}
        </ul>
        """

@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1> Browsing the {subreddit} Subreddit</h1>"

@app.route('/r/<subreddit>/comments/<int:post_id>')    
def show_comments(subreddit, post_id):
    return f"<h1> Viewing comments for post with id: {post_id} from the {subreddit}</h1>"
      
POSTS = {
    1: "Not that good",
    2: "decent",
    3: "The best",
    4: "Favorite"
}

@app.route('/posts/<int:id>')
def find_post(id):
    post = POSTS.get(id, "Post not found")
    return f"<p>{post}</p>"

@app.route('/lucky')
def lucky_num():
    num = randint(1,10)
    return render_template('lucky.html', lucky_num=num)

@app.route('/form')
def show_form():
    return render_template("from.html")

@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)

COMPLIMENTS = ['Cool', "Clever", "Tenacious", "Awesome"]

@app.route('/spell/<word>')
def spell_word(word):
    return render_template('spell_word.html', word=word)

@app.route('/form2')
def show_form_2():
    return render_template("form_2.html")

@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants_compliments = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template('greet_2.html', username=username, wants_complments=wants_compliments, compliments=nice_things)
