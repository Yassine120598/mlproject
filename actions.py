from rasa_sdk import Action
import pandas as pd
import matplotlib.pyplot as plt

class ActionShowProjectBudget(Action):
    def name(self):
        return "action_show_project_budget"

    def run(self, dispatcher, tracker, domain):
        # Read the Excel file
        budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
        
        # Get the project name from the captured entity
        project_name = tracker.get_slot('project')
        
        # Fetch the budget for this project
        project_budget = budget_data[budget_data['Project'] == project_name]['Budget '].values[0]
        
        # Send the response
        dispatcher.utter_message(f"The allocated budget for project {project_name} is {project_budget}.")

class ActionShowOverconsumption(Action):
    def name(self):
        return "action_show_overconsumption"

    def run(self, dispatcher, tracker, domain):
        # Read the Excel file
        budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
        
        # Get the project name from the captured entity
        project_name = tracker.get_slot('project')
        
        # Fetch the overconsumption for this project
        overconsumption = budget_data[budget_data['Project'] == project_name]['overconsumption'].values[0]
        
        # Send the response
        dispatcher.utter_message(f"The overconsumption for project {project_name} is {overconsumption}.")

class ActionShowBudgetPerMonthHistogram(Action):
    def name(self):
        return "action_show_budget_per_month_histogram"

    def run(self, dispatcher, tracker, domain):
        # Read the Excel file
        budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
        
        # Aggregating the monthly budgets
        monthly_budgets = budget_data[['Budget Per June', 'Budget per july', 'Budget per august ']].sum()
        
        # Plotting the histogram
        monthly_budgets.plot(kind='bar')
        plt.title('Budget Allocated Each Month')
        plt.ylabel('Budget')
        plt.xlabel('Month')
        plt.tight_layout()
        
        # Save the figure
        plt.savefig("C:/Users/Yassine/Pictures/12/monthly_budget_histogram.png")
        
        # Send the response (you might need to integrate a way to display the image in your chat interface)
        dispatcher.utter_message(image="C:/Users/Yassine/Pictures/12/monthly_budget_histogram.png")

class ActionShowMonthlyBudget(Action):
    def name(self):
        return "action_show_monthly_budget"

    def run(self, dispatcher, tracker, domain):
        # Read the Excel file
        budget_data = pd.read_excel("C:/Users/Yassine/Pictures/12/budgetM.xlsx")
        
        # Get the project name from the captured entity
        project_name = tracker.get_slot('project')
        
        # Fetch the monthly budget details for this project
        project_data = budget_data[budget_data['Project'] == project_name]
        budget_june = project_data['Budget Per June'].values[0]
        budget_july = project_data['Budget per july'].values[0]
        budget_august = project_data['Budget per august '].values[0]
        
        # Send the response
        response = (f"The monthly budget distribution for project {project_name} is:\n"
                    f"June: {budget_june}\n"
                    f"July: {budget_july}\n"
                    f"August: {budget_august}")
        dispatcher.utter_message(response)


