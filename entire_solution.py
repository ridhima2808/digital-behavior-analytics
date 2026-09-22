import csv
APP = "Instagram"
minutes = []
with open("digital_behaviour.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        minutes.append(row["Instagram_Minutes"])
        
minutes = minutes[:7]
for i in range(len(minutes)):
    minutes[i] = int(minutes[i])
print(minutes)
total = sum(minutes)
average = total //len(minutes)
highest = max(minutes)
lowest = min(minutes)
cnt = 0
'''for i in range(len(minutes)):
    if(minutes[i]>average):
    '''
for value in minutes:
    if value > average:
        cnt += 1
print(cnt)
print(f"APP:{APP}, TOTAL USAGE : {total}, AVERAGE USAGE : {average}, HIGHEST USAGE:{highest}, LOWEST USAGE:{lowest}, DAYS ABOVE AVG:{cnt}")
