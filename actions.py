from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
import matplotlib.pyplot as plt

class ActionShowProjectBudget(Action):
    def name(self):
        return "action_show_project_budget"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        try:
            budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
            project_name = tracker.get_slot('project')
            
            if project_name in budget_data['Project'].values:
                project_budget = budget_data[budget_data['Project'] == project_name]['Budget '].values[0]
                dispatcher.utter_message(f"The allocated budget for project {project_name} is {project_budget}.")
            else:
                dispatcher.utter_message(f"Sorry, I couldn't find the project named {project_name}.")
        except Exception as e:
            dispatcher.utter_message(f"Sorry, I faced an error while fetching the data: {e}")

class ActionShowOverconsumption(Action):
    def name(self):
        return "action_show_overconsumption"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        try:
            budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
            project_name = tracker.get_slot('project')
            
            if project_name in budget_data['Project'].values:
                overconsumption = budget_data[budget_data['Project'] == project_name]['overconsumption'].values[0]
                dispatcher.utter_message(f"The overconsumption for project {project_name} is {overconsumption}.")
            else:
                dispatcher.utter_message(f"Sorry, I couldn't find the project named {project_name}.")
        except Exception as e:
            dispatcher.utter_message(f"Sorry, I faced an error while fetching the data: {e}")

class ActionShowBudgetPerMonthHistogram(Action):
    def name(self):
        return "action_show_budget_per_month_histogram"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        try:
            budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
            monthly_budgets = budget_data[['Budget Per June', 'Budget per july', 'Budget per august ']].sum()
            
            monthly_budgets.plot(kind='bar')
            plt.title('Budget Allocated Each Month')
            plt.ylabel('Budget')
            plt.xlabel('Month')
            plt.tight_layout()
            
            plt.savefig("C:/Users/Yassine/Pictures/12/monthly_budget_histogram.png")
            
            dispatcher.utter_message(image="http://your_server_address_or_domain/path_to_image/monthly_budget_histogram.png")
        except Exception as e:
            dispatcher.utter_message(f"Sorry, I faced an error while generating the histogram: {e}")

class ActionShowMonthlyBudget(Action):
    def name(self):
        return "action_show_monthly_budget"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: dict):
        try:
            budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
            project_name = tracker.get_slot('project')
            
            if project_name in budget_data['Project'].values:
                project_data = budget_data[budget_data['Project'] == project_name]
                budget_june = project_data['Budget Per June'].values[0]
                budget_july = project_data['Budget per july'].values[0]
                budget_august = project_data['Budget per august '].values[0]
                
                response = (f"The monthly budget distribution for project {project_name} is:\n"
                            f"June: {budget_june}\n"
                            f"July: {budget_july}\n"
                            f"August: {budget_august}")
                dispatcher.utter_message(response)
            else:
                dispatcher.utter_message(f"Sorry, I couldn't find the project named {project_name}.")
        except Exception as e:
            dispatcher.utter_message(f"Sorry, I faced an error while fetching the monthly budget data: {e}")

