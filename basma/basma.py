#!/usr/bin/env python3

import os,sys,time
import numpy
from datetime import datetime
from datetime import timedelta
from pygame import mixer

def convert(arr, x, y):
    sp = 240 // y
    sx = 320 // sp
    while sx > x:
        sp = sp + 1
        sx = 320 // sp

    arr_tmp = [[] for i in range(240)]

    for y in range(240):
        token = 0
        tol = 0
        for x in range(320):
            if token == sp:
                # print(y,tol,sp)
                arr_tmp[y].append(tol)
                token = 0
                tol = 0
            tol += int(arr[y][x])
            token += 1
        if x == 329:
            arr_tmp[y].append(tol)
    arr = arr_tmp
    del arr_tmp

    arr_tmp = [[] for i in range(len(arr[0]))]
    for x in range(len(arr[0])):
        token = 0
        tol = 0
        for y in range(240):
            if token == sp:
                arr_tmp[x].append(tol)
                token = 0
                tol = 0
            tol += int(arr[y][x])
            token += 1
        if x == 239:
            arr_tmp[x].append(tol)

    arr = numpy.array(arr_tmp).T.tolist()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] >= sp * sp // 2:
                arr[i][j] = 1
            else:
                arr[i][j] = 0

    sma = ''
    for s in arr:
        sma += "".join(str(i)+str(i) for i in s) + '\n'
    del arr
    return sma

def millis():
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms

def playmp3(mp3_path):
    mixer.init()
    mixer.music.load(mp3_path)
    mixer.music.play()

def test_time():
    start_time = datetime.now()
    sma = []
    with open(os.path.join(SMA_RESOURCES, 'badapple_00001.txt'), 'r') as f:
            l = f.readline()[:-1]
            while len(l) != 0:
                sma.append(l)
                l = f.readline()[:-1]
            nsma = convert(sma, 130, 39)
    print(millis())

def playsma(spath, x, y):
    for root, dirs, filenames in os.walk(spath):
        for d in filenames:
            sma = []
            with open(os.path.join(spath, d), 'r') as f:
                l = f.readline()[:-1]
                while len(l) != 0:
                    sma.append(l)
                    l = f.readline()[:-1]
            nsma = convert(sma, x, y)
            sys.stdout.flush()
            sys.stdout.write(nsma)
            time.sleep(0.01)

def main():
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    SMA_RESOURCES = os.path.join(ROOT_PATH, 'badapple_digit')
    MP3_RESOURCES = os.path.join(ROOT_PATH, 'ba.mp3')

    rows, columns = os.popen('stty size', 'r').read().split()

    playmp3(MP3_RESOURCES)

    columns = int(columns) // 2
    playsma(SMA_RESOURCES, columns, int(rows))

if __name__ == '__main__':
    main()
