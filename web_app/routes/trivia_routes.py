from flask import Blueprint, request, jsonify, render_template, redirect, flash # FYI new imports

from app.trivia_service import list_question

trivia_routes = Blueprint("trivia_routes", __name__)

#@trivia_routes.route("/trivia/game.json")
#def trivia_game_api():
#
#    print("THIS IS YOUR TRIVIA GAME (API)...")
#    print("URL PARAMS:", dict(request.args))
#
#    return ----
    #accept user input here. adapt to nmbr of players later

    # country_code = request.args["country_code"] #the dict might not have this key all the time
    #country_code = request.args.get("country_code") or "US"
    #zip_code = request.args.get("zip_code") or "20057"

    #data validation here 
    #get_hourly_forecasts this function fetches in information from the API 
    #results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
    #if results:
        #return jsonify(results)
    #else:
        #return jsonify({"message":"Invalid Geography. Please try again."}), 404

@trivia_routes.route("/trivia/game", methods=["POST"])
def trivia_game():
    print("THIS IS YOUR TRIVIA GAME...")
    return render_template("trivia_game.html")

#@weather_routes.route("/weather/forecast", methods=["GET", "POST"])
#def weather_forecast():
#    print("WEATHER FORECAST...")
#
#    if request.method == "GET":
#        print("URL PARAMS:", dict(request.args))
#        request_data = dict(request.args)
#    elif request.method == "POST": # the form will send a POST
#        print("FORM DATA:", dict(request.form))
#        request_data = dict(request.form)
#
#    country_code = request_data.get("country_code") or "US"
#    zip_code = request_data.get("zip_code") or "20057"
#
#    results = get_hourly_forecasts(country_code=country_code, zip_code=zip_code)
#    if results:
#        flash("Weather Forecast Generated Successfully!", "success")
#        return render_template("weather_forecast.html", country_code=country_code, zip_code=zip_code, results=results)
#    else:
#        flash("Geography Error. Please try again!", "danger")
#        return redirect("/weather/form")