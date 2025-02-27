from modulevariant import ModuleVariant

class Main():
    def main():
        with open("alphaTest.txt", "a") as log:
            while True:
                inputData = input()
                x, y = map(float, inputData.split())
                out = (x, y, ModuleVariant.fp(x, y))
                log.write(str(out) + "\n")
                print(str(out)) 




