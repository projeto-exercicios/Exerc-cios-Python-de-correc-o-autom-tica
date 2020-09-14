
def format_string(string):
    counter = 0
    final_string = []
    complexity = 0
    for i in range(len(string)):
        if counter > 1:
            counter -=1
            continue
        if '[' in string[i]:
            text = ''
            nString = string[i:]
            for o in nString:
                counter +=1
                if '[' in o:
                    complexity += 1
                if ']' in o and complexity > 0:
                    complexity -= 1
                if ']' in o and complexity == 0:             
                    text += o
                    break
                text += o + ' '  
            final_string.append(text)
            continue
        if '(' in string[i]:
            text = ''
            nString = string[i:]
            for o in nString:
                counter +=1
                if '(' in o:
                    complexity += 1
                if ')' in o and complexity > 0:
                    complexity -= 1
                if ')' in o and complexity == 0:             
                    text += o
                    break
                text += o + ' '  
            final_string.append(text)
            continue
        if '{' in string[i]:
            text = ''
            nString = string[i:]
            for o in nString:
                counter +=1
                if '{' in o:
                    complexity += 1
                if '}' in o and complexity > 0:
                    complexity -= 1
                if '}' in o and complexity == 0:             
                    text += o
                    break
                text += o + ' '  
            final_string.append(text)
            continue
        final_string.append(string[i])
    return final_string

