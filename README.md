
## the map of tongliao-universe 通辽宇宙地图

作为小约翰可汗的歌迷，为可汗献图大家可以理解吧。

### preview 预览

![通辽宇宙地图预览](/tongliao-universe.png)

### basic info 通辽宇宙基本信息

**capital 通辽宇宙首府：** 内蒙古通辽市

![通辽宇宙地图](/favicon.ico)

**the supreme leader 最高领导人：** 小约翰可汗 

![耗子头像](/john.jpg)


Our great and supreme Great Khan of Tongliao is in a superposition of the Dusk Sovereign and the Ming Emperor, and his rule is not perfect, but his rule is great, his rule is brilliant, and his rule is irreplaceable. When Little John was updated, John was in the state of a king, receiving "Khan Diligence", "The Supreme King, Little John Come Back To His Loyal Bilibili" and many other positive buffs for one to two weeks. When Little John does not update, when John is in a comatose state, at this time the folk style evaluation begins to decline, the Diao people will urge changes on various platforms, "dead rats quickly update" is the common term of the Diao people.

我们伟大至高的通辽大可汗处于昏君与明君的叠加态，他的统治并不是完美的，但是他的统治是伟大的，他的统治是光辉的，他的统治是不可替代的。当小约翰更新时进行观测，此时约翰处于明君态，获得“可汗勤政”、“The Supreme King, Little John Come Back To His Loyal Bilibili”等等诸多正面Buff，持续一到两周。当小约翰不更新时进行观测，此时约翰处于昏君态，此时民间风评开始下降，刁民们将在各个平台上催更，“死耗子快更新”是刁民们的常用催更用语。


**basic area unit 通辽宇宙基本面积单位：** 通辽，记作T，通辽，简写T，总面积59535平方千米。

**Basic population units 通辽宇宙基本人口单位：** 大单位：天通苑，约50万人；小单位：回龙观，约30万人。


## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Build

```sh
npm run build-only
```

### Build docker image
```
docker build -t tongliao-universe .
```

### run docker 
```shell
docker run -p 8080:80 --name tongliao-universe -d tongliao-universe
```

## 本站技术分析

总的来说，项目包括数据获取与数据展示部分。其中工作量主要在界面绘制与数据整理。

### 界面部分
界面使用echarts + vue  + antdv处理。echarts主要用来处理大地图展示地图geo数据，antdv提供界面组件。地图展示有我们自己标注的数据需要手动渲染处理一下。

### 数据部分
数据包括两个，一是up主小约翰可汗的视频数据与up信息数据的爬取与整理，二是世界地图数据的获取与整理。视频信息与up可以通过接口爬取，这里使用了python写了一个爬虫工具将数据存在json文件了，但是直接获取到的数据是不能直接使用的，需要识别出视频内容讲的是什么人什么国家什么组织，有的视频会在视频简介中写明，有些则没有，一个通用的方式是，提取视频语音转成文字后交给AI提取主题，但是这个硬件要求太高了，我这个办公本显然不能胜任，最后还是选择手动补全。地图数据网上是可以找到的，但是通辽、回龙观与天通苑是需要自己手动标注的，于是自己标了一下，非专业人士，所以不太美观。