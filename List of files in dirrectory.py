import os
for root, dirs, files in os.walk(r'type the dirrectory here'):
    for name in files:
        fullname = os.path.join(root, name)
        print(fullname)
