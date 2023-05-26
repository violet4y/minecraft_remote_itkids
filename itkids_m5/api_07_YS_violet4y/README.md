# minecraft_remote_itkids

Minecraft APIs made by IT Kids

## ----**07_YS violet4y API**----

ピラミッドを作るコード

[<img src="./images/api.png" width="400">](./images/api.png)[<img src="./images/diagonal-pyramids.png" width="400">](./images/diagonal-pyramids.png)


## [api_violet4y.py](api_violet4y.py)
ピラミッドを作るコードです。x,y,zの座標、高さ、作成速度を設定できます。

```
pyramid.set_pyramid(pyramidtype=1, X=10, Y=63, Z=10, H=6, SLEEP=0.5, BLOCK=param.GOLD_BLOCK)
```
```
pyramid.set_pyramid_diagonal(X=10, Y=63, Z=10, H=5, SLEEP=0.1, BLOCK=param.GOLD_BLOCK)
```

## --**コードについて** <set_pyramid>--
---

## *pyramidtype*

pyramidtype=1   ---row---  
1列ずつ作成します。

[<img src="./images/api_row.png" width="300">](./images/api_row.png)


pyramidtype=2  ---block---  
1ブロックずつ作成します。

[<img src="./images/api_block.png" width="300">](./images/api_block.png)

## *X,Y,Z,H*

ピラミッドを作る座標を決めます。
指定した座標から  
xのプラス方向へ、yのプラス方向へ、zのプラス方向へと作成します。
Hに数値を入れることでピラミッドの高さが決まります。

| H | 4 | 5 | 6 | 7 |
|:---|:---:|:---:|:---:|:---:|
|横幅|7|9|11|13|
|画像|[<img src="./images/pyramid-4height.png" width="300">](./images/pyramid-4height.png)|[<img src="./images/pyramid-5height.png" width="300">](./images/pyramid-5height.png)|[<img src="./images/pyramid-6height.png" width="300">](./images/pyramid-6height.png)|[<img src="./images/pyramid-7height.png" width="300">](./images/pyramid-7height.png)|

## *SLEEP*

列やブロックを設置した後、次に設置するまでも待機秒数です。

## *BLOCK*

ピラミッドを構築するブロックを指定できます。

|param.IRON_BLOCK|param.GOLD_BLOCK|param.DIAMOND_BLOCK|
|---|---|---|
|[<img src="./images/pyramid-iron.png" width="300">](./images/pyramid-iron.png)|[<img src="./images/pyramid-gold.png" width="300">](./images/pyramid-gold.png)|[<img src="./images/pyramid-diamond.png" width="300">](./images/pyramid-diamond.png)|

---
## --**コードについて** <set_pyramid_diagonal>--

| H | 4 | 5 | 6 | 7 |
|:---|:---:|:---:|:---:|:---:|
|横幅|7|9|11|13|
|画像|[<img src="./images/dia-4hei.png" width="300">](./images/dia-4hei.png)|[<img src="./images/dia-5hei.png" width="300">](./images/dia-5hei.png)|[<img src="./images/dia-6hei.png" width="300">](./images/dia-6hei.png)|[<img src="./images/dia-7hei.png" width="300">](./images/dia-7hei.png)|