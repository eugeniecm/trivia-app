# web_app/routes/home_routes.py

from flask import Blueprint, request, render_template
from app.trivia_service import list_question
home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    #return "Welcome Home"
    return render_template("home.html")

#@home_routes.route("/trivia/game")
#def about():
#    print("TRIVIA GAME:")
#    #return "About Me"
#    return render_template("trivia_game.html")

@home_routes.route("/another")
def another():
    print("ANOTHER PAGE MAYBE...")
    return "Here is another page"

@home_routes.route("/trivia/game")
def trivia_game():
    print("THIS IS YOUR TRIVIA GAME...")
    outcome = list_question()
    return render_template("trivia_game.html", outcome=outcome)

@home_routes.route("/hello")
def hello_world():
    print("HELLO...", dict(request.args))

    # go check the URL params for one called "name", and use it if possible
    # if no "name" parameter is specified, use a default value
    name = request.args.get("name") or "World"


    message = f"Hello, {name}!"
    #return message
    return render_template("hello.html", message=message, other="YOLO")