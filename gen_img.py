import os

for root, dirs, files in os.walk("public"):
    for file in files:
        if '.jpg' in file:
            print(f'''"/_ipx/_/{root.replace('public/', '')}/{file}",''')