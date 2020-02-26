from control import lqr
import numpy as np
from math import pi


ki=10
kd=10
kp=0.01

#@state_feedback
#    param:
#        X
#            [theta, theta_dot, x, x_dot]
#        t
#            double
#    return:
#        new_X
#            [new_theta, new_theta_dot, new_x, new_x_dot]
def state_feedback(X,t,Xprev):
    
    if -pi/360 < X[0] and X[0] < pi/360:
        return [0, 0, 0, 0]
    else:    
	for i in range(4):
		intgrl=-ki*X[i]*t
		diff=kd*(X[i]-Xprev[i])/t
		prop=-kp*X[i]
		X[i]+=prop+diff+intgrl
        X[2]=0
        return X


