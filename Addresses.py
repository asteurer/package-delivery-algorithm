import csv

class Addresses:
    address_col = []
    address_row = []
    address_matrix = []

    def __init__(self):
        with open("WGUPS Distance Table.csv") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for i, row in enumerate(reader):
                edited_row = [cell.replace("\n", "") for cell in row]
                if i == 0:
                    Addresses.address_row = edited_row[2:]
                else:
                    Addresses.address_col.append(edited_row[0])
                    Addresses.address_matrix.append(edited_row[2:])

    def calculate_distance(self, address1, address2):
        address1_col_index = -1
        for i, entry in enumerate(Addresses.address_row):
            if address1 in entry:
                address1_col_index = i
                break
        
        address2_row_index = -1
        for i, entry in enumerate(Addresses.address_col):
            if address2 in entry:
                address2_row_index = i
                break

        return Addresses.address_matrix[address2_row_index][address1_col_index]