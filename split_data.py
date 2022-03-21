f = open("brown-corpus-tagged-text.txt", "r")
txt = f.read()
split = round(len(txt)*0.8)

split_80 = txt[0:split] # first 80% for training
split_20 = txt[split:] # last 20% for testing

text_file = open("split_80.txt", "w")
text_file.write(split_80)
text_file.close()

text_file = open("split_20.txt", "w")
text_file.write(split_20)
text_file.close()