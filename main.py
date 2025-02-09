from dataclasses import dataclass
import numpy as np
import matplotlib.pyplot as plt

CALORIE_GOAL_LIMIT = 3000
PROTEIN_GOAL = 180
FAT_GOAL = 80
CARBS_GOAL = 300
today = []

@dataclass
class Food:
    name: str
    calories: int
    protein: int  
    carbs: int

done = False
while not done:
    print("""
    (1) Add a new food
    (2) Visualize progress
    (q) Quit
    """)

    choice = input("Choose an option: ")
    if choice == "1":
        print("Adding a new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protein = int(input("Proteins: ")) 
        fat = int(input("Fats: "))  
        carbs = int(input("Carbs: "))
        food = Food(name, calories, protein, fat, carbs)  
        today.append(food)
        print("Successfully added!")
    elif choice == "2":
        calorie_sum = sum(food.calories for food in today)
        protein_sum = sum(food.protein for food in today) 
        fat_sum = sum(food.fat for food in today)  
        carbs_sum = sum(food.carbs for food in today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"])
        axs[0, 0].set_title("Macronutrients Distribution")  
        axs[0,1].bar([0,1,2],[protein_sum,fat_sum,carbs_sum],width=0.4)
        axs[0,1].bar([0.5,1.5,2.5],[PROTEIN_GOAL,FAT_GOAL,CARBS_GOAL],width=0.4)
        axs[0,1].set_title("Macronutrients Progress")
        axs[1,0].pie([calorie_sum,CALORIE_GOAL_LIMIT-calorie_sum],labels=["Calories","Remaining"],autopct="%1.1f%%")
        axs[1,0].set_title(["Calories Goal Progress"])
        axs[1,1].plot(list(range(len(today))),np.cumsum([food.calories for food in today]),label="Calories Eaten")
        axs[1,1].plot(list(range(len(today))),[CALORIE_GOAL_LIMIT]*len(today),label="Calories Goal")
        axs[1,1]._legend()
        axs[1,1].set_title("Calorie Goal over Time")
        fig.tight_layout()
        plt.show()
    elif choice == "q":
        done = True
    else:
        print("Invalid choice. Please try again.")