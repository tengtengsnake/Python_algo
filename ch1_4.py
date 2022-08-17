import matplotlib.pyplot as plt
import numpy as np
xpt=np.linspace(1,10,10)
ypt1=xpt/xpt
ypt2=np.log2(xpt)
ypt3=xpt
plt.plot(xpt,ypt1,'-o',label="O(1)")
plt.plot(xpt,ypt2,'-o',label="O(logn)")
plt.plot(xpt,ypt3,'-o',label="O(n)")
plt.legend(loc='best')
plt.show()
