import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = [element for nestedlist in [[key for _ in range(kwargs[key])] for key in kwargs] for element in nestedlist]

    def draw(self, num):
        draw = num
        if num > len(self.contents):
            draw = len(self.contents)
        return [self.contents.pop(self.contents.index(random.choice(self.contents))) for _ in range(draw)]

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        draw = copy.deepcopy(hat).draw(num_balls_drawn)
        if all(draw.count(ball) >= expected_balls[ball] for ball in expected_balls):
            success += 1
    return success/ num_experiments      

hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
            
