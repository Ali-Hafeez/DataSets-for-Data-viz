import os
import pathlib
import pandas as pd

def recursive_excel_to_csv_converter():
    # 1. Start exactly where the script is located
    start_path = pathlib.Path(__file__).parent.resolve()
    print(f"--- Starting Converter from: {start_path} ---\n")

    # Defined list of Excel extensions to look for
    excel_extensions = {'.xlsx', '.xls', '.xlsm', '.xlsb'}
    
    converted_count = 0
    errors = []

    # 2. Walk through the directory tree
    for root, dirs, files in os.walk(start_path):
        current_folder = pathlib.Path(root)
        
        # Check every file in the current folder
        for filename in files:
            file_path = current_folder / filename
            suffix = file_path.suffix.lower()

            # 3. If file is an Excel file
            if suffix in excel_extensions:
                # Create the new filename: same name but with .csv extension
                # e.g., 'fig_4.xlsx' -> 'fig_4.csv'
                new_csv_filename = file_path.stem + ".csv"
                new_csv_path = current_folder / new_csv_filename

                # Skip if the CSV already exists (optional, saves time)
                if new_csv_path.exists():
                    print(f"Skipping (CSV exists): {filename}")
                    continue

                try:
                    print(f"Converting: {filename} -> {new_csv_filename} ...")
                    
                    # 4. Use Pandas to read the Excel file
                    # By default, this reads the FIRST sheet only.
                    df = pd.read_excel(file_path)
                    
                    # 5. Save as CSV
                    # index=False removes the row numbers (0,1,2) on the left
                    # encoding='utf-8' ensures special characters work
                    df.to_csv(new_csv_path, index=False, encoding='utf-8')
                    
                    converted_count += 1
                    
                except Exception as e:
                    error_msg = f"Failed to convert {filename}: {e}"
                    print(f"  [ERROR] {error_msg}")
                    errors.append(error_msg)

    print(f"\n--- Conversion Complete ---")
    print(f"Total files converted: {converted_count}")
    if errors:
        print(f"Total errors: {len(errors)}")
        print("First few errors:", errors[:3])

if __name__ == "__main__":
    recursive_excel_to_csv_converter()