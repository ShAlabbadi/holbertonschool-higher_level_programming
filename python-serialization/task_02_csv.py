#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format and write to data.json.
    
    Args:
        csv_filename: The filename of the input CSV file
        
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Read CSV file
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Write JSON file
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)
            
        return True
    except FileNotFoundError:
        return False
    except Exception as e:
        return False
