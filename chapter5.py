import maincharacter
import endscene

def play(player):
        print("Chapter 5 Intro: 'The Final Enchantment'")
        print("The showdown between light and darkness draws near.")
        print("Confront the ancient evil, using the power of prophecy to banish darkness from Gulzat.")
        
        print("\nThe final magical battle unfolds in the heart of Windmere, where the balance of power tips on the edge.")
        print("Your journey has led you here, and the choices you've made will determine the ultimate outcome.")
        
        choice = input("\nWhat will you do?\n1. Engage in a thrilling magical battle, showcasing mastered spells.\n2. Make choices reflecting your values embraced during the journey.\n3. Determine Gulzat's fate and the legacy of your magical journey.\n> ")
        
        if choice == "1":
                print("You unleash a torrent of magical energy, showcasing your mastery over various spells.")
                print("The ancient knowledge you've acquired empowers your magic, making you a formidable force.")
                answer = input("You can see me in water, but I never get wet. What am I?(reflection/shadow)\n> ")
                if answer.lower() == "reflection":
                   endscene.play(player)
                else:
                   print("You engage in the magical battle, but your lack of advanced spells hinders your performance.")
                   play(player) 

        if choice == "2":
                print("You draw upon your deep connection with light magic and make choices aligned with your values.")
                answer = input("I can be cracked, made, told, and played. What am I?(a clown/a joke)\n> ")
                if answer.lower() == "a joke":
                  endscene.play(player)
                else:
                  print("You struggle to make impactful choices, as your light magic isn't yet strong enough to guide you decisively.")
                  play(player)

        elif choice == "3":
                print("With the guidance of Master Alistair and the trust of the villagers, you take charge of the battle.")
                print("Your leadership and conviction shape the outcome, ensuring a brighter future for Gulzat.")
                answer = input("I'm full of holes, yet I can still hold water. What am I? (a sponge/skin)\n> ")
                if answer.lower() == "a sponge":
                  endscene.play(player)
                else:
                  print("Without the strong support of your mentor and the villagers, your influence over the battle's outcome is limited.")
                  print("As you confront the ancient evil, the culmination of your journey will reveal the legacy you leave behind.")
                  play(player)


