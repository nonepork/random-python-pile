import os
import time
import inquirer

global file_path
file_path = ''
global text
text = ''

def get_file_path():

    os.system('clear' if os.name == 'posix' else 'cls')

    all_files = os.listdir()
    for i in all_files:
        if os.path.isdir(i):
            all_files.remove(i)
    while True:
        questions = [
            inquirer.List('file', message = 'Choose a text file to search', choices = all_files)
        ]
        answers = inquirer.prompt(questions)
        if answers['file'].endswith('.txt'):
            break
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
            print('Please select a text file that ends with .txt extensions')

    global file_path
    file_path = os.path.join(os.getcwd(), answers['file'])

def search(searched_word, file):

    os.system('clear' if os.name == 'posix' else 'cls')
    print('Searching...')

    search_result = []

    with open(file, 'r', encoding='utf-8') as f:
        for i in f:
            if searched_word.lower() in i.lower():
                search_result.append(i)

    with open(f'{searched_word} results.txt', 'a', encoding='utf-8') as f:
        for i in search_result:
            f.write(i)

    print(f'Search done, check "{searched_word} results.txt"')
    time.sleep(5)
    os.system('clear' if os.name == 'posix' else 'cls')

def options():
    global text
    while True:
        option = input('====> ')
        if option == '1':
            get_file_path()
            return False
        elif option == '2':
            if file_path:  # Check if file_path is not an empty string
                text = str(input('Search: '))
                search(text, file_path)
            else:
                print('Please select a file first.')
                time.sleep(5)
            return False
        elif option == '3':
            exit()
        else:
            print('Please select a valid option')
    

logo = '''
██╗      █████╗ ██████╗  ██████╗ ███████╗
██║     ██╔══██╗██╔══██╗██╔════╝ ██╔════╝
██║     ███████║██████╔╝██║  ███╗█████╗  
██║     ██╔══██║██╔══██╗██║   ██║██╔══╝  
███████╗██║  ██║██║  ██║╚██████╔╝███████╗
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝ file text searcher


'''

text_options = '''
[SELECT]
L[1] Select file
L[2] Search
L[3] Exit
'''

if __name__ == "__main__":
    while True:
        os.system('clear' if os.name == 'posix' else 'cls')
        temp = os.getcwd()+'\\'

        print(logo)
        print(f'Current selected file: {file_path.replace(temp, "")}')
        print(f'Last searched text: {text}')
        print(text_options)
        options()
