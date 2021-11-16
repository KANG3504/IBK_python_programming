def file_read(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lyric = file.read()
        return lyric


read = file_read("yesterday.txt")
print(read)
ans = read.upper().count("YESTERDAY")
print("Number of Yesterday is {}".format(ans))
ans1 = read.lower().count("yesterday")
print("Number of Yesterday is {}".format(ans1))
'''
f = open("yesterday.txt", 'r')
data = f.read()
f.close()
ans = data.count("Yesterday")
ans += data.count("yesterday")
print(ans)
'''
'''
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()
'''

'''
s = " Hello World  "
print(len(s))
print(s[1].upper())
print(s.count('e'))
print(s.strip())
ss = s.replace(" ",'')
print(ss)
'''