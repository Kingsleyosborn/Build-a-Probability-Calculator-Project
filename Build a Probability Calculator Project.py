import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        if num_balls >= len(self.contents):
            return self.contents
        
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a copy of the hat to draw from
        temp_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        drawn_balls = temp_hat.draw(num_balls_drawn)

        # Count the balls in the drawn list
        drawn_balls_count = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        
        # Check if drawn balls meet or exceed expected balls
        success = all(drawn_balls_count.get(color, 0) >= count for color, count in expected_balls.items())
        
        if success:
            successful_experiments += 1

    probability = successful_experiments / num_experiments
    return probability
