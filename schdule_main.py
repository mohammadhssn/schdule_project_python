import main
import time


def show(name):
    print('this is methode show' + name)


def welcome():
    print('welcome')


main.every(6).seconds.do(show, 'sara')
main.every().hours.at(':18').do(welcome)

while True:
    main.run_pending()
    time.sleep(1)

