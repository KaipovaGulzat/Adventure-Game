import maincharacter
import chapter3

def play(player):
    # Chapter 2 Introduction
    print("Chapter 2 Intro: 'The Enchanted Forest'")
    print("Rumors of disturbances in Luminesia's enchanted forest reach Windmere.")
    print("Master Alistair senses dark forces threatening the realm's balance.")
    
    print("\nYou set out on a quest to Luminesia with Master Alistair to investigate the disturbances.")
    print("As you venture deeper into the forest, you encounter magical creatures and sense an enigmatic darkness shrouding the area.")
    
    while True:
        # Present choices to the player
        choice = input("\nWhat will you do?\n1. Choose to aid or confront the magical beings you encounter.\n2. Use your developing spells to overcome obstacles and dispel magical barriers.\n3. Impact your relationship with Master Alistair and the magical world.\n4. Return to Windmere.\n> ")
        
        if choice == "1":
            # Player chooses to aid or confront magical beings
            print("You chose to aid or confront the magical beings you encounter.")
            answer = input("What comes once in a minute, twice in a moment, but never in a thousand years?(Letter O/Letter M)\n> ")
            if answer.lower() == "Letter M":
                # Player successfully interacts with the magical beings and earns their trust
                print("You successfully interact with the magical beings, earning their trust.")
                # Increase your relationship with magical beings
                player.relationshipvillagers += 1
                break  # Exit the loop and move on to Chapter 3
            else:
                # Player's choice had consequences, and their relationship with magical beings is affected
                print("Your choice had consequences, and you must now deal with the aftermath.")
                # Decrease your relationship with magical beings
                player.relationshipvillagers -= 1
        elif choice == "2":
            # Player chooses to use developing spells
            print("You chose to use your developing spells to overcome obstacles and dispel magical barriers.")
            answer = input(" I'm tall when I'm young and short when I'm old. What am I?(a candle/a tree)\n> ")
            if answer.lower() == "a candle":
                # Player's magical abilities continue to improve, and they gain confidence
                print("Your magical abilities continue to improve, and you feel more confident in your skills.")
                # Increase your magical skill
                player.fire += 1
                player.water += 1
                player.earth += 1
                player.air += 1
                break  # Exit the loop and move on to Chapter 3
            else:
                # Player's spells weren't as effective as they hoped, but they remain determined
                print("Your spells weren't as effective as you hoped, but you're determined to keep learning.")
        elif choice == "3":
            # Player chooses to impact their relationship with Master Alistair and the magical world
            print("You attempt to impact your relationship with Master Alistair and the magical world.")
            answer = input("What has keys but can't open locks?(a smart house/a piano)\n> ")
            if answer.lower() == "a piano":
                # Player's positive attitude is noticed, and they strengthen their bond with Master Alistair
                print("Your positive attitude is noticed, and you strengthen your bond with Master Alistair.")
                # Increase your relationship with Master Alistair
                player.relationshipvillagers += 1
                break  # Exit the loop and move on to Chapter 3
            else:
                # Player's indifference may have consequences in the future, but they continue their journey
                print("Your indifference may have consequences in the future, but you continue your journey.")
        chapter3.play(player)  # Move on to Chapter 3


    