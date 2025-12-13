import pathlib
import os

def create_master_header_report():
    # 1. Determine the Root Directory (where this script is running)
    root_path = pathlib.Path(__file__).parent.resolve()
    
    # 2. define the single output file name
    output_file_name = "MASTER_HEADERS_REPORT.txt"
    output_path = root_path / output_file_name
    
    print(f"--- Starting Master Scan from: {root_path} ---")
    
    found_count = 0
    
    # 3. Open the master file ONE time in Write ('w') mode.
    #    This creates the file if missing, or overwrites it if it exists.
    with open(output_path, "w", encoding="utf-8") as out_f:
        
        # Write a header for the text file itself
        out_f.write(f"Scanned Directory: {root_path}\n")
        out_f.write("="*80 + "\n\n")

        # 4. Recursively find every .csv file using 'rglob' (Recursive Glob)
        #    rglob("*.csv") finds all CSVs in this folder AND all sub-folders
        for csv_path in root_path.rglob("*.csv"):
            
            try:
                # Open the CSV to read the header
                with open(csv_path, "r", encoding="utf-8", errors="replace") as in_f:
                    header = in_f.readline().strip()
                    
                    # 5. Write the Entry:
                    #    Full Path -> Headers
                    out_f.write(f"FILE: {csv_path}\n")
                    out_f.write(f"HEAD: {header}\n")
                    out_f.write("-" * 40 + "\n") # Divider for readability
                    
                    found_count += 1
                    
            except Exception as e:
                # If a file is locked or permission denied, log it inside the text file
                print(f"Error reading: {csv_path.name}")
                out_f.write(f"FILE: {csv_path}\n")
                out_f.write(f"ERROR: Could not read file - {e}\n")
                out_f.write("-" * 40 + "\n")

    print(f"\n--- Scan Complete ---")
    print(f"Total CSVs processed: {found_count}")
    print(f"Master report saved to: {output_path}")

if __name__ == "__main__":
    create_master_header_report()