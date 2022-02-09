from urllib.request import urlopen

if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

    test = urlopen(url)
    test = test.read().decode().replace('\r', '').replace('-', '').replace('.', '').replace(',', '').replace("'", '').split('\n')

    wordle_list = []
    for text in test:
        if len(text) == 6:
            wordle_list.append(text)

    with open('words.txt', 'w') as f:
        for item in wordle_list:
            print("Writing: ", item.lower())
            f.write("%s\n" % item.lower())

