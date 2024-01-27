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
        address2_col_index = -1
        for i, entry in enumerate(Addresses.address_row):
            if address1 in entry:
                address1_col_index = i
            
            if address2 in entry:
                address2_col_index = i
            
            if address1_col_index != -1 and address2_col_index != -1:
                break
        
        address1_row_index = -1
        address2_row_index = -1
        for i, entry in enumerate(Addresses.address_col):
            if address1 in entry:
                address1_row_index = i
            
            if address2 in entry:
                address2_row_index = i

            if address1_row_index != -1 and address2_row_index != -1:
                break
        
        """
        The data structure of the distance table is structured such that searching the
        table with one address in the top row and the other in the first column could return 
        a blank value. This is remedied by switching the row and column values.
        """
        if Addresses.address_matrix[address1_row_index][address2_col_index] == '':
            return float(Addresses.address_matrix[address2_row_index][address1_col_index])

        else:
            return float(Addresses.address_matrix[address1_row_index][address2_col_index])
        