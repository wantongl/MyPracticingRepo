import csv

# Practicing with CSV
# Requirement:
# Create a new csv file and fill it with information from data.
# Read from that new csv file and use the data to create another new CSV file containing SUM(QTY) and SUM(AMT).
# SUM(QTY) shows the total quantity for each Symbol shown in data.
# SUM(AMT) shows the total (quantity * price) for each symbol shown in data.

data = [["Symbol","Quantity","Price"],
        ["MCF",10,20],
        ["APPL",5,30],
        ["MCF",10,15],
        ["RAN",2,9],
        ["MCF",50,5]
        ]

with open("csvtest.csv",'w+',newline="") as file:
    writer = csv.writer(file,delimiter=',')
    for i in data:
        writer.writerow(i)


with open("csvtest.csv","r") as file:
    reader = csv.DictReader(file,delimiter=',')
    sumQTY = {}
    sumAMT = {}

    for i in reader:
        if i["Symbol"] not in sumQTY:
            sumQTY[i["Symbol"]] = int(i["Quantity"])
        else:
            sumQTY[i["Symbol"]] += int(i["Quantity"])

        if i["Symbol"] not in sumAMT:
            sumAMT[i["Symbol"]] = (int(i["Quantity"]) * int(i["Price"]))
        else:
            sumAMT[i["Symbol"]] += (int(i["Quantity"]) * int(i["Price"]))

    print("Sum(QTY): ")
    for i in sumQTY:
        print(i, sumQTY[i])

    print("Sum(AMT): ")
    for i in sumAMT:
        print(i, sumAMT[i])


    with open("csvtestresult.csv", 'w+', newline="") as file:
        writer = csv.writer(file, delimiter=",")
        writer.writerow(["Symbol","Sum(QTY)","Sum(AMT)"])
        for i in sumQTY:
            writer.writerow([i,sumQTY[i],sumAMT[i]])

    # for i in reader
    # is a iterator that goes through the file like sys.stdin.readlines
    # need to use seek(0) to go back to the beginning of the line
    # reader.seek(0)