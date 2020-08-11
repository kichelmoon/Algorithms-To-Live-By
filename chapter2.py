import random

places = []
for i in range(10):
    places.append([random.randint(0, 10), 0, 0])

turns = 10
current_turn = 1

player_wins = 0

computer_wins = 0
computer_choice = 1

def is_lucky(place):
    lucky_number = random.randint(0, 10)
    return lucky_number <= place[0]

while current_turn <= turns:
    for i in range(len(places)):
        print(str(i + 1) + ") Wins: " + str(places[i][1]) + " Losses: " + str(places[i][2]))

    turn_message = "Current turn: " + str(current_turn) + "/" + str(turns)  + ": Which place to go to next?"
    player_choice = int(input(turn_message))
    if player_choice > 0 and player_choice < len(places):
        place_index = player_choice - 1
        if is_lucky(places[place_index]):
            print ("You win!")
            places[place_index][1] += 1
            player_wins += 1
        else:
            print("You lose!")
            places[place_index][2] += 1

    place_index = computer_choice - 1
    if is_lucky(places[place_index]):
        computer_wins += 1
    else:
        computer_choice += 1    

    current_turn += 1

print("Player wins: " + str(player_wins))
print("Computer wins: " + str(computer_wins))
