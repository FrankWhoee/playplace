f = open("co2_emissions_per_person.csv", "r")
data_set = f.readlines()
data_list = []
for dlu in data_set:
    data_list.append(dlu.split(","))

print(data_list[0])
print(data_list[57])