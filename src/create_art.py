from PIL import Image
import numpy as np


a = np.array(Image.open('uoy.png'))

lines = ''

rowskip = 9
lineskip = 10
for i,e in enumerate(a[::lineskip]):
    txt =  ''.join(['.'  if k>0 else ' ' for k in e[::rowskip]])
    lines += txt+'\n'
    with open('../sandbox/data_%02d.txt'%i,'w') as f:
	f.write(txt[::-1])


