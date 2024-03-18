import requests

def main():
    r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    [print(i) for i in r.__dir__()]

if __name__ == "__main__":
    main()
