world=['australia', 'italy', 'france', 'spain', 'england']
print(world)
# sorted alphabatically - not permanently
print(sorted(world))
# check that storage stays the same
print(world)
# temporarily sort in reverse
world=['australia', 'italy', 'france', 'spain', 'england']
print(sorted(world, reverse=True))
#check that storage is the same
print(world)

#change order permenantly
world.reverse()
print(world)

#reverse it again
world.reverse()
print(world)

#use of sort alphabatically
world.sort()
print(world)

#sort in alphabatically reverse order
world.sort(reverse=True)
print(world)