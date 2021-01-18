import time
import os

dir = input("wprowadź katalog:")

if not os.path.isdir(dir):
    print("%s must be a directory" % dir)
else:
    file = input("Wprowadź nazwę pliku:")
    path = os.path.join(dir, file)
    if not os.path.exists(path):
        print("plik nie istieje")
    else:
        print("wlasciwosci pliku:")
        print("data modyfikacji: ", time.localtime(os.path.getmtime(path)))
        print("wielkość pliku: ", os.path.getsize(path))
        print("sciezka bezwzgledna:", os.path.abspath(path))
        print("bierzący katalog:", os.path.dirname(path))


#############################################

import datetime
import os

##########sprawdzenie istnienia katalogow i plikow ########

data_input_catalog = "c:\\temp\\data_input"
data_output_catalog = "c:\\temp\\data_output"

today = datetime.date.today()

today_output_catalog = os.path.join(data_output_catalog, today.strftime("%Y-%m-%d"))

# wejsciowy katalog musi istnieć
is_input_catalog_ok = os.path.isdir(data_input_catalog)

# wyjsciowy katalog musi istnieć
is_output_catalog_ok = os.path.isdir(data_output_catalog)

# katalog lub plik z data dzisiejszą nie istnieje
is_today_output_catalog_ok = not (os.path.isdir(today_output_catalog)) and not (os.path.isfile(today_output_catalog))

if is_input_catalog_ok and is_output_catalog_ok and is_today_output_catalog_ok:
    print("Warunki spełnione, katalogi istnieją, można kontynuować")
else:
    print("Bład")

    ##display detailed error conditions
    if not is_input_catalog_ok:
        print("Input catalog %s musi istnieć!" % data_input_catalog)
    if not is_output_catalog_ok:
        print("Output catalog %s musi istnieć!" % data_output_catalog)
    if not is_today_output_catalog_ok:
        print("Today's output %s nie może istniec (ani jako plik ani jako katalog)!" % today_output_catalog)

################ odczyt danych z pliku#########


file_path = "C:\\temp\\data_input\\orders.csv"

# file = open(file_path)
# for line in file.readlines():
# print(line)

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')

        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0], order[1], order[2]))
    else:
        print("Line %s malformed!!!" % line)
file.close()

############# zapis danych do pliku ############

webaddresses = []c

line = input("wprowadż adres strony www: ")

while line:
    webaddresses.append(line)
    line = input("wprowadż adres strony www: ")

dirname = os.getcwd()

filname = input("podaj nazwe pliku:")

filepath = os.path.join(dirname, filname)

file = open(filepath, "w")

for wpis in webaddresses:
    file.write(wpis + "\n")

file.close()


