def create_txtfile():
    rm = open("README.txt", 'w')
    rm.write(" this is a text file")
    rm.close()

create_txtfile()