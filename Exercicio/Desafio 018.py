from math import sin,cos,tan,radians
a = float(input('Digite um Angulo '))
print ('O angulo de {} tem o Seno {:.2f}\nO angulo de {} tem o Cosseno {:.2f}\nO angulo de {} tem a Tangente{:.2f}'.format(a,sin(radians(a)),a,cos(radians(a)),a,tan(radians(a))))