import string

def read(path: str) -> str:
    with open(path, "r") as file:
        return file.read().split('\n')
    
def parse(data: list) -> dict:
    res = []
    for _ in data:
        flag = 0
        for letter in _:
            if letter in string.punctuation + ' ':
                flag += 1
        if flag == 0:
            res.append(_)
    return {_: (Counter(''.join(data), _), ''.join(data).index(_)) for _ in set(res)}


def Counter(data: str, val: str) -> int:
    return data.count(val)

dct = parse(read("text2.txt"))
srt = sorted(dct.items(), key=lambda x: x[1][0], reverse=True)
print(srt)

with open('result.txt', 'w') as file:
    for i in srt:
        file.write(str(i) + '\n')