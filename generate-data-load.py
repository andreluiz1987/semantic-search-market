import csv
import json
import re


def parse_price(price_str):
    match = re.search(r'\$(\d+\.\d+)', price_str)
    if match:
        return float(match.group(1))
    return None


def clean_text(text):
    text = text.replace('\n', ' ').replace('\r', ' ')
    text = re.sub(r'(\d+)\"', r'\1', text)
    return text.strip()


def process_csv_to_json(csv_file_path, json_file_path):
    data_list = []

    with open(csv_file_path, mode='r', encoding='utf-8', ) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for index, row in enumerate(csv_reader, start=1):
            item = {
                "id": index,
                "name": clean_text(row["Title"]),
                "description": clean_text(row["Product Description"].strip()),
                "category": row["Sub Category"],
                "price": parse_price(row["Price"]),
            }
            data_list.append(item)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data_list, json_file, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    csv_file_path = 'files/GroceryDataset.csv'
    json_file_path = 'output.json'
    process_csv_to_json(csv_file_path, json_file_path)

    print(f"JSON file created at {json_file_path}")
