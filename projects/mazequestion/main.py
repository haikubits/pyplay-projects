def solution(maze: list[str], actions: list[tuple[int, str]], end_time: int) -> list[str]:
    x_initial, y_initial = 0, 0
    for i in range(len(maze)):
        ball_index = maze[i].find('o')
        if ball_index >= 0:
            x_initial, y_initial = i, ball_index
            break
    x, y = x_initial, y_initial
    # the actions list sorted
    for action in actions:
        # exit if end_time is reached
        if action[0] >= end_time:
            break
        else:
            if action[1].upper() == "FLAT":
                continue
            elif action[1].upper() == "LEFT":
                if maze[x][y-1] != "-":
                    y = y-1
            elif action[1].upper() == "UP":
                if maze[x-1][y] != "|":
                    x = x-1
            elif action[1].upper() == "RIGHT":
                if maze[x][y+1] != "-":
                    y = y+1
            elif action[1].upper() == "DOWN":
                if maze[x+1][y] != "|":
                    x = x+1
    maze[x_initial].replace("o", " ")
    row_list = list(maze[x])
    row_list[y] = "o"
    maze[x] = "".join(row_list)    
    return maze


result = solution(
    [
        ".-.-.-.-.",
        "|     | |",
        ".-.-. . .",
        "|   |   |",
        ". . . . .",
        "| |  o  |",
        ".-.-.-.-.",
    ],
    [(0, "UP"), (3, "RIGHT")],
    10,
)
for row in result:
    print(row)

# UP, DOWN, LEFT, RIGHT, and FLAT

# .-.-.-.-. <-- walls
# |o o o|o|
# .-.-. . . <-- walls
# |o o|o o|
# . . . . . <-- walls
# |o|o o o|
# .-.-.-.-. <-- walls
# ^ ^ ^ ^ ^
# +-+-+-+-+---> walls

# solution():
# -> 
# .-.-.-.-.
# |    o| |
# .-.-. . .
# |   |   |
# . . . . .
# | |     |
# .-.-.-.-.