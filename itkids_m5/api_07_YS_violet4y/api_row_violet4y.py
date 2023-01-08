# ピラミッド作成プログラム
from mcje.minecraft import Minecraft
import param_MCJE as param

"量産型"

import pyramid_row
import pyramid_single

mc = Minecraft.create(port=param.PORT_MC)  # MCJE:14712, MCPI:4711
mc.postToChat("demo4-set pyramid!!")

pyramid_row.set_pyramid(X=10, Y=63, Z=10, H=6, SLEEP=0.5, BLOCK=param.GOLD_BLOCK)

mc.postToChat("finish")
