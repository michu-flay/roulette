# roulette_simulation.py
import json
import random

def simulate_roulette(num_spins=1000, filename="simulation_results.json"):
    results = []

    for _ in range(num_spins):
        # Simulate the roulette spin
        winning_number = random.randint(0, 36)
        winning_color = "red" if winning_number % 2 == 0 else "black"

        # Store the results
        results.append({"number": winning_number, "color": winning_color})

    # Save the results to a JSON file
    with open(filename, "w") as file:
        json.dump(results, file)

if __name__ == "__main__":
    simulate_roulette()
