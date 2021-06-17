with open("text with donkey.txt") as f:
    text_read=f.read()
text_read=text_read.replace("donkey","######")
with open ("text with donkey.txt","w") as x:
    x.write(text_read)
