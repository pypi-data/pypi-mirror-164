import numpy as np
from math import pi,cos,sin,tan,atan,ceil
import operator as op
from cmath import exp
def linear_conv(x,h):
              
              N=len(x)+len(h)-1
              x1=np.zeros((N))
              h1=np.zeros((N))
              m=len(x)
              n=len(h)
              y=np.zeros((N))
              for i in range(m):
                            x1[i]=x[i]
              for i in range(n):
                            h1[i]=h[i]
              for i in range(N):
                            for j in range(i+1):
                                          y[i]=y[i]+ x1[j]*h1[i-j]
              return y
    
def circular_conv(x,h):   
              N=max(len(x),len(h))
              y=np.zeros((N))
              x1=np.zeros((N))
              h1=np.zeros((N))
              for i in range(len(x)):
                            x1[i]=x[i]
              for i in range(len(h)):
                            h1[i]=h[i]
              for i in range(N):
                            for j in range(N):
                                          y[i]=y[i]+x1[j]*h1[op.mod((i-j),N)]

              return y

def sampling_theorem():
              Rt=float(input('Enter the resolution of analog signal'))
              Ns= int(1/Rt)
              t=[Rt*t1 for t1 in range(Ns)]
              fm=int(input('enter the fundamental frequency'))
              xt=[cos(2*pi*fm*Rt*t1) for t1 in range(Ns)]
              fs=int(input('enter the sampling frequency'))
              Ts=(1/fs)
              N=fs
              n=[n1 for n1 in range(N)]
              xn=[cos(2*pi*fm*n1*Ts) for n1 in range(N)]
              xr=np.zeros((len(xt)))
              tr=0
              for t1 in range(Ns):
                            for n2 in range(N):
                                          if((pi*(tr-n2*Ts)/Ts)==0):
                                                        xr[t1]=xr[t1]+xn[n2]
                                          else:
                                                        xr[t1]=xr[t1]+xn[n2]*(sin(pi*(tr-n2*Ts)/Ts))/((pi*(tr-n2*Ts))/Ts)
                            tr=tr+Rt
              return t,xt,n,xn,xr
def fft(x):
        N=len(x)
        X=np.zeros((N),'complex')
        for k in range(N):
            for n in range(N):
                X[k]=X[k] + x[n]*exp(-1j*2*pi*k*n/N)
        return X
def ifft(X):
        N=len(X)
        x=np.zeros((N),'complex')
        for n in range(N):
            for k in range(N):
                x[n]=x[n] + X[k]*exp(1j*2*pi*k*n/N)
        x=x/N
        return x
def rect2sinc(du,a,fs):
              du=int(du)
              a=int(a)
              fs=int(fs)
              t=[i for i in np.arange(0,du,(du/fs))]
              N=len(t)
              x=np.zeros(fs)
              for i in range(int(fs/4),int((3*fs)/4)):
                            x[i]=a
              X=np.fft.fft(x)
              X1=np.fft.fftshift(X)
              f=[i for i in np.arange(-fs/2,fs/2,fs/N)]
              return x,t,X1,f
def sinc2rect(du,fm,fs):
              du=int(du)
              fm=int(fm)
              fs=int(fs)
              t=[i for i in np.arange(-du/2,du/2,(du/fs))]
              N=len(t)
              x=[np.sinc(2*np.pi*fm*i) for i in np.arange(-du/2,du/2,(du/fs))]
              X=np.fft.fft(x)
              X1=np.fft.fftshift(X)
              f=[i for i in np.arange(-fs/2,fs/2,fs/N)]
              return x,t,X1,f
def auto_correlation(x):
        x1=x[::-1]
        N=len(x)+len(x1)-1
        x11=np.zeros((N))
        h1=np.zeros((N))
        m=len(x)
        n=len(x1)
        y=[0]*N
        for i in range(m):
            x11[i]=x[i]    
        for i in range(n):
            h1[i]=x1[i]   
        for i in range(N):
            for j in range(i+1):
                y[i]=y[i]+ x11[j]*h1[i-j]   
        return y

