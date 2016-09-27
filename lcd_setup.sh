#! /bin/bash
##Startup script to ready the display

##set configuration registers to LCD output
i2cset -y 1 0x20 0x00 0x55
i2cset -y 1 0x20 0x01 0x55
i2cset -y 1 0x20 0x02 0x55
i2cset -y 1 0x20 0x03 0x55

##Set LCD control register with LCDEN =1, REGEN=1, BIAS1=1
## BIAS0=1, hi_DRV =1
i2cset -y 1 0x20 0x04 0x3d

