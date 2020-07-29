"""
This python file reads the csv file under input directory and outputs related data analysis into output directory
"""

import csv
from collections import defaultdict
import sys

__author__ = 'Meiqi Wang'

#read_csv function reads the csv file and convert the data into a dictionary, the dictionary stores products
#, year, company and the complaints each company received
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
            #count the number of complaints each company received each year for each product
            pro_dict[product][year][company] += 1

    return pro_dict

#write_csv function loops through the dictionary returned from read_csv function, does some calculation
#and writes the fields into the output csv file
def write_csv(dict, filename):
    with open(filename, mode='w') as f:
        f_writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        #fieldnames = ['product', 'year', 'total number of complaints', 'total number of companies', 'highest percentage of complaints against one company']
        #f_writer.writerow(fieldnames)
        for pro, v in sorted(dict.items()):
            for year, comps in sorted(v.items()):
                #add up the total number of complaints of the product in the year
                total = sum(comps.values())
                #get the number of companies that received the complaint
                comp_total = len(comps)
                #calculate the highest percentage of total complaints filed against one company
                p = round(float(max(comps.values())) / total, 2)
                percent = int(p * 100)
                f_writer.writerow([pro, year, total, comp_total, percent])


if __name__ == '__main__':
    input = sys.argv[1]
    output = sys.argv[2]
    dict = read_csv(input)
    write_csv(dict, output)