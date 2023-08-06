# WINCOM module python in https://pypi.org

# Modules
import os
import shutil



# Variables
html_code = '''<DOCTYPE html>
<html lang="en">
<head>
      <meta charset="utf-8">
      <title>Document</title>
</head>
<body>

</body>
</html>
'''




# CMD commands
def cmd(command='echo Default CMD command'):
      os.system(command)


# PYTHON commands
def py(command='print("Default python command")'):
      eval(command)


# *FOLDER AND FILE CREATE*
def folder(name):
      os.mkdir(name)
      return f'Suceffuly created folder {name}'

def file(name):
      with open(name, 'w+', encoding='utf-8') as f:
            f.write('#')
            f.close()
      return f'Suceffuly created file {name}'


# *DELETE FOLDER OR FILE*
def del_folder(name):
      shutil.rmtree(name)
      return f'Suceffuly removed folder {name}'

def del_file(name):
      os.remove(name)
      return f'Suceffuly removed file {name}'


# *EDIT FILE*
def read(file):
      with open(file, mode='r', encoding='utf-8') as f:
            text = f.read()
            f.close()

      return text

def write(file, text):
      with open(file, 'w', encoding='utf-8') as f:
            f.write(text)
            f.close()

      return text




# PROGRAMMING
def stldir(name):
      os.mkdir('static')
      os.mkdir('static/css')
      with open(f"static/css/{str(name)}.css", 'w+', encoding='utf-8') as f:
            f.write(f'/* CREATED FILE {name} */')
            f.close()
      return f'Suceffuly created path "static/css/{name}"'

def imgdir():
      if not os.path.exists('static'):
            os.mkdir('static')
            os.mkdir('static/images')
      else:
            os.mkdir('static/images')
      return 'Suceffuly created path "static/images"'

def html(name):
      with open(str(name)+'.html', 'w+', encoding='utf-8') as f:
            f.write(html_code)
            f.close()