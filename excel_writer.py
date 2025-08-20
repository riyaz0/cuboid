
import pandas as pd
from architecture import calculate_cuboid_architecture

def save_coordinates_to_excel(file_name, coordinates):
 
    try:
   
        df = pd.DataFrame(coordinates, columns=['x', 'y', 'z'])

     
        df.to_excel(file_name, index=False)
        print(f"Successfully saved all 10,000 brick coordinates to '{file_name}'.")
    
    except ImportError:
        print("Error: The 'pandas' or 'openpyxl' library is not installed.")
        print("Please install it by running: pip install pandas openpyxl")
    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    total_bricks_count = 10000
    brick_dims = (200, 100, 100)  
    excel_file_name = "brick_coordinates.xlsx"

   
    print("Getting brick coordinates from the architecture module...")
    architecture_data = calculate_cuboid_architecture(total_bricks_count, brick_dims)
    all_coordinates = architecture_data['brick_coordinates']
    

    save_coordinates_to_excel(excel_file_name, all_coordinates)
    

    print("\nYou can now open the Excel file to view the data.")
