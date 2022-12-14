import csv
import os

path = "en-US"
os.chdir(path)
  
def read_text_file(file_name, file_path):
     with open(file_path, 'r') as f:
        content = f.read()
        print(file_name)

        file1 = open('../vi-VN/%s' %(file_name),"w+")
        with open('../data.csv', "r",  encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            file1.write(f'export default {"{"}\n')
            for row in csv_reader:
                if row[0] in content and row[0] != '':
                    text = ''
                    count = 0
                    for t in row:
                        if (count > 0):
                            text += ''.join(t.splitlines())
                        count += 1
                    file1.write(f"'{row[0]}': `{text}`,\n")
                line_count += 1
            file1.write(f'{"}"}')
        file1.close()
  
# iterate through all file
for file in os.listdir(os.getcwd()):
    if file.endswith(".js"):
        with open(os.path.join(os.getcwd(), file), 'r') as f:
            read_text_file(file, os.path.join(os.getcwd(), file))
print(f'Done.')

