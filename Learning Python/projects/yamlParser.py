import yaml as yml

with open("D:\\Paddy\\input.txt", 'r', encoding='utf-8') as configFile:
    dataList = configFile.readlines()
    for sentence in dataList:
        result = sentence.replace(" ", "")
        print(result)