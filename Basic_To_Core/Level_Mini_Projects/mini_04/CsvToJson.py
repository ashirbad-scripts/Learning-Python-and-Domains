import json
import csv

def convertCsvToJson(csv_file, Json_file):
    try:
        with open(csv_file, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        with open(Json_file, "w") as file:
            json.dump(data, file, indent=4)
        
        print("Csv Data Saved in Json file")
    
    except FileNotFoundError as e:
        print("Error message: ",e)

csvDirectory = "Level_11 (Mini_Projects)/mini_04/data.csv"
jsonDirectory = "Level_11 (Mini_Projects)/mini_04/data.json"
convertCsvToJson(csvDirectory, jsonDirectory)