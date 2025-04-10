import csv
import requests
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

filename = './Task_2/Task 2 - Intern.csv'
errors = []

if not os.path.exists(filename):
    print(f"Error: The file '{filename}' does not exist in the current directory.")
else:
    try:
        with open(filename, 'r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                url = row['urls']
                try:
                    response = requests.get(url, headers=headers, timeout=5)
                    print(f"({response.status_code}) {url}")
                except requests.exceptions.RequestException as e:
                    errors.append((url, str(e)))
                    print(f"(ERROR) {url}")
    except Exception as e:
        print(f"An error occurred while processing the file: {str(e)}")

# Writing detailed errors to a file
if errors:
    with open('./Task_2/error_details.txt', 'w', encoding='utf-8') as f:
        f.write("URL,Error\n")
        for url, error in errors:
            f.write(f'"{url}","{error}"\n')
    print("\nMore details on error URLs can be found in 'error_details.txt'.")