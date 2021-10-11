def read_file(filename):
    lines = []
    with open(filename, 'r',encoding='utf-8-sig') as f:    
        for line in f:
            lines.append(line.strip())
    return lines
            
            
            
            
def convers_file(lines):
    message = []
    for line in lines:        
        if line == 'Allen':
            name = 'Allen'
            continue
        elif line == 'Tom':
            name = 'Tom'
            continue
        if name:
            message.append(name + ': '+ line)
    return message

def write_file(filename,lines):
    with open(filename, 'w',encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')    
        

lines = read_file('input.txt')
lines = convers_file(lines)
write_file('output.txt',lines)


            