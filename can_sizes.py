"""
Author: Vitor Hugo Santos de Freitas

04 Checkpoint: Variable Scope
"""
import math

# Function to compute the volume of a cylinder
def compute_volume(radius, height):
    return math.pi * radius**2 * height

# Function to compute the surface area of a cylinder
def compute_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)

# Function to compute the storage efficiency of a cylinder
def compute_storage_efficiency(radius, height):
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)
    efficiency = volume / surface_area
    return efficiency

# Function to compute the cost efficiency of a cylinder
def compute_cost_efficiency(volume, cost):
    return volume / cost

# Function to print the results for all can sizes
def main():
    can_sizes = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42),
    ]

    for size, radius, height, cost in can_sizes:
        efficiency = compute_storage_efficiency(radius, height)
        print(f"{size}: {efficiency:.2f}")

if __name__ == "__main__":
    main()