def cross_correlation(x,h):
        h1=h[::-1]
        N=len(x)+len(h)-1
        x11=np.zeros((N))
        h11=np.zeros((N))
        m=len(x)
        n=len(h)
        y=np.zeros((N))
        for i in range(m):
            x11[i]=x[i]    
        for i in range(n):
            h11[i]=h1[i]   
        for i in range(N):
            for j in range(i+1):
                y[i]=y[i]+ x11[j]*h11[i-j]   
        return y

def filter(b,a,x):
              N=len(x)
              b1=np.zeros((N))
              a1=np.zeros((N))
              nr=np.zeros((N))
              dr=np.zeros((N))
              y=np.zeros((N))
              if(np.size(a)==1):
                            for i in range(len(b)):
                                          b1[i]=b[i]
                            for i in range(N):
                                          for j in range(i+1):
                                                        y[i]=y[i]+b1[j]*x[i-j]
              else:
                                          
                            for i in range(len(b)):
                                          b1[i]=b[i]
                            for i in range(len(a)):
                                          a1[i]=a[i]
                            for i in range(N):
                                          for j in range(i+1):
                                                        nr[i]=nr[i]+b1[j]*x[i-j]
                                          for j in range(i+1):
                                                        dr[i]=dr[i]-a1[j]*y[i-j]
                                          y[i]=nr[i]+dr[i]
              return y

def fir_lpf(N,wc,win,freq_resolution):
              w=np.zeros((N))
              if win=='hamm':            
                            for n in range(N):
                                          w[n]=0.54-0.46*cos((2*pi*n)/(N-1))
              elif win=='hann':
                            for n in range(N):
                                          w[n]=0.5-0.5*cos((2*pi*n)/(N-1))
              else:
                            for n in range(N):
                                          w[n]= 1
         
              hd=np.zeros((N))
              h=np.zeros((N))
              alp=(N-1)/2
              for n in range(N):
                            if n==alp:
                                          hd[n]=wc/pi
                            else:
                                          hd[n]=sin(wc*(n-alp))/(pi*(n-alp))
              for n in range(N):
                            h[n]=hd[n]*w[n]
              N1=np.ceil((2*pi)/(freq_resolution))+1
              H=np.zeros(int(N1),'complex')
              w2=-pi
              t1=np.zeros(int(N1))
              i=0
              for w1 in range(int(N1)):
                            for n in range(N):
                                          H[w1]=H[w1]+h[n]*exp(-1j*w2*n)
                            t1[i]=w2
                            w2=w2+freq_resolution
                            i=i+1
              return h,t1,H
def fir_hpf(N,wc,win,freq_resolution):
              w=np.zeros((N))
              if win=='hamm':            
                            for n in range(N):
                                          w[n]=0.54-0.46*cos((2*pi*n)/(N-1))
              elif win=='hann':
                            for n in range(N):
                                          w[n]=0.5-0.5*cos((2*pi*n)/(N-1))
              else:
                            for n in range(N):
                                          w[n]= 1
         
              hd=np.zeros((N))
              h=np.zeros((N))
              alp=(N-1)/2
              for n in range(N):
                            if n==alp:
                                          hd[n]=(pi-wc)/pi
                            else:
                                          hd[n]= -sin(wc*(n-alp))/(pi*(n-alp))
              for n in range(N):
                            h[n]=hd[n]*w[n]
              N1=np.ceil((2*pi)/(freq_resolution))+1
              H=np.zeros(int(N1),'complex')
              w2=-pi
              t1=np.zeros(int(N1))
              i=0
              for w1 in range(int(N1)):
                            for n in range(N):
                                          H[w1]=H[w1]+h[n]*exp(-1j*w2*n)
                            t1[i]=w2
                            w2=w2+freq_resolution
                            i=i+1
              return h,t1,H
def buttord(fp,fs,ap1,as1,F):
              T=1/F
              wp=2*pi*fp/F
              ws=2*pi*fs/F
              Wp=2*F*tan(wp/2)
              Ws=2*F*tan(ws/2)
              nr= 10**(ap1/10)-1
              dr=  10**(as1/10)-1
              N= np.log10((nr/dr))/(2*np.log10(Wp/Ws))
              N=ceil(N)
              if(ap1>10):
                            Wc= (Ws)/((10**(as1/10)-1)**(1/(2*N)))
              else:
                            Wc= (Wp)/((10**(ap1/10)-1)**(1/(2*N)))
              wc= 2*atan((Wc*T)/2)
              return N,wc/pi
