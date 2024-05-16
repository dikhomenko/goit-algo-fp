import random
import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_simulation(num_simulations):
    sums_count = {i: 0 for i in range(2, 13)}
    
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        dice_sum = die1 + die2
        sums_count[dice_sum] += 1
    
    probabilities = {s: count / num_simulations for s, count in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.figure(figsize=(10, 5))
    plt.bar(sums, probs, color='blue', edgecolor='black')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність сум чисел на двох кубиках (Метод Монте-Карло)')
    plt.xticks(sums)
    plt.grid(True)
    plt.show()

num_simulations = 1000000
probabilities = monte_carlo_simulation(num_simulations)
plot_probabilities(probabilities)

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

print("Ймовірності, отримані методом Монте-Карло:")
for s, p in probabilities.items():
    print(f"Сума {s}: {p:.4f}")

print("\nАналітичні ймовірності:")
for s, p in analytical_probabilities.items():
    print(f"Сума {s}: {p:.4f}")
