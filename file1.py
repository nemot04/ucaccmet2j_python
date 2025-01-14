import json


with open('precipitation.json', 'r') as file:
    data = json.load(file)

#CSV loading Seattle
seattle=[]
for key in data:
    if key['station']=='GHCND:US1WAKG0038':
        seattle.append(key)

#total precipitation months
months=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
precipitation_month=[]
results_precipitation={}
total_precipitation_year=0

for month in months:
    total_monthly_precipitation=0
    for key in seattle:
        if key['date'] >= f'2010-{month}-01' and key['date'] <= f'2010-{month}-31':
            precipitation_month.append(key['value'])
            total_monthly_precipitation=total_monthly_precipitation + key['value']
            total_precipitation_year=total_precipitation_year+ total_monthly_precipitation
    print(f'{month}', total_monthly_precipitation)
    results_precipitation[month]={'total_monthly_precipiation': total_monthly_precipitation}


list_total_monthly_precipitation= {'{month}}': '{total_monthly_precipitation}'}
print(list_total_monthly_precipitation)
with open('results_precipitation.json', 'w')as file:
    json.dump(results_precipitation, file, indent=4)
print(total_precipitation_year)