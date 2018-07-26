import os
path = r'C:\Users\isica\Desktop\gt'

count = 0
for filename in os.listdir(path):
    num, suffix = filename[:-6].split('_')
    num = str(count).zfill(6)
    new_filename = num + "_prediction.png"
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
    count += 1
   