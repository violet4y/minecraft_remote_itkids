# ピラミッド作成プログラム
from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep
import math

"pyramidのapi"
"kadai_08_violet4yの元"

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711

def set_pyramid(pyramidtype=1, X=10, Y=63, Z=10, H=6, SLEEP=0.8, BLOCK=param.GOLD_BLOCK):
    POS = 0   #位置情報
    mc.setBlocks(X, Y, Z, X+2*H-2, Y+H+1, Z+2*H-2, param.AIR)
    sleep(2)
    mc.postToChat("create a pyramid")

    if pyramidtype == 1:    
        for i in range(H+1):
            for i in range(2*H-1-POS*2):
                mc.setBlocks(X+POS, Y+POS, Z+POS, X+2*H-2-POS, Y+POS, Z+POS, BLOCK)
                Z += 1
                sleep(SLEEP)
            Z -= 2*H-1-POS*2
            POS += 1    

    if pyramidtype == 2:
        for count in range(H):
            xdifference = H-1-count
            zdifference = 0
            while zdifference < H-count:
                mc.setBlocks(X+xdifference, Y+count, Z+zdifference, X-xdifference, Y+count, Z-zdifference, BLOCK)
                xdifference -= 1
                zdifference += 1
                sleep(SLEEP)
        mc.setBlock(X, Y+H-1, Z, param.GLOWSTONE)

    if pyramidtype == 3:
        H2 = H
        for i in range(H):
            angle = 0
            for count in range(360):
                zdifference = round(math.sin(angle) * H2-i)
                xdifference = round(math.cos(angle) * H2-i)
                mc.setBlock(X+xdifference, Y+i, Z+zdifference, BLOCK)
                angle += 1
            H2 -= 1
            X += 1
            Z += 1
            sleep(SLEEP)
        mc.setBlock(X-H, Y+i+1, Z-H,param.GLOWSTONE)
        
    

    


if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    set_pyramid(3,15,63,12,8,0.1,param.SANDSTONE)
    



