import csv
from collections import defaultdict
import sys

def read_csv(filename):
    pro_dict = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header_dict = {}
        headers = next(csv_reader)
        for i, header in enumerate(headers):
            header_dict[header.strip().lower()] = i
        for row in csv_reader:
            product = row[header_dict['product']].strip().lower()
            year = row[header_dict['date received']].split("-")[0]
            company = row[header_dict['company']].strip().upper()
            pro_dict[product][year][company] += 1
    #print(pro_dict)
    return pro_dict

def write_csv(dict, filename):
    with open(filename, mode='w') as f:
        f_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        #fieldnames = ['product', 'year', 'total number of complaints', 'total number of companies', 'highest percentage of complaints against one company']
        #f_writer.writerow(fieldnames)
        for pro, v in sorted(dict.items()):
            for year, comps in sorted(v.items()):
                total = sum(comps.values())
                comp_total = len(comps)
                p = round(float(max(comps.values())) / total, 2)
                percent = int(p * 100)
                f_writer.writerow([pro, year, total, comp_total, percent])


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    dict = read_csv(input)
    write_csv(dict, output)
    #dict = read_csv('../insight_testsuite/test_1/input/complaints.csv')
    #write_csv(dict, '../insight_testsuite/test_1/output/report.csv')