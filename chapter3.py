import maincharacter
import chapter4

def play(player):
    # Chapter 3 Introduction
    print("Chapter 3 Intro: 'The Lost Wisdom'")
    print("A cryptic vision leads you to Avalon's ancient ruins, a place of forgotten knowledge and wisdom.")
    
    print("\nAs you step into the ruins, you're surrounded by a hushed stillness. Spectral guardians watch over the sacred space.")
    print("You come across cryptic inscriptions that seem to hold the key to the ancient wisdom sought by many.")
    
    while True:
        # Present choices to the player
        choice = input("\nWhat will you do?\n1. Engage in riddles and puzzles.\n2. Search for ancient spells and artifacts.\n3. Embrace the legacy of the ancient mages.\n4. Return to Windmere.\n> ")
        
        if choice == "1":
            # Player chooses to engage in riddles and puzzles
            print("Your prowess with riddles helps you decipher the inscriptions, revealing hidden paths and secrets.")
            answer = input("I have rivers, but don’t have water. I have dense forests, but no trees and animals. I have cities, but no people live in those cities. What am I?? (a map/river)\n> ")
            if answer.lower() == "a map":
                # Player successfully solves the riddle
                print("Congratulations! You solved the riddle and unlocked the secrets of the ruins.")
                # You can reward the player with knowledge or artifacts here.
                player.knowledge.append("Ancient Wisdom")
                player.abilities.append("Ancient Artifacts")
                break  # Exit the loop and move on to Chapter 4
            else:
                # Player's answer is incorrect
                print("You engage in riddles and puzzles, but your limited understanding hinders your progress in uncovering the inscriptions' meanings.")
                play(player)
        elif choice == "2":
            # Player chooses to search for ancient spells and artifacts
            print("You search the ruins for ancient spells and artifacts. With the 'Ancient Spellbook' in hand, you uncover hidden knowledge.")
            answer = input("I have keys but open no locks. I have space but no room. You can enter, but you can't go inside. What am I?(a keyboard/a cloud)\n> ")
            if answer.lower() == "a keyboard":
                # Player opens and reads the Ancient Spellbook
                print("You've gained valuable knowledge from the Ancient Spellbook.")
                # You can reward the player with magical abilities or spells here.
                player.knowledge.append("Ancient Spells")
                break  # Exit the loop and move on to Chapter 4
            else:
                # Player chooses not to open the Ancient Spellbook
                print("Your search reveals only fragments of knowledge. Without the right resources, your progress is limited.")
                play(player)
        elif choice == "3":
            # Player chooses to embrace the legacy of the ancient mages
            print("I'm light as a feather, yet the strongest person can't hold me for much longer than a minute. What am I?(light/breath)\n> ")
            if answer.lower() == "breath":
                # Player feels a strong connection to ancient magic
                print("Your connection to ancient magic grows stronger, granting you new abilities.")
                # You can reward the player with enhanced magical abilities here.
                break  # Exit the loop and move on to Chapter 4
            else:
                # Player's connection to ancient magic is weak
                print("You attempt to embrace the legacy of the ancient mages, but your connection is weak without the guidance of your mentor.")
                play(player)

    chapter4.play(player)  # Move on to Chapter 4


