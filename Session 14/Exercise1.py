strippable = string.punctuation + string.whitespace

for word in doc.split:
    word = word.strip(stripple)
    word = word.lower()
    print(word)

if skip_header:
    skip_gutenberg_header(fp)

for line in fp:
    if line.startswith('***END OF THIS PROJECT'):
        break
    
for word in line.split():


return len(list)
