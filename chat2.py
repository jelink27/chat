def read_file(filename):
    lines = []
    with open(filename, 'r',encoding='utf-8-sig') as f:    
        for line in f:
            lines.append(line.strip())
    return lines           
   
            
def convers_file(lines):
    allen_word_count = 0
    viki_word_count = 0
    allen_sticker_count = 0
    viki_sticker_count = 0
    allen_image_count = 0
    viki_image_count = 0
    for line in lines:   
        s = line.split(' ')     #遇到空白切割出一格
        time = s[0]   
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sticker_count += 1
            elif s[2] == '圖片':
                allen_image_count += 1  
                
            else:
                for m in s[2:]:
                    allen_word_count += len(m)
        
        elif name == 'Viki':
            if s[2] == '貼圖':
                viki_sticker_count += 1
            elif s[2] == '圖片':
                viki_image_count += 1  
            else:    
                for m in s[2:]:
                    viki_word_count += len(m)
              
    print('allen說了', allen_word_count,'個字，傳了', allen_sticker_count, '個貼圖，', allen_image_count, '張圖片')   
    print('viki說了', viki_word_count,'個字，傳了', viki_sticker_count, '個貼圖，', viki_image_count, '張圖片' ) 
    return


def write_file(filename,lines):
    with open(filename, 'w',encoding='utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')    
        

lines = read_file('LINE-Viki.txt')
lines = convers_file(lines)
#write_file('Lineoutput.txt',lines)


            