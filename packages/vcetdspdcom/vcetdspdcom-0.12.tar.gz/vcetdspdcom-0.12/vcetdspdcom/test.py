from dsp import *
import numpy as np
from scipy.io import wavfile
""" x=[1,2,3,4,5]
Lo_D=[1/np.sqrt(2),1/np.sqrt(2)]
Hi_D=[-1/np.sqrt(2),1/np.sqrt(2)]
Lo_R=[1/np.sqrt(2),1/np.sqrt(2)]
Hi_R=[1/np.sqrt(2),-1/np.sqrt(2)]
ca,cd=dwt(x,Lo_D,Hi_D)
print(ca,cd)
y=idwt(ca,cd,Lo_R,Hi_R)
print(y) """
fs,a=wavfile.read('for1.wav')
a=a[:,0]
frame_length=512
frame_step=256
filter_bank_size=18
mfc=mfcc_coeff(a,fs,frame_length,frame_step,filter_bank_size)
print(mfc)
