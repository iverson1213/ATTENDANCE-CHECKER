#ATTENDANCE CHECKER PROGRAM
import os
from fuzzywuzzy import fuzz

def normalize_name(name):
    parts = name.split(',')
    if len(parts) > 1:
        last_name = parts[0].strip()
        first_name_parts = parts[1].strip().split()
        if first_name_parts:
            first_name = first_name_parts[0].strip()
            return f"{last_name}, {first_name}"
    return name

def read_names_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            names = set(normalize_name(line.strip()).lower() for line in file)
        return names
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
        return set()

def write_names_to_file(file_path, names):
    with open(file_path, 'w') as file:
        for name in sorted(names):
            file.write(f"{name}\n")

def find_absent_names(roster_file, present_file, absent_file, threshold=85):
    
    roster_names = read_names_from_file(roster_file)
    present_names = read_names_from_file(present_file)

    if not roster_names:
        print("Roster file is empty.")
        return

    print(f"Roster Names: {roster_names}")

    absent_names = set()

    for roster_name in roster_names:
        if not any(fuzz.ratio(roster_name, present_name) >= threshold for present_name in present_names):
            absent_names.add(roster_name)

    print(f"Absent Names: {absent_names}")

    if absent_names:
        write_names_to_file(absent_file, absent_names)
        print(f"Absent names written to {absent_file}.")
    else:
        print("No absent names found.")

directory_path = r'C:\Users\Varassi\Desktop\Studies\QCU-ROTC\Adjutant Duties\Checker' #CHANGE TO UR DIRECTORY :DDDD

roster_male_file = os.path.join(directory_path, 'Roster_Male.txt') #EXISTING FILE WITHIN DIRECTORY
present_male_file = os.path.join(directory_path, 'Present_Male.txt')#EXISTING FILE WITHIN DIRECTORY
absent_male_file = os.path.join(directory_path, 'Absent_Male.txt')#EXISTING FILE WITHIN DIRECTORY IF IT DOES NOT EXIST IT WILL CREATE ONE

roster_female_file = os.path.join(directory_path, 'Roster_Female.txt')#EXISTING FILE WITHIN DIRECTORY
present_female_file = os.path.join(directory_path, 'Present_Female.txt')#EXISTING FILE WITHIN DIRECTORY
absent_female_file = os.path.join(directory_path, 'Absent_Female.txt')#EXISTING FILE WITHIN DIRECTORY IF IT DOES NOT EXIST IT WILL CREATE ONE

os.makedirs(directory_path, exist_ok=True)

find_absent_names(roster_male_file, present_male_file, absent_male_file)

find_absent_names(roster_female_file, present_female_file, absent_female_file)
    