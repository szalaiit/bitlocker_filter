import csv


with open('bitlocker.csv', 'r') as csv_file:
    with open('output.csv', 'a') as output_file:
        reader = csv.reader(csv_file)
        next(reader, None)
        next(reader, None)
        for row in reader:
            name = row[0:1]
            hostname = str(name[0])[70:84]
            date = str(name[0])[3:13] + " " + (name[0])[14:22]
            passwd = row[1:2]
            key = str(passwd[0:1])[2:-2]
            output_file.write(date + ',')
            output_file.write(hostname + ',')
            output_file.write(key + ',' + '\n')
csv_file.close()