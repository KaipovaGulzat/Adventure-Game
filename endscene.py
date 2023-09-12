import maincharacter
import chapter1

def play(player):
    print("Congratulations! You've reached the end of your magical journey.")
    print("The fate of Gulzat has been determined by your choices and actions.")
    print("\nYour journey has been challenging, and your choices have shaped the outcome.")
    print("The battle against darkness was fierce, and the results reflect your efforts.")
    print("Gulzat's future may be uncertain, but your contributions have made a significant impact.")
    
    print("\nThank you for playing the game! We hope you enjoyed the adventure.")


    play_again = input("Do you want to play again? (yes/no)\n> ")
    if play_again.lower() == "yes":
        print("\nStarting a new game...\n")
        
        chapter1.play(player)
    else:
        print("Goodbye! Have a great day.")
        exit()  # Exit the game

    if __name__ == "__main__":
     print("Welcome to the Magical Adventure Game!")


