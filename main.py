import numpy as np 
import time

class Decorator:
    def __init__(self,func): 
        self._func = func
        self.czas = []
        
    def __call__(self, *args, **kwargs):
        
        start = time.time()
        wynik = self._func(*args, **kwargs)
        stop = time.time()
        self.czas.append(stop - start)
        self.srednia = sum(self.czas)/len(self.czas)
        self.max = max(self.czas)
        self.min = min(self.czas)
        
        self.std = np.std(self.czas)
        return wynik
    


#dekorujemy 
np.arange = Decorator(np.arange)

for n in range(5):
    a = np.arange(1000000000)


print("wszystkie czasy: ",np.arange.czas)
print("sredni czas: ",np.arange.srednia)
print("max czas: ",np.arange.max)
print("min czas: ",np.arange.min)
print("odchylenie czasow: ",np.arange.std)
# for n in range(5):
#     start = time.time()
#     a = np.arange(1000000000)
#     stop = time.time()
#     print(stop-start)
