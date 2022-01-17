import RPi.GPIO as gpio #导入库
import time 
gpio.setmode(gpio.BCM) #确定编码格式
gpio.setup(20,gpio.OUT)  #设置输出引脚
gpio.setup(21,gpio.OUT)

while 1:
    输入 = int(input('输入：'))
    if 输入 == 1:
        gpio.output(20,gpio.HIGH)# 20引脚输出高电平
        time.sleep(4) #休眠4秒
        gpio.output(20,gpio.LOW)# 20引脚输出低电平
        time.sleep(4)
    elif 输入 == 2:
        gpio.output(21,gpio.HIGH)# 21引脚输出高电平
        time.sleep(4)
        gpio.output(21,gpio.LOW)# 21引脚输出低电平
        time.sleep(4)
    elif 输入 == 3:
        exit() #退出程序
gpio.cleanup()
