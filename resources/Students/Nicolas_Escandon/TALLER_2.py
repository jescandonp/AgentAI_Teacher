think(100)
contador = 0
while front_is_clear():
    move()
    if object_here():
        take()
        contador = contador + 1 
    if wall_in_front():
        turn_left()
    if at_goal():
        pause()
print ("la cantidad de manzanas fueron", contador)

