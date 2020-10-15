import time


def progress(count, total):
    bar_len = 100
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '█' * filled_len + '░' * (bar_len - filled_len)

    return '%s' % (bar)


print('My Console Loading Bar...')
for x in range(101):
    print(progress(x, 100), end='')
    time.sleep(0.1)
    print('', end='\r')
