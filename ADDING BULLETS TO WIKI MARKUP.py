import pyperclip
text=pyperclip.paste() #hi hello 
text='* '+text.replace('\n','\n*')
pyperclip.copy(text)
print(text)
