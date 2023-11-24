# create_simulation_data.py
import random
import json

class RouletteSimulation:
    def __init__(self):
        self.numbers = list(range(1, 37))
        self.colors = {1: 'red', 2: 'black', 3: 'red', 4: 'black', 5: 'red', 6: 'black', 7: 'red', 8: 'black',
                       9: 'red', 10: 'black', 11: 'black', 12: 'red', 13: 'black', 14: 'red', 15: 'black', 16: 'red',
                       17: 'black', 18: 'red', 19: 'red', 20: 'black', 21: 'red', 22: 'black', 23: 'red', 24: 'black',
                       25: 'red', 26: 'black', 27: 'red', 28: 'black', 29: 'black', 30: 'red', 31: 'black', 32: 'red',
                       33: 'black', 34: 'red', 35: 'black', 36: 'red'}
        self.results = []

    def spin_wheel(self):
        return random.choice(self.numbers)

    def run_simulation(self, num_spins):
        for _ in range(num_spins):
            result = self.spin_wheel()
            self.results.append({"number": result, "color": self.colors[result]})

    def save_results(self, filename="simulation_results.json"):
        with open(filename, "w") as file:
            json.dump(self.results, file)

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

# Example usage:
if __name__ == "__main__":
    simulation = RouletteSimulation()
    simulation.run_simulation(1000)  # Change the number of spins as needed
    simulation.save_results()
    print("Simulation completed. Results saved in simulation_results.json")
