import random
import time

def objective_function(x):
    return -(x-2)**2 + 5

def generate_neighbour(current_solution, step_size=0.1):
    return current_solution + (random.random() * 2 - 1) * step_size

def hill_climbing(max_iterations=1000, step_size=0.1):
    current_solution = random.uniform(-10,10)
    current_value = objective_function(current_solution)

    for _ in range(max_iterations):
        neighbour = generate_neighbour(current_solution, step_size)
        neighbour_value = objective_function(neighbour)

        if neighbour_value > current_value:
            current_solution, current_value = neighbour, neighbour_value

    return current_solution, current_value

best_x , best_val = hill_climbing()
print("Best solution found: x=", best_x, "value =", best_val)
