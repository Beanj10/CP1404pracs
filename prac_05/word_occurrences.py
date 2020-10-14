sentence = input(str('Text: '))
words = sentence.split(" ")
print(words)

output = {}

for word in words:
    if word not in output:
        count = words.count(word)
        output.update({word: count})

sorted_output = sorted(output)

for word in sorted_output:
    print("{:5} : {}".format(word, output[word]))

