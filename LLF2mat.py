import numpy as np
import re
#import os
#import sys
#sys.modules[__name__].__dict__.clear()

#os.chdir('~/Desktop/esp/code/')
file = open('../data/All_app.tsv', 'rb')
table = [row.strip().decode("utf-8") for row in file]
print(table)
file.close()

mat = []
for i in table:
    #str = '../data/llfraw/LLF_40/'+ i +'/1024';
    #file = open(str)
    #cc = file.read();
    #file.close()
    cc = open('../data/llfraw/LLF_40/'+ i +'/1024').read();
    index_start = cc.index('Core (SKT) | EXEC | IPC  | FREQ  | AFREQ | L3MISS | L2MISS | L3HIT | L2HIT | L3CLK | L2CLK  | READ  | WRITE | TEMP');
    index_end = cc.index('Cleaning up');
    arr = re.findall(r"[-+]?\d*\.\d+|\d+", cc[index_start:index_end]);
    mat.append(arr);
    print("-----len(mat)",len(arr))
aa = np.matrix(mat);
print(len(mat))
#print(aa)
#print(len(aa))
