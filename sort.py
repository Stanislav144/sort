import csv
def sorting():
    with open('employees.csv', encoding="utf-8") as data:
        # sorted_data = sorted(data, key = lambda r: r[1])
        read_list = csv.reader(data)
        # sorted_data = sorted(read_list, key=lambda row: int(row[0]))
        sorted_data = sorted(read_list, key=lambda row: row[0])
        for item in sorted_data:
            print(item)
