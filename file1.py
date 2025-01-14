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
        results_precipitation[month]={'total_monthly_precipiation': total_monthly_precipitation}


relative_precipitation_results={}
total_precipitation_year=sum(precipitation_month)
for month in months:
    total_monthly_precipitation=0
    for key in seattle:
        if key['date'] >= f'2010-{month}-01' and key['date'] <= f'2010-{month}-31':
            precipitation_month.append(key['value'])
            total_monthly_precipitation=total_monthly_precipitation + key['value']
        results_precipitation[month]={'total_monthly_precipiation': total_monthly_precipitation}
        relative_precipitation=total_monthly_precipitation/total_precipitation_year
    print('relative_precipitation', f'{month}',relative_precipitation)
    relative_precipitation_results[month]={'monthly_relative_precipitation': relative_precipitation}

results={'results_precipitation': results_precipitation, 'relative_precipitation_results': relative_precipitation_results}


print('total_precipitation_year', total_precipitation_year)

with open('results_precipitation.json', 'w')as file:
    json.dump(results, file, indent=4)
