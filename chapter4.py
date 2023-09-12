
import maincharacter
import chapter5

def play(player):
        print("Chapter 4 Intro: 'The Gathering Storm'")
        print("The darkness looms larger, and an ancient evil threatens Gulzat.")
        print("Master Alistair senses a malevolent presence gathering strength.")
        
        print("\nYou return to Windmere, where the villagers are on edge, sensing the impending danger.")
        print("With Master Alistair's guidance, you prepare to fortify defenses and face the ultimate confrontation with the dark forces.")
        
        choice = input("\nWhat will you do?\n1. Collaborate with villagers to strengthen defenses.\n2. Delve into arcane mysteries to empower your magical abilities.\n3. Face moral dilemmas shaping the outcome of the approaching battle.\n> ")
        
        
        if choice == "1":
            print("You rally the villagers and together you reinforce the defenses of Windmere, creating a united front.")
            answer = input("I have wings, but I'm not a bird; I'm not alive, but I can fly. What am I?(AbbyFrank/an airplane)\n> ")
            if answer.lower() == "an airplane":
                chapter5.play(player)
            else:
                print("Your attempts to collaborate with the villagers are met with skepticism. The defenses remain fragmented.")
                play(player)  # Start Chapter 4 again
            
        if choice == "2":
            print("You study the 'Arcane Codex,' uncovering hidden knowledge that empowers your magical abilities.")
            answer = input("What can travel around the world while staying in a corner? (A postage stamp/a bird)\n>")
            if answer.lower() == "A postage stamp":
                 chapter5.play(player)
            else: 
                    print("Your attempts to delve into arcane mysteries are hindered by your lack of suitable resources.")
                    play(player) #start chapter 4 again

        elif choice == "3":
                print("You grapple with moral dilemmas and make choices that resonate with your light magic. Your convictions are resolute.")
                answer = input("I have a heart that never beats, I can't breathe, but I need air; I have no mouth but can speak. What am I?(a bell/a fire)\n>")
                if answer.lower() == "a bell":
                     chapter5.play(player)
                else:
                   print("You have to work on your beliefs.")
                   play(player) #start chapter 4 again
        
        



