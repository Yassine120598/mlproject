from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd

class ActionFetchBudget(Action):

    def name(self) -> str:
        return "action_fetch_budget"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict) -> list:
        # Load the Excel file
        budget_data = pd.read_excel("C:/Users/Yassine/Pictures/Budget/budget.xlsx")

        # Get the project name from the tracker
        project_name = tracker.get_slot("project")

        # Check if the project is in the Excel file
        if project_name in budget_data["Project"].values:
            budget = budget_data[budget_data["Project"] == project_name]["Budget"].iloc[0]
            dispatcher.utter_message(text=f"The budget for the project {project_name} is {budget}.")
        else:
            dispatcher.utter_message(text="Sorry, I don't have information about that project.")
        
        return []


