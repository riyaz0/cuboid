
"""
Created on Wed Aug 20 17:58:15 2025

@author: riyaz
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

def visualize_cuboid_3d(brick_coords):
    """
    Visualizes the cuboid in 3D using the brick coordinates.

    Args:
        brick_coords (np.array): A NumPy array of brick coordinates.
    """

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')


    ax.scatter(brick_coords[:, 0], brick_coords[:, 1], brick_coords[:, 2], s=1, c='red', alpha=0.5)


    ax.set_xlabel('Length (mm)')
    ax.set_ylabel('Width (mm)')
    ax.set_zlabel('Height (mm)')
    ax.set_title('3D Cuboid Visualization (10,000 Bricks)')

    
    ax.set_xlim(0, 5000)
    ax.set_ylim(0, 2000)
    ax.set_zlim(0, 2000)

    plt.show()

def visualize_top_view(brick_coords):

    fig, ax = plt.subplots(figsize=(8, 8))
    
    
    ax.scatter(brick_coords[:, 0], brick_coords[:, 1], s=1, c='red', alpha=0.5)
    
    ax.set_title('Top View')
    ax.set_xlabel('Length (mm)')
    ax.set_ylabel('Width (mm)')
    

    ax.set_xlim(0, 5000)
    ax.set_ylim(0, 2000)
    
    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()

def visualize_side_view(brick_coords):
 
    fig, ax = plt.subplots(figsize=(8, 8))
    
  
    ax.scatter(brick_coords[:, 0], brick_coords[:, 2], s=1, c='red', alpha=0.5)
    
    ax.set_title('Side View')
    ax.set_xlabel('Length (mm)')
    ax.set_ylabel('Height (mm)')
    

    ax.set_xlim(0, 5000)
    ax.set_ylim(0, 2000)

    ax.set_aspect('equal', adjustable='box')
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    try:

        df = pd.read_excel('brick_coordinates.xlsx')
        
   
        brick_coordinates = df[['x', 'y', 'z']].values
        
        
        visualize_cuboid_3d(brick_coordinates)
        visualize_top_view(brick_coordinates)
        visualize_side_view(brick_coordinates)
        
    except FileNotFoundError:
        print("Error: 'brick_coordinates.xlsx' file not found.")
        print("Please ensure the Excel file is in the same directory as this script.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")