'''
Desktop Sorter
by Carlo Buama
'''

import shutil
import os
import time

count = 0
path = '/Users/'+str(os.getlogin())+'/Desktop'
extensions = []

print('Scanning files...')
time.sleep(0.5)

#obtains list of extensions, excluding folders
for file in (x for x in os.listdir(path) if os.path.isfile(os.path.join(path, x))):
    if file[file.rfind('.'):] not in ['.ini','.tmp']:
        extensions.append(file[file.rfind('.')+1:])
extensions = list(set(extensions))

if len(extensions) != 0:
    print('> Found {n} filetype(s) in {path}.'.format(n=len(extensions), path=path))
    time.sleep(0.5)

    print('Creating sorted directory...')
    time.sleep(0.5)
    try:
        os.mkdir(path+'/Sorted/')
        print('> Directory created successfully.')
    except:
        print('> Directory already exists.')
    time.sleep(0.5)

    print('Creating file type directories...')
    time.sleep(0.5)

    for item in extensions:
        try:
            os.mkdir(path + '/Sorted/' + item + '/')
        except:
            print('> Directory for .{item} files already exists.'.format(item=item))
    time.sleep(0.5)

    #moves files by file type
    try:
        for a in extensions:
            for i in os.listdir(path):
                if i.endswith(a) and a != i:
                    try:
                        print('Moving "{file}" ...'.format(file=i))
                        src = path+'/'+i
                        dest = path + '/Sorted/' + a + '/'+i
                        shutil.move(src, dest)
                        count += 1
                    except:
                        print('Could not move "{file}".'.format(file=i))

        if count > 1:
            print('> Successfully moved {count} files!'.format(count=count))
        elif count == 1:
            print('> Successfully moved {count} file!'.format(count=count))
        else:
            print('> 0 files moved!')
        time.sleep(5)
    except:
        print('> Oops! An error has occurred.')
        time.sleep(5)
else:
    print('> No files to sort!')


