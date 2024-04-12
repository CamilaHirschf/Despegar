import os
import re

access_key_regex = re.compile(r'((?:ASIA|AKIA|AROA|AIDA|ABIA|ACCA|AGPA|AIPA|ANPA|ANVA|APKA|ASCA)([A-Z0-7]{16}))')
secret_access_key_regex = re.compile(r'[A-Za-z0-9/\+=]{40}')
gpat_regex = re.compile(r'ghp_[0-9a-zA-Z]{36}')

RED = '\033[31m'
RESET = '\033[0m'
GRAY = '\033[90m'

def search_matches(file, regex, type_key):
    managed_file = os.path.normpath(file)
    with open(managed_file, 'r', encoding='utf-8', errors='ignore') as f:
        for num_line, line in enumerate(f, start=1):
            match = regex.search(line)
            if match:
                found_key = match.group()
                print(f"{type_key} encontrada en: {file}, línea {num_line}: {RED}{found_key}{RESET}\n")

def search_in_repository(path_repository):
    for root, dirs, files in os.walk(path_repository):
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            file_path = os.path.join(root, file)
            if '.git' in file_path:
                continue
            search_matches(file_path, access_key_regex, f"{GRAY}Clave de Acceso AWS{RESET}")
            search_matches(file_path, secret_access_key_regex, f"{GRAY}Clave Secreta de Acceso AWS{RESET}")
            search_matches(file_path, gpat_regex, f"{GRAY}Token de Acceso Personal GPAT{RESET}")

# Cambiar 'ruta/a/tu/proyecto' por la ruta real de tu proyecto local de GitHub Ej: 'C:/Users/User/Documentos/Despegar'
search_in_directory = './'
search_in_repository(search_in_directory)




