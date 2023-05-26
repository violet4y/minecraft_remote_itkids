# ピラミッド作成プログラム
from mcje.minecraft import Minecraft
import param_MCJE as param
from time import sleep

"pyramidのapi"
"kadai_08_violet4yの元"

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711

def set_pyramid(pyramidtype=1, X=10, Y=63, Z=10, H=6, SLEEP=0.8, BLOCK=param.GOLD_BLOCK):
    POS = 0   #位置情報
    mc.setBlocks(X, Y, Z, X+2*H-2, Y+H+1, Z+2*H-2, param.AIR)
    sleep(2)

    if pyramidtype == 1:    
        mc.postToChat("build a pyramid by 1 row...")
        for i in range(H+1):
            for i in range(2*H-1-POS*2):
                mc.setBlocks(X+POS, Y+POS, Z+POS, X+2*H-2-POS, Y+POS, Z+POS, BLOCK)
                Z += 1
                sleep(SLEEP)
            Z -= 2*H-1-POS*2
            POS += 1    

    if pyramidtype == 2:
        XPOS = 0
        mc.postToChat("build a pyramid by 1 block...")
        for i in range(H+1):
            for i in range(2*H-1-POS*2):
                for i in range(2*H-1-POS*2):
                    mc.setBlock(X+POS+XPOS, Y+POS, Z+POS, BLOCK)
                    XPOS += 1
                    sleep(SLEEP/5)
                Z += 1
                XPOS = 0
                sleep(SLEEP)
            Z -= 2*H-1-POS*2
            POS += 1
    

    mc.setBlock(X+POS-2, Y+POS-2, Z+POS-3, param.GLOWSTONE)


def set_pyramid_diagonal(X=10, Y=63, Z=10, H=5, SLEEP=0.1, BLOCK=param.GOLD_BLOCK):
    mc.postToChat("create a pyramid")
    sleep(3)
    for count in range(H):
        xdifference = H-1-count
        zdifference = 0
        while zdifference < H-count:
            mc.setBlocks(X+xdifference, Y+count, Z+zdifference, X-xdifference, Y+count, Z-zdifference, BLOCK)
            xdifference -= 1
            zdifference += 1
            sleep(SLEEP)
    mc.setBlock(X, Y+H-1, Z, param.GLOWSTONE)
    


if __name__ == "__main__":
    mc = Minecraft.create(port=param.PORT_MC)
    set_pyramid_diagonal(-5,63,5,9,0.1,param.SANDSTONE)
    #set_pyramid(X=10, Z=10, Y=63, H=6, SLEEP=0.3, BLOCK=param.GOLD_BLOCK)



