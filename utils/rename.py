import os
#path = r'C:\Users\isica\Desktop\gt'
path = r"C:\Users\isica\Desktop\isic_resizing\labels"

count = 0
for filename in os.listdir(path):
    prefix, num, suffix = filename.split('_')
#    num = str(count).zfill(6)
    new_filename = prefix +  "_" + num + ".png"# + "_prediction.png"
    os.rename(os.path.join(path, filename), os.path.join(path, new_filename))
#    count += 1