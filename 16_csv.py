#CSV format

import csv
# import pandas as pd 

#read csv file usinf csv or panda 
# to install pandas >>pip3 install pandas
def read_csv_read(name):
    with open(name) as f:
        read = csv.reader(f, delimiter=",")
        for row in read:
            print(row) # can add index to read only one index [1]

#read csv with csv.Dictreader
def read_csv_dic(name):
    with open(name) as f:
        dictreader = csv.DictReader(f, delimiter=",")
        for row in dictreader:
            print(f'{row["monsterName"]} is price {row["price"]}')



# read csv with panda module
#ToDo cant import panda to be cheked >>>>>>>
# def read_csv_pandas(name):
# 	df = pd.read_csv(name)
# 	print(df)        


def write_to_csv(file):
    with open(file, 'w') as f:
        writer = csv.writer(f) #create object
        writer.writerow(["ID", "Category", "Name", "Quantity", "Price"])
        writer.writerow([41, "Furnishings", "Office Chair", 10, 85])
        writer.writerow([20, "Office Supplies", "Pens", 30, 10])
        writer.writerow([13, "Housekeeping", "Bed Sheet (Double)", 15, 20])

#add new row in existing csv file under header 
def wrire_to_csv_dictionary(file):
    with open(file, 'a') as f:
        header = ['id', 'category', 'name','quantity', 'price']
        writer = csv.DictWriter(f, fieldnames=header)
        item = {'id':65, 'category': 'maintenance', 'name':'ladder', 'quantity':33, 'price':50}
        writer.writerow(item)



# read_csv_read('Files/monsters.csv')
read_csv_dic('Files\monsters.csv')
# write_to_csv('Files/products.csv')
# # read_csv_read('Files/products.csv')
# wrire_to_csv_dictionary('Files/products.csv')
# read_csv_read('Files/products.csv')