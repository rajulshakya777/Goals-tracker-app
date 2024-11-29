from flask import Flask, render_template, request
from tracker import Tracker

app = Flask(__name__)

# Instantiate the Tracker
tracker = Tracker()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        if "set_goals" in request.form:
            # Set weekly goals
            tracker.set_goals(
                assignments=float(request.form["assignments_goal"]),
                friends=float(request.form["friends_goal"]),
                screen=float(request.form["screen_goal"]),
                exercise=float(request.form["exercise_goal"]),
            )
            message = "Weekly goals set successfully!"
        elif "log_time" in request.form:
            # Log time for a specific category
            data_type = request.form["data_type"]
            time_spent = float(request.form["time_spent"])
            tracker.log_time(data_type, time_spent)
            message = f"Time logged successfully for {data_type.capitalize()}!"

    # Generate all visualizations
    tracker.generate_all_visualizations()

    return render_template("index.html", message=message, goals=tracker.goals)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, port=8000)

