import flet as ft
import random

def main(page: ft.Page):
    page.title = "Favorite Snack selector machine"

    Snack = ft.Dropdown(
        label="Do you prefer salty or sweet snacks?",
        options=[
            ft.dropdown.Option("salty"),
            ft.dropdown.Option("sweet"),
        ],
    )

    Drink = ft.Dropdown(
        label="Do you prefer water, juice, or soda?",
        options=[
            ft.dropdown.Option("water"),
            ft.dropdown.Option("juice"),
            ft.dropdown.Option("soda"),
        ],
    )

    Mood = ft.Dropdown(
        label="How are you feeling today?(optional)",
        options=[
            ft.dropdown.Option("tired😐"),
            ft.dropdown.Option("energetic⚡️"),
            ft.dropdown.Option("happy😆"),
            ft.dropdown.Option("relaxed😎"),
        ],
    )

    output = ft.Column()
    warning = ft.Text(color="red")

    def Submit(e):
        snack = Snack.value
        drink = Drink.value
        mood = Mood.value

        output.controls.clear()
        warning.value = ""

        if not snack:
            warning.value = "Choose a snack."
            page.update()
            return
        
        if not drink:
            warning.value = "Choose a drink."
            page.update()
            return

        output.controls.append(ft.Text("Snack suggestion:"))
        if snack == "salty":
            output.controls.append(ft.Text("You might like popcorn or potato chips."))
        elif snack == "sweet":
            output.controls.append(ft.Text("You might like donuts or Oreos."))

        output.controls.append(ft.Text("Drink suggestion:"))
        if drink == "water":
            output.controls.append(ft.Text("You might like fruit water or just normal water."))
        elif drink == "juice":
            output.controls.append(ft.Text("You might like orange and apple juices."))
        elif drink == "soda":
            output.controls.append(ft.Text("You might like Pepsi or Coca-Cola."))
        else:
            output.controls.append(ft.Text("You might like cookies with milk."))

        output.controls.append(ft.Text("Snack and Drink combo idea:"))
        if snack == "salty" and drink == "water":
            output.controls.append(ft.Text("You might like nuts with any type of water."))
        elif snack == "salty" and drink == "juice":
            output.controls.append(ft.Text("You might like chips with orange juice."))
        elif snack == "salty" and drink == "soda":
            output.controls.append(ft.Text("You might like popcorn with Sprite."))
        elif snack == "sweet" and drink == "water":
            output.controls.append(ft.Text("You might like yogurt with any type of water."))
        elif snack == "sweet" and drink == "juice":
            output.controls.append(ft.Text("You might like fruit with orange juice."))
        elif snack == "sweet" and drink == "soda":
            output.controls.append(ft.Text("You might like donuts with Coca-Cola."))

        if mood:
            output.controls.append(ft.Text("Suggestion based on your mood:", weight="bold"))
            if mood == "tired😐":
                output.controls.append(ft.Text("Try a chocolate bar with coffee or maybe a soda to boost your energy."))
            elif mood == "energetic⚡️":
                output.controls.append(ft.Text("Try some sweet potatoes, eggs, or leafy greens"))
            elif mood == "happy😆":
                output.controls.append(ft.Text("Have some cupcakes and an apple juice, you deserve it"))
            elif mood == "relaxed😎":
                output.controls.append(ft.Text("Have some avocadoes, hot chocolate, or fruits to relax"))

        if mood:
            score = 50 
            if snack == "sweet" and mood in ["happy😆", "relaxed😎"]:
                score = 90
            elif snack == "salty" and mood in ["energetic⚡️", "tired😐"]:
                score = 85
            elif drink == "juice" and mood == "happy😆":
                score = 80
            elif drink == "water" and mood == "relaxed😎":
                score = 75
            elif snack == "sweet" and mood == "tired😐":
                score = 60
            else:
                score = 40
            output.controls.append(ft.Text("Mood Match Score:", weight="bold"))
            if score >= 90:
                output.controls.append(ft.Text(f"✅ {score} Excellent match for your mood!"))
            elif score >= 70:
                output.controls.append(ft.Text(f"👍 {score} Pretty good combo."))
            elif score >= 50:
                output.controls.append(ft.Text(f"😐 {score} Maybe."))
            else:
                output.controls.append(ft.Text(f"❌ {score} Not a good combo, try something else"))

        page.update()

    def Reset(e):
        Snack.value = False
        Drink.value = False
        Mood.value = False
        warning.value = ""
        output.controls.clear()
        page.update()

    def help(e):
        output.controls.clear()
        output.controls.append(ft.Text("Welcome to the Snack and Drink Selector!"))
        output.controls.append(ft.Text("Choose your preferred snack."))
        output.controls.append(ft.Text("Choose your preferred drink."))
        output.controls.append(ft.Text("Optionally, select your mood (tired, energetic, happy, relaxed)."))
        output.controls.append(ft.Text("Click 'Submit' to receive suggestions."))
        output.controls.append(ft.Text("If you want to start over, click 'Reset'."))
        page.update()

    def WomboCombo(e):
        snacks = ["salty", "sweet"]
        drinks = ["water", "juice", "soda"]
        snackChoice = random.choice(snacks)
        drinkChoice = random.choice(drinks)
        
        output.controls.clear()
        output.controls.append(ft.Text("Randomized combination:"))
        output.controls.append(ft.Text(f"Snack: {snackChoice}"))
        output.controls.append(ft.Text(f"Drink: {drinkChoice}"))
        
        output.controls.append(ft.Text("Random Snack + Drink combo idea:"))
        if snackChoice == "salty" and drinkChoice == "water":
            output.controls.append(ft.Text("You might like nuts with any type of water."))
        elif snackChoice == "salty" and drinkChoice == "juice":
            output.controls.append(ft.Text("You might like chips with orange juice."))
        elif snackChoice == "salty" and drinkChoice == "soda":
            output.controls.append(ft.Text("You might like popcorn with Sprite."))
        elif snackChoice == "sweet" and drinkChoice == "water":
            output.controls.append(ft.Text("You might like yogurt with any type of water."))
        elif snackChoice == "sweet" and drinkChoice == "juice":
            output.controls.append(ft.Text("You might like fruits with orange juice."))
        elif snackChoice == "sweet" and drinkChoice == "soda":
            output.controls.append(ft.Text("You might like donuts with Coca-Cola."))

        page.update()

    submitButton = ft.ElevatedButton("Submit", on_click=Submit)
    resetButton = ft.OutlinedButton("Reset", on_click=Reset)
    helpButton = ft.OutlinedButton("Help", on_click=help)  
    WomboComboButton = ft.OutlinedButton("Random Combo", on_click=WomboCombo)

    page.add(
        Snack,
        Drink,
        Mood,
        ft.Row([submitButton, resetButton, helpButton, WomboComboButton], spacing=10), 
        warning,
        output
    )

ft.app(target=main)
