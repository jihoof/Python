stair_number = int(input())
all_list = [[] for i in range(stair_number+2)]
for _ in range(stair_number+1):
    all_list[0].append(" ")
comp_move = 4
player_move = 7

if stair_number % 2 != 0:
    for i in range(1, ((stair_number+1)//2) + 1):
        for _ in range(i):
            all_list[i].append('■')
        for _ in range((stair_number+1)-(i*2)):
            all_list[i].append(" ")
        for _ in range(i):
            all_list[i].append('■')
   
elif stair_number % 2 == 0:
    for i in range(1, (stair_number//2) + 1):
        for _ in range(i):
            all_list[i].append('■')
        for _ in range((stair_number+1)-(i*2)):
            all_list[i].append(" ")
        for _ in range(i):
            all_list[i].append('■')

if comp_move + player_move != stair_number:
    if player_move <= (stair_number-1) // 2:
        all_list[player_move][player_move] =  "○"
    elif player_move > (stair_number-1) // 2:
        all_list[stair_number-player_move][player_move] = "○"
    if comp_move >(stair_number-1) // 2:
        all_list[stair_number-comp_move][-comp_move-1] =  "●"
    elif comp_move <= (stair_number-1) // 2:
        all_list[comp_move][-comp_move-1] = "●"

else:
    if player_move <= (stair_number-1) // 2:
        all_list[player_move][player_move] =  "◴"
    elif player_move > (stair_number-1) // 2:
        all_list[stair_number-player_move][player_move] = "◴"



for line in all_list:
    for i in line:
        print(i,end = '')
    print()