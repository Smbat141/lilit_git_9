import re
keyword = input('Find: ')
count = int(input("Count: "))
with open('sample_data.csv') as f:
    data = f.read().split(',')
    data = ''.join(data)
    result = re.findall(keyword + r'[ a-zA-Z]{0,}"', data)
    if result:
        for name in result:
            count -= 1
            print(name[0:-1])
            if count == 0:
                break
    else:
        print('Not Found')
        
    
    
    
    