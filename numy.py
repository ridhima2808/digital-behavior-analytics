import numpy as np
import csv
insta_minutes = []
study_minutes = []
with open("digital_behaviour.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_minutes.append(int(row["YouTube_Minutes"]))
        study_minutes.append(int(row["Study_Minutes"]))
insta_minutes = insta_minutes[0:7]
study_minutes = study_minutes[0:7]
instagram = np.array(insta_minutes)
study = np.array(study_minutes) 
total_instagram = np.sum(instagram)
total_study = np.sum(study)
#t = instagram.sum()
average_instagram = instagram.mean()
average_study = study.mean()
maximum_instagram = np.max(instagram)
minimum_instagram = np.min(instagram)
maximum_study = np.max(study)
minimum_study = np.min(study)
days_instagram= len(instagram)
days_study = len(study)
print(f"first day value of instagram: {instagram[0]}")
print(f"last day value of instagram:{instagram[-1]}")
print(f"first 3 days of instagram:{instagram[0:3]}")
print(f"last two days of instagram:{instagram[-2:]}")
print(f"first day value of study: {study[0]}")
print(f"last day value of study: {study[0]}")
print(f"first 3 days of study:{study[0:3]}")
print(f"last two days of study:{study[-2:]}")
print(instagram[0:4])
print(instagram[::2])
print(study[0:4])
print(study[::2])
i_hours = instagram/60
s_hours = study/60
diff = instagram - study
i_hours = i_hours.round(2)
s_hours = s_hours.round(2)
# i_boolean = [True if val >100 else False for val in diff] in python, output in boolean
i_boolean = instagram>100 #output in boolean 
iigreater = instagram[i_boolean]
#i_greater = [bool_ for bool_ in boolean if bool_], this is filtering, i_greater will store only True
#if there is an underscore after variable it means that the variable is a keyword and _ is used to avoid confusion.
#i_greater = filter(lambda bool_ : bool_ , i_boolean)
i_greater = instagram[instagram>100]
print(f"igreater = {i_greater}")
print(i_boolean)
print(len(i_greater))
print(iigreater)
'''count = (instagram>100)
print(count)
count = count.sum()
print(count)
count = i_greater.sum()
print(count)'''
count = (instagram>100).sum()
print(count)
a = instagram[instagram>average_instagram]
print(a)
print(average_instagram)
print(instagram)
