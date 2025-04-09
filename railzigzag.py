def decode(text, rows):
    length = len(text)
    result = [''] * length
    position = 0
    
    for row in range(rows):
        step = 2 * (rows - 1)
        if row > 0:
            step -= 2 * row
        place = row
        
        while place < length:
            result[place] = text[position]
            position += 1
            if row > 0 and row < rows - 1 and place + step < length:
                result[place + step] = text[position]
                position += 1
            place += 2 * (rows - 1)
    
    return ''.join(result)

message = ''
for num in range(3, 15):
    print(decode(message, num))
