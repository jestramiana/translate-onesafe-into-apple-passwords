import csv
import sys

# Check if the input file is provided
if len(sys.argv) < 3:
    print("Usage: python3 translate.py <input_file> <output_file>")
    sys.exit(1)
input_file = sys.argv[1]
output_file = sys.argv[2]

# Conversion routine
def convert_onesafe_to_apple(input_file, output_file):
    # Open the oneSafe CSV file for reading
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile, delimiter=';')
        
        # Open the output CSV file for writing
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            fieldnames = ['Name', 'URL', 'Username', 'Password', 'Notes']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)

            # Write the header row
            writer.writeheader()

            # Convert each row from oneSafe to Apple Passwords format
            for row in reader:
                writer.writerow({
                    'Name': row.get('Title', ''),
                    'URL': row.get('URL', ''),
                    'Username': row.get('User Name', ''),
                    'Password': row.get('Password', ''),
                    'Notes': row.get('Note', '')
                })

# Do the conversion
convert_onesafe_to_apple(input_file, output_file)
