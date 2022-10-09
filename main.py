

import requests
import json
import time
import shutil
from alive_progress import alive_bar
import os

vvod=input('1. Сбор данных')
def f1():
    if os.path.exists('data'):
        shutil.rmtree('data')
    os.mkdir('data')
    #os.system('cls||clear')
    r = requests.get(
        'https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT')
    data = json.loads(r.text)
    # print(data)
    all_para = []
    count = len(data['symbols'])
    f_all_para = open('data/all_para.txt', 'w')
    for i in range(count):  # data
        para = data['symbols'][i]['baseAsset']+'/'+data['symbols'][i]['quoteAsset']
        all_para.append(para)
        f_all_para.write(para+'\n')
    usdt = []
    usdt2=[]
    no_usdt = []
    vector = []

    for j in all_para:
        if j.find('USDT') == -1:
            no_usdt.append(j)
            with open('data/no_usdt.txt','a') as f_no_usdt:
                f_no_usdt.write(j+'\n')
        else:
            usdt.append(j)
            usdt2.append(j)
            with open('data/usdt.txt','a') as f_usdt:
                f_usdt.write(j+'\n')

    shutil.copyfile('data/usdt.txt', 'data/usdt2.txt')
    counter=0
    middle=''

    count_iter = range(len(usdt)*len(usdt2))

    with alive_bar(len(count_iter)) as bar:

        for i1 in usdt:
            for i2 in usdt2:
                # print(f'{i1}  -  {i2}')
                if i1.split('/')[0] == 'USDT':
                    part1 =i1.split('/')[1]
                elif i1.split('/')[1] == 'USDT':
                    part1 =i1.split('/')[0]
                if i2.split('/')[0] == 'USDT':
                    part2 =i2.split('/')[1]
                elif i2.split('/')[1] == 'USDT':
                    part2 =i2.split('/')[0]
                if f'{part1}/{part2}' in no_usdt:
                    middle=(f'{part1}/{part2}')
                    vector.append(f'{i1} >> {middle} >>  {i2}')
                elif f'{part2}/{part1}' in no_usdt:
                    middle=(f'{part2}/{part1}')
                    vector.append(f'{i1} >> {middle} >>  {i2}')
                bar()


    with alive_bar(len(vector)) as bar2:
        for v in vector:
            # print(v)
            with open('data/finish.txt','a') as finish:
                finish.write(f'{v}\n')
            bar2()


if int(vvod)==1:
    f1()
else:
    print('Введите исправную команду')



