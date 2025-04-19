from first import process_text

text = ''
with open("text1.txt", "r") as file:
    text = file.read()


res = process_text(text)


print(res['word_lengths'].count(4) + \
      res['word_lengths'].count(3) + \
        res['word_lengths'].count(2) + \
            res['word_lengths'].count(1))