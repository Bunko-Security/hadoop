import argparse
from colorama import init
from colorama import Fore, Style

from commands import HDFSCommands


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('host', type=str, help='Сервер')
    parser.add_argument('port', type=int, help='Порт')
    parser.add_argument('user', type=str, help='Имя пользователя')
    args = parser.parse_args()
    
    
    hdfs = HDFSCommands(args.host, args.port, args.user)
    while True:
        command = input(
            '\n' + 
            Fore.GREEN + Style.BRIGHT + f'''hdfs~{hdfs.hdfs_pwd}''' + Style.RESET_ALL + '''\n''' +
            Fore.YELLOW + Style.BRIGHT +f'''local~{hdfs.local_pwd}''' + Style.RESET_ALL + '''\n''' +
            Fore.WHITE + Style.NORMAL + f'''({args.user}@{args.host}:{args.port})$ ''' + Style.RESET_ALL
        )
        if command == 'exit':
            break
        elif '\\' in command or '/' in command:
            print('Слэши не поддерживаются')
        else:
            hdfs.execute(command.split())


if __name__ == '__main__':
    init(autoreset=True)
    main()