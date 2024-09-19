
import random

# Function to generate a valid circle with directional restrictions and a variable number of generations
def generate_circle_with_generations(participants, restrictions, generations):
    def shuffle(array):
        random.shuffle(array)

    def is_valid_circle(circle, restrictions):
        for i in range(len(circle)):
            giver = circle[i]
            receiver = circle[(i + 1) % len(circle)]  # Circular wrap-around
            if (giver, receiver) in restrictions:
                return False
        return True

    circle = []
    valid_generation = 0

    while valid_generation < generations:
        circle = participants[:]
        shuffle(circle)

        if is_valid_circle(circle, restrictions):
            valid_generation += 1

    result = [(circle[i], circle[(i + 1) % len(circle)]) for i in range(len(circle))]
    return result

# List of participants and restrictions
participants = ["Csaba", "Marcsi", "Netti", "Gergo", "Eni", "Judit", "Dani"]
restrictions = [
    ("Marcsi", "Csaba"),
    ("Csaba", "Marcsi"),
    ("Netti", "Gergo"),
    ("Gergo", "Netti"),
    ("Judit", "Dani"),
    ("Dani", "Judit"),
    ("Marcsi", "Gergo"),
    ("Netti", "Marcsi"),
    ("Csaba", "Judit"),
    ("Gergo", "Csaba"),
    ("Judit", "Netti"),
    ("Eni", "Dani"),
    ("Dani", "Eni"),
]

# Define the number of generations as a separate variable
generations = 998

# Generate and display the result of the nth valid generation
result = generate_circle_with_generations(participants, restrictions, generations)
print("Gift exchange circle:")
for giver, receiver in result:
    print(f"{giver} -> {receiver}")
