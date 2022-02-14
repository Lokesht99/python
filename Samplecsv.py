# import csv
# with open("protagonist.csv","r") as csvfile:
#  data = csv.reader(csvfile, delimiter=' ')
#  for row in data:
#    print(' '.join(row))
# ---------------------------------------------------------------
#
# import csv
# with open("protagonist.csv", "w") as file:
#     writer1 = csv.writer(file)
#     writer1.writerow(["SN", "Movie", "Protagonist"])
#     writer1.writerow([1, "Lord of the Rings", "Frodo Baggins"])
#     writer1.writerow([2, "Harry Potter", "Harry Potter"])
# -------------------------------------------------------------------
# import csv
# with open('protagonist.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# -----------------------------------------------------
# import csv
# csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
#                [2, "Harry Potter", "Harry Potter"],[3, "Hobbit", "Frodo Baggins"],[4, "john", "maharshi"]]
# with open('protagonist.csv', 'w',newline='') as file:
#     writer1 = csv.writer(file)
#     writer1.writerows(csv_rowlist)
# ------------------------------------------------------
# import csv
# with open("protagonist.csv", 'r') as file:
#     csv_file = csv.DictReader(file)
#     for row in csv_file:
#         print(dict(row))
# ------------------------------------------------
import csv
with open('protagonist.csv', 'w', newline='') as file:
    #fieldnames - a list object which should contain the column headers specifying the order in which data should be written in the CSV file
    fieldnames = ['name', 'rating','score']
    write1 = csv.DictWriter(file, fieldnames=fieldnames)
    write1.writeheader() #fieldnames = ['name', 'rating']
    write1.writerow({'name': 'John', 'rating': 2870,'score':344})
    write1.writerow({'name': 'Sam', 'rating': 2822,'score':555})
    write1.writerow({'name': 'Peter', 'rating': 2801,'score':666})
