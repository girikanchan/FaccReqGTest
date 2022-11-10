import csv

with open('StudentDetailsS.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('StudentDetails.csv','w') as new_file:
        csv_writer = csv.writer(new_file,delimiter = '_')

    for line in csv_reader:
        print(line)
