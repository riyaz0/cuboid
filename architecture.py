# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 17:51:14 2025

@author: riyaz
"""

# architecture.py
import csv
from io import StringIO

def calculate_cuboid_architecture(total_bricks, brick_dimensions):
   
    brick_length, brick_width, brick_height = brick_dimensions


    num_bricks = {
        "x": 25,
        "y": 20,
        "z": 20
    }


    final_length_m = (num_bricks["x"] * brick_length) / 1000.0
    final_width_m = (num_bricks["y"] * brick_width) / 1000.0
    final_height_m = (num_bricks["z"] * brick_height) / 1000.0


    brick_coordinates = []
    for z in range(num_bricks["z"]):
        for y in range(num_bricks["y"]):
            for x in range(num_bricks["x"]):
                # Calculate the center point of each brick
                x_coord = (x + 0.5) * brick_length
                y_coord = (y + 0.5) * brick_width
                z_coord = (z + 0.5) * brick_height
                brick_coordinates.append((x_coord, y_coord, z_coord))

    return {
        "num_bricks": num_bricks,
        "final_dimensions": (final_length_m, final_width_m, final_height_m),
        "location": "On a flat, level surface.",
        "orientation": "The largest face (5.0m x 2.0m) is the base for maximum stability.",
        "brick_coordinates": brick_coordinates
    }

def convert_coordinates_to_csv(coordinates):

    output = StringIO()
    writer = csv.writer(output)
    writer.writerow(['x', 'y', 'z'])  
    writer.writerows(coordinates)    
    return output.getvalue()


if __name__ == "__main__":
    total_bricks_count = 10000
    brick_dims = (200, 100, 100)  


    result = calculate_cuboid_architecture(total_bricks_count, brick_dims)
    all_coordinates = result['brick_coordinates']


    csv_output = convert_coordinates_to_csv(all_coordinates)


    print("--- Cuboid Architecture Output ---")
    print(f"Final Cuboid Dimensions: {result['final_dimensions']}")
    print(f"Location: {result['location']}")
    print(f"Orientation: {result['orientation']}")
    print(f"Total Bricks: {len(all_coordinates)}")
    
    print("\n--- CSV Output for Excel ---")
    print("Copy the following text and paste it into an Excel spreadsheet:")
    print("-" * 50)
    print(csv_output)
    print("-" * 50)