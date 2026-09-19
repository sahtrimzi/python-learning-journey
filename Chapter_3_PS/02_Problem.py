# Program to fill the letter template from image.png[cite: 1]
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Sonny").replace("<|Date|>", "27 December 2024"))