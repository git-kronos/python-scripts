import os

# ========================================
# change working directory
# ========================================
# os.chdir('E:/project.dev/Temp')

# ========================================
# current working directory
# ========================================
# os.getcwd()

# ========================================
# make directory
# ========================================
# os.mkdir('Templates')
# os.makedirs(NEW_FOLDER)

# ========================================
# remove directory
# ========================================
# os.rmdir(NEWDIR)
# os.removedirs(NEW_DIR)

# ========================================
# rename a file/directory
# ========================================
# os.rename('E:/project.dev/Temp/20some.py', "E:/project.dev/Temp/20.py")

# ========================================
# status of a file/folder
# ========================================
# os.stat('20.py')
# print(os.stat('20.py').st_size)
# print(os.listdir('E:/project.dev/Temp'))

# ========================================
# folder details
# ========================================
# print(os.walk('E:/project.dev/Temp'))
# print()
# for dirpath, dirnames, filenames in os.walk('E:/project.dev/Temp'):
#     print('Current Path: ', dirpath)
#     print('Directory: ', dirnames)
#     print('Files: ', filenames)
#     print()


# ========================================
# ENV variables
# ========================================
# print(os.environ)
# print(os.environ.get('HOMEPATH'))
# print(os.environ.get('COMPUTERNAME'))
# print(os.environ.get('USERNAME'))
# print(os.environ.get('USERDOMAIN'))
# print(os.environ.get('SYSTEMROOT'))
# print(os.environ.get('SYSTEMDRIVE'))
# print(os.environ.get('PROGRAMFILES'))


# ========================================
# os.path
# ========================================
BASE_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, 'Templates')
# print(BASE_DIR)
# print(TEMPLATES_DIR)
# print(os.path.basename(f'{BASE_DIR}/test.txt'))
# print(os.path.dirname(f'{BASE_DIR}/test.txt'))
# print(os.path.exists(f'{BASE_DIR}/test.txt'))
# print(os.path.isdir(f'{BASE_DIR}/test.txt'))
# print(os.path.isfile(f'{BASE_DIR}/test.txt'))
# print(os.path.splitext(f'{BASE_DIR}\\test.txt'))
# print(dir(os.path))
# print(os.path.sys)
