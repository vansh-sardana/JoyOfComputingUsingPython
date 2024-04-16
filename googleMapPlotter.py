from gmplot import gmplot
import csv
lat= 28.463161
lng= 77.015771
gmap= gmplot.GoogleMapPlotter(lat,lng,18)
gmap.marker(lat,lng, "blue")
with open("coordinates.csv", "r") as f:
    data= csv.reader(f)
    for row in data:
        lat= float(row[0])
        lng= float(row[1])
        gmap.marker(lat,lng, "yellow")
        
gmap.marker(lat,lng, "red")
gmap.draw("mymap.html")