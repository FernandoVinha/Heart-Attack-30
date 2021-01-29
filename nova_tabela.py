import csv

 with open('dados_api.csv', 'w', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(["age","gender","height","weight","ap_hi,ap_lo","cholesterol","gluc,smoke","alco","active","cardio"])