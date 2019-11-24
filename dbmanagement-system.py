#!/usr/bin/env python3
#This script is written by Bishoy Fawzi
import csv
import os, errno
import shutil
def create_dir(name):
    try:
        os.makedirs(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
def delete_dir(name):
    try:
        shutil.rmtree(name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def main():
    create_dir('DB-management') 
    print('Please choose option')
    print('1- Create New Database')
    print('2- Delete Database')
    print('3- Create Table on Database')
    print('4- Drop Table')
    print('5- ADD Field from table')
    print('6- Drop Field from table')
    print('7- Add records')
    print('8- remove records')
    print('9- Select records with condition')
    g = input("Enter Value : ") 
    if g=='1':
        dbname=input("Enter DB name : ")
        create_dir('DB-management/'+dbname)
    elif g=='2':
        for x in os.listdir('DB-management'):
            print (x)
        dbname=input("Enter DB name : ")
        delete_dir('DB-management/'+dbname)
        for x in os.listdir('DB-management'):
            print (x)
    elif g=='3':
        tbname=input("Enter Table name : ")
        for x in os.listdir('DB-management'):
            print (x)
        dbname=input("Enter DB name : ")
        with open('DB-management/'+dbname+'/'+tbname+'.csv', 'wb') as f:
            reader = csv.reader(f)

#    elif g=='4':
#        print('drop table')
    



if __name__ == '__main__':
    main()



