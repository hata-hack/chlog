#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import codecs

def hhelo():
    print('+___________________________________________________________+')
    print('|                      CheLog v0.1                          |')
    print('|                                                           |')
    print('| Checking the logs for the presence of the sites you need  |')
    print('| Coded By Hata: j_id: hata@thesecure.biz                   |')
    print('| Telegram Chanel https://t.me/hata_hack                    |')
    print('+___________________________________________________________+')
    print(' ')


#get list signature
def read_sig():
    f = open('sign.txt')
    array_sig = []
    for line in f.readlines():
        array_sig.append(line)

    #del duble & /r/n
    array_sig = [line.rstrip() for line in array_sig]
    print('↳ Number of rows loaded (duplicates removed!): ' + str(len(array_sig)))
    return array_sig


def allfilelist(sig_list):
    #out arr
    array_wayfile = []

    #set directory
    os.chdir("logi")
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            array_wayfile.append(os.path.join(root, name))
    print('↳ Number of files to check: ', str(len(array_wayfile)))
    print('')
    return array_wayfile


def find_sig(file_list, sig_list):
    array_good_find = []

    #for progress bar
    percent = 100 / len(sig_list)
    progress = 0

    #for log
    logfile = open('found_link.log', 'w')

    for sig in sig_list:

        progress += percent
        print('\r↳ Processing completed %3d%%' % progress, end='', flush=True)

        for name in file_list:
            with codecs.open(name, 'r', encoding='utf-8', errors='ignore') as file:
                for line in file:
                    if sig in line:
                        #print('Found {', sig, '} in ', name)
                        sgud = ('Found {' + sig + '} in ' + name)
                        logfile.write(sgud + '/r/n')
                        array_good_find.append(sgud)

    logfile.close()
    return len(array_good_find)

def main():
    hhelo()
    arr_sig = read_sig()
    arr_file = allfilelist(arr_sig)
    found_coim = find_sig(arr_file, arr_sig)
    print ('Records found: ', (len(found_coim)))

if __name__ == '__main__':
    main()