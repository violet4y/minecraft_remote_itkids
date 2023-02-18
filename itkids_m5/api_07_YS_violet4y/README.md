# minecraft_remote_itkids

Minecraft APIs made by IT Kids

## ----**07_YS violet4y API**----
---
ピラミッドを作るコード

[<img src="./api.png" width="500">](./api.png)

## [api_violet4y.py](api_violet4y.py)
ピラミッドを作るコードです。x,y,zの座標、高さ、作成速度を設定できます。

```
pyramid.set_pyramid(pyramidtype=1, X=10, Y=63, Z=10, H=6, SLEEP=0.5, BLOCK=param.GOLD_BLOCK)
```

## **コードについて**
---

## *pyramidtype*
---
pyramidtype=1   ---row---  
1列ずつ作成します。

[<img src="./api_row.png" width="300">](./api_row.png)


pyramidtype=2  ---block---  
1ブロックずつ作成します。

[<img src="./api_block.png" width="300">](./api_block.png)

## *X,Y,Z,H*
---
ピラミッドを作る座標を決めます。
指定した座標から  
xのプラス方向へ、yのプラス方向へ、zのプラス方向へと作成します。
Hに数値を入れることでピラミッドの高さが決まります。

| H | 4 | 5 | 6 | 7 |
|:---|:---:|:---:|:---:|:---:|
|横幅|7|9|11|13|
|画像|[<img src="./pyramid-4height.png" width="300">](./pyramid-4height.png)|[<img src="./pyramid-5height.png" width="300">](./pyramid-5height.png)|[<img src="./pyramid-6height.png" width="300">](./pyramid-6height.png)|[<img src="./pyramid-7height.png" width="300">](./pyramid-7height.png)|

## *SLEEP*
---
列やブロックを設置した後、次に設置するまでも待機秒数です。

## *BLOCK*
---
ピラミッドを構築するブロックを指定できます。
