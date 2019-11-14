import os

files = os.listdir('./')

fc = 0
for i in range(len(files)):
    phrase = ","
    count = 0
    with open(files[i], 'r') as f:
        for j in f:
            if phrase in j:
                count += 1
    print(count)
    if count > 1:
        os.rename(files[i], f"Data.csv {fc}.csv")
        fc += 1