# analyze_simulation.py
import pandas as pd
import matplotlib.pyplot as plt

def analyze_results(filename="simulation_results.json"):
    # Load simulation results from the file
    with open(filename, "r") as file:
        results = pd.read_json(file)

    # Calculate the frequency of winning numbers
    number_counts = results["number"].value_counts().sort_index()

    # Calculate the probability of each number
    number_probabilities = number_counts / len(results)

    # Calculate the probability of winning each color
    color_probabilities = results["color"].value_counts() / len(results)

    # Visualize the results with plots
    plt.figure(figsize=(12, 6))

    # Plot for winning numbers
    plt.subplot(1, 2, 1)
    plt.bar(number_counts.index, number_counts.values)
    plt.title("Frecuencia de números ganadores")
    plt.xlabel("Numero")
    plt.ylabel("Frecuencia")

    # Plot for color probabilities
    plt.subplot(1, 2, 2)
    color_probabilities.plot(kind="bar", color=["red", "black"])
    plt.title("Probabilidad de color ganador")
    plt.xlabel("Color")
    plt.ylabel("Probabilidad")

    plt.tight_layout()
    plt.show()

# Example usage:
if __name__ == "__main__":
    analyze_results()
