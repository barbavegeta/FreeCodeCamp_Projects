import copy
import random

class Hat:
    def __init__(self, **balls):
        # Create a list of balls based on the input arguments
        self.contents = []
        for color, count in balls.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # Handle case where number of balls to draw exceeds available balls
        if num_balls >= len(self.contents):
            drawn_balls = self.contents[:]
            self.contents = []  # Empty the hat after drawing all balls
            return drawn_balls

        # Randomly draw balls without replacement
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0

    for _ in range(num_experiments):
        # Create a copy of the hat to ensure each experiment is independent
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)

        # Count the balls drawn
        drawn_count = {}
        for ball in drawn_balls:
            drawn_count[ball] = drawn_count.get(ball, 0) + 1

        # Check if the drawn balls satisfy the expected balls condition
        success = True
        for color, count in expected_balls.items():
            if drawn_count.get(color, 0) < count:
                success = False
                break

        if success:
            successful_experiments += 1

    # Calculate and return the probability
    return successful_experiments / num_experiments

# Example usage
if __name__ == "__main__":
    hat = Hat(blue=5, red=4, green=2)
    probability = experiment(
        hat=hat,
        expected_balls={"red": 1, "green": 2},
        num_balls_drawn=4,
        num_experiments=2000
    )
    print(f"Probability: {probability}")