def dct(x):
    N=len(x)
    X=np.zeros(N)
    for k in range(N):
        for n in range(N):
            X[k]=X[k]+ (cos(((pi*(2*n+1)*k)/(2*N)))*x[n])
        if k==0:
            X[k]=np.sqrt(1/N)*X[k]
        else:
            X[k]=np.sqrt(2/N)*X[k]
    return X
def idct(X):
    N=len(X)
    x=np.zeros(N)
    for n in range(N):
        for k in range(N):
            if k==0:
                x[n]=x[n]+ (cos(((pi*(2*n+1)*k)/(2*N)))*X[k]*(np.sqrt(1/N)))
            else:
                x[n]=x[n]+ (cos(((pi*(2*n+1)*k)/(2*N)))*X[k]*(np.sqrt(2/N)))
    return x
def dwt(x,Lo_D,Hi_D):
    lp=np.convolve(x,Lo_D)
    hp=np.convolve(x,Hi_D)
    print(lp)
    print(hp)
    ca=[lp[i] for i in range(1,len(lp),2)]
    cd=[hp[i] for i in range(1,len(hp),2)]
    return ca,cd
def idwt(ca,cd,Lo_R,Hi_R):
    up1=np.zeros(2*len(ca))
    j=0
    for i in range(len(ca)):
        up1[j]=ca[i]
        j+=2
    up11=np.convolve(up1,Lo_R)
    up2=np.zeros(2*len(cd))
    j=0
    for i in range(len(ca)):
        up2[j]=cd[i]
        j+=2
    up22=np.convolve(up2,Hi_R)
    re=up11+up22
    re=re[0:len(re)-1]
    return re
def triang(N):
    w=[0]*N
    for n in range(N):
        w[n]=1- 2*(np.abs((n-((N-1)/2))/(N-1)))
    return w
def mfcc_coeff(a,fs,frame_length,frame_step,filter_bank_size):
    l=0
    x=[]
    for i in range(0,len(a)-frame_length,frame_step):
        for k in range(frame_length):
            x.append(a[i+k])
            l+=1
    if len(x)%2==0:
        cols=len(x)/frame_length
    else:
        x=x+[0]
        cols=len(x)/frame_length
    cols=int(cols)
    x1=np.reshape(x,(frame_length,cols),order='F')
    x2=np.zeros((frame_length,cols))
    c=np.hamming(frame_length)
    for i in range(cols):
        x2[:,i]=x1[:,i]*c
    fx=np.zeros((frame_length,cols))
    for i in range(cols):
        fx[:,i]=(1/frame_length)*(np.abs(np.fft.fft(x2[:,i]))**2)
    fx=fx[0:int(frame_length/2),0:cols]
    fl=300
    fu=fs/2
    f=[i for i in np.arange(fl,fu)]
    f=np.array(f)
    mel=1125*(np.log(1+f/700))
    step=(mel[len(mel)-1]-mel[0])/(filter_bank_size+2)
    fmel=[i for i in np.arange(mel[0],mel[len(mel)-1]+1,step)]
    fmel=np.array(fmel)
    fin=700*(np.exp((fmel)/(1125))-1)
    rn=np.floor(((frame_length+1)*fin)/(fs))
    rn=list(rn)
    mel_win=list()
    for i in range(len(rn)-2):
        mel_win.append([0]*int(rn[i]-1)+triang(int(rn[i+2])-int(rn[i]))+[0]*(256-int(rn[i+2])+1))
    mel_win=np.array(mel_win)
    mel_win=np.transpose(mel_win)
    fx1=np.zeros((filter_bank_size,int(frame_length/2),cols))
    for i in range(cols):
        for k in range(filter_bank_size):
            fx1[k,:,i]=fx[:,i]*mel_win[:,k]
    se=np.zeros((filter_bank_size))
    for i in range(filter_bank_size):
        se[i]=np.sum(fx1[i,:,:])
    mfc=dct(np.log(se))
    return mfc   
