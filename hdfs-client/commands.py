import requests
import pathlib
from colorama import Fore, Style



class HDFSCommands:
    # https://hadoop.apache.org/docs/r2.10.2/hadoop-project-dist/hadoop-hdfs/WebHDFS.html
    
    def __init__(self, host, port, user) -> None:
        self.hdfs_url = f'http://{host}:{port}/webhdfs/v1'
        self.user = user
        self.hdfs_pwd = ''
        self.local_pwd = pathlib.Path.cwd()
    
    
    def _get_url(self):
        return self.hdfs_url + self.hdfs_pwd + '/'
        
        
    def mkdir(self, dirname: str):
        response = requests.put(f'{self._get_url()}{dirname}?user.name={self.user}&op=MKDIRS')
        if response.status_code == 200:
            print(f'Директория {dirname} успешно создана')
        else:
            print(f'Что-то пошло не так')
            print(response.json())
            
            
    def cd(self, dirname: str):
        if dirname == '..':
            self.hdfs_pwd = '/'.join(self.hdfs_pwd.split('/')[:-1])
            return
        
        response = requests.get(f'{self._get_url()}{dirname}?user.name={self.user}&op=GETFILESTATUS')
        if response.status_code != 200:
            print(f'{self.hdfs_pwd + "/" + dirname} не директория')
            return
        
        if response.json().get('FileStatus').get('type') != 'DIRECTORY':
            print(f'{self.hdfs_pwd + "/" + dirname} не директория')
            return
        
        self.hdfs_pwd = self.hdfs_pwd + '/' + dirname
        
        
    def ls(self):
        response = requests.get(f'{self._get_url()}?user.name={self.user}&op=LISTSTATUS')
        for file in response.json().get('FileStatuses').get('FileStatus'):
            if file.get('type') == 'FILE':
                print(Fore.WHITE + file.get('pathSuffix'), end=' ')
            elif file.get('type') == 'DIRECTORY':
                print(Fore.BLUE + file.get('pathSuffix'), end=' ')
            elif file.get('type') == 'SYMLINK':
                print(Fore.RED + file.get('pathSuffix'), end=' ')
        print()
    
       
    def put(self, filename):
        try:
            path = self.local_pwd.joinpath(filename)
            with open(path, 'rb') as file:
                response = requests.put(f'{self._get_url()}{filename}?user.name={self.user}&op=CREATE', allow_redirects=True, data=file)
                if response.status_code == 201:
                    print(f'Файл {filename} создан')
                elif response.status_code == 403:
                    print(f'Файл {filename} уже создан')
                else:
                    print('Что-то пошло не так')
                    print(response.json())
        except FileNotFoundError:
            print(f'Файл {path} не существует')
        
    
    def append(self, local_filename, hdfs_filename):
        response = requests.get(f'{self._get_url()}{hdfs_filename}?user.name={self.user}&op=GETFILESTATUS')
        
        if response.status_code != 200:
            print(f'{self.hdfs_pwd + "/"} не существует')
            return
        elif response.json().get('FileStatus').get('type') != 'FILE':
            print(f'{self.hdfs_pwd + "/"} не файл')
            return
        
        try:
            path = self.local_pwd.joinpath(local_filename)
            with open(self.local_pwd.joinpath(local_filename), 'rb') as file:
                response = requests.post(f'{self._get_url()}{hdfs_filename}?user.name={self.user}&op=APPEND', allow_redirects=True, data=file)
                
                if response.status_code == 200:
                    print(f'Конкатенация успешна')
                else:
                    print('Что-то пошло не так')
                    print(response.json())
        except FileNotFoundError:
            print(f'Файл {path} не существует')
    

    def delete(self, filename):
        response = requests.delete(f'{self._get_url()}{filename}?user.name={self.user}&op=DELETE')
        if response.json().get('boolean'):
            print(f'{filename} удален')
        else:
            print(f'Файл не может быть удален')
    
    
    def get(self, filename):
        response = requests.get(f'{self._get_url()}{filename}?user.name={self.user}&op=OPEN', allow_redirects=True)
        if response.status_code == 200:
            with open(self.local_pwd.joinpath(filename), 'wb') as localfile:
                localfile.write(response.content)
        else:
            print('Что-то пошло не так')
            print(response.json())

    
    def lls(self):
        for i in self.local_pwd.iterdir():
            if i.is_file():
                print(Fore.WHITE + i.name, end=' ')
            elif i.is_dir():
                print(Fore.BLUE + i.name, end=' ')
            elif i.is_symlink():
                print(Fore.RED + i.name, end=' ')
        print()
                
    
    def lcd(self, dirname):
        if dirname == '..':
            self.local_pwd = self.local_pwd.parent
        elif self.local_pwd.joinpath(dirname).is_dir():
            self.local_pwd = self.local_pwd.joinpath(dirname)
        else:
            print(f'{self.local_pwd.joinpath(dirname)} не директория')
    
       
    def help(self):
        help_path = pathlib.Path(__file__).parent
        with open(help_path.joinpath('help.txt'),'r' ,encoding='utf-8') as f:
            help_list = f.read().split('\n')
        
        for command in help_list:
            text = command.split(' ')
            print(' ' + Fore.BLUE + text[0] + Style.RESET_ALL + ' ' + ' '.join(text[1:]))


    def execute(self, args):
        match args[0]:
            case 'mkdir': 
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.mkdir(args[1])
            case 'cd':
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.cd(args[1])
            case 'ls':
                if len(args) != 1:
                    print('Неверная команда')
                else:
                    self.ls()
            case 'put':
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.put(args[1])
            case 'append':
                if len(args) != 3:
                    print('Неверная команда')
                else:
                    self.append(args[1], args[2])
            case 'delete':
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.delete(args[1])
            case 'get':
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.get(args[1])
            case 'lls':
                if len(args) != 1:
                    print('Неверная команда')
                else:
                    self.lls()
            case 'lcd':
                if len(args) != 2:
                    print('Неверная команда')
                else:
                    self.lcd(args[1])
            case '?':
                self.help()
            case _:
                print(f'Команда {args[0]} не существует')