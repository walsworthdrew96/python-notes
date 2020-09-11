import os

for (root, subs, files) in os.walk('.'):
    for name in files:
        print(root, name)
