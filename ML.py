l=0
o=0
def cal_mean(readings):
  
    readings_total = sum(readings)
    number_of_readings = len(readings)
    mean = readings_total / float(number_of_readings)
    return mean
from math import pow

def cal_variance(readings):
   readings_mean = cal_mean(readings)
   mean_difference_squared_readings = [pow((reading - readings_mean), 2) for reading in readings]
   variance = sum(mean_difference_squared_readings)
   return variance / float(len(readings) - 1)  
  
from math import pow

def cal_covariance(readings_1, readings_2):
    
    readings_1_mean = cal_mean(readings_1)
    readings_2_mean = cal_mean(readings_2)
    readings_size = len(readings_1)
    covariance = 0.0
    for i in range(0, readings_size):
        covariance += (readings_1[i] - readings_1_mean) * (readings_2[i] - readings_2_mean)
    return covariance / float(readings_size - 1)
  
def linear_regression(x_readings, y_readings):
    global l 
    global o
  
    l=w1 = cal_covariance(x_readings, y_readings) / float(cal_variance(x_readings))
    o=w0 = cal_mean(y_readings) - (w1 * cal_mean(x_readings))
    return w0, w1
 
 
 
def predic(X):
  predicted_values=o+l*X
  return predicted_values

