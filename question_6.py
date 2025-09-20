#importing csv module
import csv

#opening csv file
with open("bitsat_cutoff.csv", "r") as f:
    #creating a reader element
    csv_reader = csv.reader(f)

    #setting the pointer to the nect of the heading line
    header =  next(csv_reader)

    #a blank list to store values
    l = []

    for row in csv_reader:
        #storing values and excluding the maximum marks 390 which is at index 3
        l.append(row[:3])

#printing the list
print(l)

d = {}
d_pilani = {}
d_goa = {}
d_hyd = {}

#creating branch vs cutoff for differrent campus
for i in l:
    campus = i[0]
    branch = i[1]
    cutoff = i[2]
    if campus == "Pilani":
        d_pilani[branch] = cutoff
    elif campus == "Goa":
        d_goa[branch] = cutoff
    else:
        d_hyd[branch] = cutoff

#combining them into a single dictionary
d["Pilani"] = d_pilani
d["Goa"] = d_goa
d["Hyderabad"] = d_hyd


print(d)