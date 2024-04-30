import csv

""" Open the Bestseller - Sheet1.csv file in "read" mode.
Use the CSV reader to navigate through the data and find the book with the highest sales, via the sales in millions column.
Create a new file called bestseller_info.csv with the CSV writer.
In the new file, use .writerow() to add new CSV data. """

#abrir el CSV en modo lectura
with open("Bestseller - Sheet1.csv", "r", encoding="utf-8") as file:
    #leer el archivo
    csv_reader = csv.reader(file)
    #omitir la primera fila que contiene los encabezados
    next(csv_reader)
    #declarar variable de ventas mas altas
    highest_sales = 0
    #recorrer la lista de datos
    for row in csv_reader:
        current_sales = int(row[4])
        if current_sales > highest_sales:
            highest_sales = current_sales
            bestseller_info = row
    print(bestseller_info)

#crear un nuevo archivo CSV
with open("bestseller_info.csv", "w", newline="", encoding="utf-8") as file:
    #crear un escritor de CSV
    csv_writer = csv.writer(file)
    #escribir la fila con los datos del libro con mas ventas
    csv_writer.writerow(bestseller_info)