import random

places = []
for i in range(10):
    places.append([random.randint(0, 10), 0, 0])

finished = False
while not finished:
    for i in range(len(places)):
        print(str(i + 1) + ") Wins: " + str(places[i][1]) + " Losses: " + str(places[i][2]))
        
    player_choice = int(input("Which place to go to next?"))
    if player_choice > 0 or player_choice < len(places):
        place_index = player_choice - 1
        player_lucky_number = random.randint(0, 10)
        if player_lucky_number <= places[place_index][0]:
            print ("You win!")
            places[place_index][1] += 1
        else:
            print("You lose!")
            places[place_index][2] += 1
    else:
        finished = True
