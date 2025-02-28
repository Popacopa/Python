from modulevariant import fp

def main():
    with open("alphaTest.txt", "a") as log:
        while True:
            inputData = input()
            x, y = map(float, inputData.split())
            out = (x, y, fp(x, y))
            log.write(str(out) + "\n")
            print(str(out))

if __name__ == "__main__": main() 




