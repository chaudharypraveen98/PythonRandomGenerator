import datetime

def randon_no():
    seconds_since_epoch = datetime.datetime.now().timestamp()
    no = int(seconds_since_epoch)
    return no%10

if __name__ == '__main__':
    print(randon_no())