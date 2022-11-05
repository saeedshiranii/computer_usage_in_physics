import numpy
import matplotlib.pyplot as plt

# x axis values 
f_x_axis = [197, 251, 280, 313, 362] 
devide_f_x_axis = [0.005, 0.004, 0.004, 0.003, 0.003, 0.002, 0.002]
# corresponding y axis values 
l1_y_axis = [28.0, 15.8, 14.1, 12.3, 10.7, 8.8, 7.5]
l2_y_axis = [56.0, 33.0, 29.0, 26.7, 22.5, 18.9, 17.0]

# plotting the points  
plt.plot(devide_f_x_axis, l2_y_axis) 
    
# naming the x axis 
plt.xlabel('x - axis') 
# naming the y axis 
plt.ylabel('y - axis') 
    
# giving a title to my graph 
plt.title('My first graph!') 
    
# function to show the plot 
plt.show() 