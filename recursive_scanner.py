import os
import pathlib

def scan_directories_and_extract_headers():
    # 1. Define where the script is running (The "Root" of the scan)
    start_path = pathlib.Path(__file__).parent.resolve()
    print(f"--- Starting Scan from: {start_path} ---\n")

    # 2. 'os.walk' travels through the directory tree step by step
    # 'root' is the current folder looking being at
    # 'dirs' are the subfolders inside it
    # 'files' are the filenames inside it
    for root, dirs, files in os.walk(start_path):
        
        # Create a Path object for the current folder (makes it easier to handle windows/mac paths)
        current_folder = pathlib.Path(root)
        
        # 3. Find only the CSV files in this specific current folder
        # We perform a check to make sure the file name actually ends with .csv
        current_csvs = [f for f in files if f.lower().endswith('.csv')]

        # 4. If CSVs exist in this folder, do the work
        if current_csvs:
            print(f"Files found in: .../{current_folder.name}")
            
            output_file_path = current_folder / "output.txt"
            
            try:
                with open(output_file_path, "w", encoding="utf-8") as out_f:
                    for filename in current_csvs:
                        full_csv_path = current_folder / filename
                        
                        try:
                            # Read JUST the first line (Safety: Read-only mode 'r')
                            with open(full_csv_path, "r", encoding="utf-8", errors="replace") as in_f:
                                header = in_f.readline().strip()
                                # Save: "filename.csv: The Header Data"
                                out_f.write(f"{filename}: {header}\n")
                        except Exception as e:
                            print(f"  [Error] Could not read {filename}: {e}")
                
                print(f"  -> Generated: output.txt (Entries: {len(current_csvs)})")
            
            except Exception as e:
                print(f"  [Error] Could not create output file in {current_folder.name}: {e}")

    print("\n--- Scan Complete ---")

if __name__ == "__main__":
    scan_directories_and_extract_headers()