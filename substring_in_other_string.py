def twoStrings(s1, s2):
    if len(s1) > len(s2):
        smaller = s2
        bigger = s1
    else:
        smaller = s1
        bigger = s2
    for size in range(1, len(smaller)+1):
        print(f'SIZE: {size} =========================================')
        for start_pos in range(len(smaller)-size+1):
            print(smaller[start_pos:start_pos+size])
            if smaller[start_pos:start_pos+size] in bigger:
                #return 'YES'
                pass
    return 'NO'

print(twoStrings('asdfasdfasdf', 'aksldfjlsakfjasdfasjdflksjadfl'))