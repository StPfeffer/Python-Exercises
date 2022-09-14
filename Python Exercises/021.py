from math import sqrt


print("Tip: Enter as 'UP/DOWN/LEFT/RIGHT amount_of_steps'")

origin = [0, 0]
pos = [0, 0]

while True:
    s = input("Enter the direction and the steps: ")

    if not s:
        break

    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    elif direction == "LEFT":
        pos[1] -= steps
    else:
        pass

distance_origin = int(round(sqrt(pos[1] ** 2 + pos[0] ** 2)))
print(distance_origin)
