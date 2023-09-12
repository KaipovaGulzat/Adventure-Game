

""" class player:
    def __init__(self, name):
        self.name = name
    relationshipvillagers = 0
    fire = 0
    water = 0
    earth = 0
    air = 0
    knowledge = []
    abilities = [] """


import maincharacter
def main():
    print("Welcome to the mystical land of Gulzat!")
    player_name = input("Enter your character's name: ")
    maincharacter.player1.name = player_name
    print(maincharacter.player1.name)


    import chapter1
    chapter1.play(maincharacter.player)
    #chapter1.play(player1)

    import chapter2
    chapter2.play(maincharacter.player)

    import chapter3
    chapter3.play(maincharacter.player)

    import chapter4
    chapter4.play(maincharacter.player)

    import chapter5
    chapter5.play(maincharacter.player)

    import endscene
    endscene.play(maincharacter.player)
    


        
if __name__ == "__main__":
    main()
