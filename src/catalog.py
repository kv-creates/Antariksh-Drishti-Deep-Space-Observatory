import csv
def load(path='data/targets.csv'):
    with open(path) as f:
        return list(csv.DictReader(f))
