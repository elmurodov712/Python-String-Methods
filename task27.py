text = input('text: ')

result = text.endswith('.pdf') or text.endswith('.docx') or text.endswith('.txt')

print(result)