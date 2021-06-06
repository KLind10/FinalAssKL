__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

from pathlib import Path
import os
import shutil 
import zipfile
path = os.getcwd()
cache_path_files = path + '\\cache'

# Files Assignment part 1: clean_cache 

def clean_cache():
  # print (list_directories_files): geeft bestanden/mappen in folder files
  list_directories_files = os.listdir() 
  
  if 'cache' in list_directories_files:
    # verwijder de folder cache
    shutil.rmtree('cache', ignore_errors=True) 
    # maak de folder cache aan
    os.mkdir('cache') 
  else:
    # maak de folder cache aan
    os.mkdir('cache') 
  # geeft bestanden/mappen in de folder files weer
  print(os.listdir()) 

# Files Assignment part 2: cache_zip

def cache_zip(zip_file_path,cache_path):
    # gebruik cache die ontstaat bij part 1
    clean_cache() 
    # creeer een ZipFile opbject en laad/voeg zipfile erin
    with zipfile.ZipFile(zip_file_path, 'r')as zip_ref: 
      # pak het Zip bestand uit in de cache folder
      zip_ref.extractall(cache_path) 
# gebruik path van file en path van folder
cache_zip(r'C:\\Users\\kimli\\WinC\\WinC Assignments\\files\\data.zip', r'C:\\Users\\kimli\\WinC\\WinC Assignments\\files\\cache')

# Files Assignment part 3: cached_files

def cached_files():
  # weergeef het pad naar de files
  # geef een lijst van files in folder cache
  file_list = []
  path = os.getcwd() +'\\cache'
  files = filter(lambda filepath: filepath.is_file(), Path(path).glob('*')) 
  for file in files:
    file_list.append(str(file.absolute()))
  
  return file_list

# Files Assignment part 4: find_password

def find_password(file_list):
  # lijst van files is gelijk aan die van vorige opdracht
  # open files en match in lines
  list_of_files = cached_files()
  for file in list_of_files:
    with open(file) as f:
      if 'password' in f.read():
        with open (str(file)) as p:
          for lines in p:
            if 'password' in lines:
              password = lines.strip('password: ')
              password = password.strip()
              print(password)
        return password


find_password(1)
