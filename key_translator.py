# E F G A B C D
# C D E F G A B

rf = open('./dark_souls_theme.txt', 'r')
wf = open('./dark_souls_theme_translated.txt', 'w')
chars = ['E', 'F', 'G', 'A', 'B', 'C', 'D']
for line in rf:
    for char in line:
        if char == 'E':
            wf.write('C')
        elif char == 'F':
            wf.write('D')
        elif char == 'G':
            wf.write('E')
        elif char == 'A':
            wf.write('F')
        elif char == 'B':
            wf.write('G')
        elif char == 'C':
            wf.write('A')
        elif char == 'D':
            wf.write('B')
        else:
            wf.write(char)
rf.close()
wf.close()
