# pinephone sensors
This is a python script from http://www.electronicsfaq.com/2020/07/enabling-industrial-io-driver-on.html 
Which I have changed to work on the pinephone. 
Mobian OS has drivers built for the sensors, which makes it a case of using the /sys directory to read the sensors. 
st_sensors_i2c 16384 1 st_magn_i2c 
st_magn 20480 1 st_magn_i2c 
inv_mpu6050_i2c 16384 0


