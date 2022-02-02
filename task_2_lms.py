def up_function(world):
    print(world.upper())


def creator_function(world):
    return up_function(world)


creator_function('Hello!')
