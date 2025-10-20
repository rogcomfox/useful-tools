import requests

if __name__ == '__main__':
    url_test = 'https://firebasestorage.googleapis.com/v0/b/dgscope-b5a0a.appspot.com/o/recording%2F0XaR0b9syDP14PluJzufRvwFG2P2%2F9KPryMPaW5TRyzTBewkD_Ccc?alt=media&token=4acadc23-d41d-47de-a89d-50e09e3a9e99'
    response = requests.get(url_test)
    open('try.mp3', 'wb').write(response.content)