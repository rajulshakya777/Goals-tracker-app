import matplotlib
matplotlib.use("Agg") 
import matplotlib.pyplot as plt

class Tracker:
    def __init__(self):
        self.goals = {
            "assignments": 0.0,
            "friends": 0.0,
            "screen": 0.0,
            "exercise": 0.0,
        }
        self.progress = {
            "assignments": 0.0,
            "friends": 0.0,
            "screen": 0.0,
            "exercise": 0.0,
        }
        self.labels = {
            "assignments": "Time Spent on Assignments",
            "friends": "Time Spent with Friends",
            "screen": "Time Spent on Screen",
            "exercise": "Time Spent on Sports/Exercise/Gym",
        }

    def set_goals(self, assignments, friends, screen, exercise):
        """Set weekly goals for each category."""
        self.goals["assignments"] = assignments
        self.goals["friends"] = friends
        self.goals["screen"] = screen
        self.goals["exercise"] = exercise

    def log_time(self, data_type, time_spent):
        """Log time spent for a specific category."""
        if data_type in self.progress:
            self.progress[data_type] += time_spent

    def generate_all_visualizations(self):
        """Generate visualizations for all data types."""
        self.generate_pie_chart("assignments")
        self.generate_pie_chart("friends")
        self.generate_pie_chart("screen")
        self.generate_pie_chart("exercise")

    def generate_pie_chart(self, data_type):
        """Generate a pie chart for a specific category."""
        spent = self.progress.get(data_type, 0)
        goal = self.goals.get(data_type, 0)

        # Handle cases where the goal is zero or invalid
        if goal == 0:
            print(f"Warning: Goal for {data_type} is zero. Skipping chart generation.")
            return

        # Calculate remaining time
        remaining = max(goal - spent, 0)

        # Validate the data to prevent NaN or invalid states
        if spent < 0 or remaining < 0:
            print(f"Warning: Invalid data for {data_type}. Skipping chart generation.")
            return

        # Prepare data for pie chart
        labels = ["Spent", "Remaining"]
        sizes = [spent, remaining]
        colors = ["#ff9999", "#66b3ff"]

        try:
            plt.figure(figsize=(6, 6))
            plt.pie(
                sizes, labels=labels, autopct="%1.1f%%", colors=colors, startangle=90
            )
            plt.title(f"{self.labels[data_type]} Progress")
            plt.savefig(f"static/plots/{data_type}.png", bbox_inches="tight")
            plt.close()
        except ValueError as e:
            print(f"Error generating chart for {data_type}: {e}")
