import csv
from googletrans import Translator

def translate_text(text, src_lang, dest_lang):
    translator = Translator()
    translated = translator.translate(text, src=src_lang, dest=dest_lang)
    return translated.text

def main():
    input_csv_file = 'input.csv'
    output_csv_file = 'output.csv'
    
    row_counter = 0
    processed_rows = 200
    start_index = 5400
    
    translated_rows = []
    
    with open(input_csv_file, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile)
        
        if start_index == 0:
            header_row = next(csvreader)
            translated_rows.append(header_row)
            row_counter += 1
        else:
            for _ in range(start_index):
                next(csvreader)
        
        for row in csvreader:
            print(row[0])
            if row[1] == '男性': row[1] = 'مرد'
            else: row[1] = 'زن'
            if row[3] == '悲伤': row[3] = 'غمگین'
            elif row[3] == '愤怒': row[3] = 'عصبانیت'
            elif row[3] == '焦虑': row[3] = 'اضطراب'
            elif row[3] == '快乐': row[3] = 'خوشحالی'
            elif row[3] == '所有情绪': row[3] = 'همه احساسات'
            row[4] = translate_text(row[4], 'zh-cn', 'fa')
            row[5] = translate_text(row[5], 'zh-cn', 'fa')
            
            translated_rows.append(row)
            row_counter += 1
            
            if row_counter >= processed_rows:
                break
    
    write_mode = 'w' if start_index == 0 else 'a'
    with open(output_csv_file, write_mode, encoding='utf-8', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        for row in translated_rows:
            csvwriter.writerow(row)

if __name__ == "__main__":
    main()