# ピラミッド作成プログラム
from mcje.minecraft import Minecraft
import param_MCJE as param

"voplet4y API"


import pyramid

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("violet4y api build a pyramid!!")

# pyramidtype = 1...    build a pyramid by 1 row
# pyramidtype = 2...    build a pyramid by 1 block
pyramid.set_pyramid(pyramidtype=1, X=10, Y=63, Z=10, H=6, SLEEP=0.5, BLOCK=param.GOLD_BLOCK)

mc.postToChat("finish")
