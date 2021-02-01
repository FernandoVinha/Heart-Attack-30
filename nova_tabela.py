import csv

with open('dados_api.csv', 'w', newline='') as csvfile:
    fieldnames = ['age', 'gender', 'height', 'weight', 'ap_hi,ap_lo', 'cholesterol', 'gluc','gluc', 'smoke', 'alco', 'active', 'cardio']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow(['18393','2','168','62.0','110,80','1','1','0','0','1,0'])