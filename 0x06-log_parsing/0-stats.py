#!/usr/bin/python3
""" Log parsing """
from sys import stdin



def logLecture():
    nl = []
    for line in stdin:
        nl.append(list(line.rstrip("\n").split(" ")))
        codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
        if len(nl) == 10:
            x = 0
            ss = []
            ctn = []
            for j in range(len(nl)):
                x = x + int(nl[j][8])
                if(nl[j][7]) in codes:
                    ss.append(nl[j][7])
                    ss.sort()
            
            print("File size: {}".format(x))
            
            for i in range(len(nl)):
                a = ss.count(ss[i])
                ctn.append(a)
                #print(ss[i], a)
            
            for key, value in dict(zip(ss, ctn)).items():
                print(key + ': ' + str(value))
        

logLecture()
