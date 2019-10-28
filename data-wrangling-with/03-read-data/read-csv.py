import csv

filename = 'data/chp03/data-text.csv'


def read_csv(file):
    csv_file = open(file, "r")
    reader = csv.reader(csv_file)

    for row in reader:
        print(row)


def read_csv_in_dict(file):
    csv_file = open(file, "r")
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row)


read_csv(filename)
read_csv_in_dict(filename)

