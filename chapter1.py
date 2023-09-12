import maincharacter
import chapter2
import endscene

def play(player):
    # Chapter 1 Introduction
    print("Chapter 1 Intro: 'The Awakening'")
    print("Begin your journey in the village of Windmere, a place known for its connection to the elements.")
    print("Your magical training under Master Alistair begins, but a mysterious event reveals your latent potential, marked by a long-lost prophecy.")

    print("\nYou find yourself in the practice yard of the Enchanter's Guild. Today's training session is about to begin.")
    print("You watch as fellow apprentices engage in elemental magic practice.")

    while True:
        # Present choices to the player
        choice = input("\nWhat will you do?\n1. Interact with villagers and apprentices.\n2. Train in elemental magic.\n3. Uncover the hidden history of the prophecy.\n> ")

        
        if choice == "1":
            # Player chooses to interact with villagers and apprentices
            print("You approach some villagers and fellow apprentices, engaging in conversations and learning about the prophecy.")
            answer = input("I'm not alive, but I can grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?(fire/water)\n> ")
            if answer.lower() == "fire":
                # Player successfully interacts with villagers and apprentices
                print("You successfully interact with villagers and apprentices, earning their trust.")
                # Increase your relationship with magical beings
                player.relationshipvillagers += 1
            else:
                # Player's choice had consequences, and their relationship with magical beings is affected
                print("Your choice had consequences, and you must now deal with the aftermath.")
                # Decrease your relationship with magical beings
                player.relationshipvillagers -= 1
        elif choice == "2":
            # Player chooses to train in elemental magic
            print("You focus on practicing your elemental magic, honing your abilities in fire, water, earth, and air.")
            answer = input("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?(echo/wind)\n> ")
            if answer.lower() == "echo":
                # Player's magical abilities continue to improve, and they gain confidence
                print("Your magical abilities continue to improve, and you feel more confident in your skills.")
            else:
                # Player's spells weren't as effective as they hoped, but they remain determined
                print("Your spells weren't as effective as you hoped, but you're determined to keep learning.")
        elif choice == "3":
            # Player chooses to uncover the hidden history of the prophecy
            print("You delve into the Guild's archives, researching the prophecy and its significance.")
            answer = input("The more you take, the more you leave behind. What am I?(footsteps/money)\n> ")
            if answer.lower() == "footsteps":
                # Player gains knowledge about the prophecy
                print("You uncover valuable information about the prophecy, deepening your understanding of your destiny.")
                # Add knowledge about the prophecy
                player.knowledge.append("prophecy")
            else:
                # Player's research didn't yield significant results, but they remain determined
                print("Your research didn't yield significant results, but you're determined to keep searching for answers.")
        else:
            # Player provides an invalid choice
            print("Invalid choice. Please choose a valid option.")

        # Continue the story by moving to the next chapter
        break