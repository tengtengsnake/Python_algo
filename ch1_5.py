import matplotlib.pyplot as plt
import numpy as np

xpt=np.linspace(1,10,10)
ypt1=xpt/xpt #time complexity is a constant O(1)
ypt2=np.log2(xpt)  #O(logn)
ypt3=xpt #O(n)
ypt4=xpt*np.log2(xpt)  #nlog(n)
ypt5=xpt*xpt #O(n*n)
plt.plot(xpt,ypt1,'-o',label="O(1)")
plt.plot(xpt,ypt2,'-o',label="O(logn)")
plt.plot(xpt,ypt3,'-o',label="O(n)")
plt.plot(xpt,ypt4,'-o',label="O(nlogn)")
plt.plot(xpt,ypt5,'-o',label="O(n*n)")
plt.legend(loc='best')

plt.show()
