# PreContour_Py
"PreContour_Py"は,降水量のコンター図を描くPythonパッケージです.

# デモ
任意の"範囲","閾値"で降水量のコンター図を描くことができます.
![](https://github.com/KodaiTamaki/PreContour_Py/blob/master/img/201710.png)
 
# 特徴
"PreContour_Py"のディレクトリ構成は以下の通りです.

```
PreContour_Py
│  customized_contour.py
│  default_contour.py
├─csv
├─gadm36_JPN_shp
└─img
```

* "default_contour.py"は,CUI操作でグラフの設定(範囲,閾値,グラフタイトル)を行うことができます.
* "customized_contour.py"は,ソースコードを編集し,グラフの設定が自由に行うことができます.(※コメントアウトを充実させて,後日コミットします.)
* "csv"は,緯度,経度,降水量データが入ったcsvファイルを格納するディレクトリです.
* "img"は,コンター図を出力するディレクトリです.
* [gadm36_JPN_shp](https://gadm.org/download_country_v3.html)は,地図描画用のデータが格納されたディレクトリです.

# 必要要件
OS:Windows,Python:anacondaの環境下であることを前提とします.

作成者の実行環境は以下の通りです.
* Windows 10
* Anaconda 4.8.2 (64-bit)

※後日,Ubuntu(Linux環境)でテストを行います.

 
# インストール
* Anaconda (Pythonディストリビューションのひとつ)
* Cartopy (地図描画のPythonライブラリ)

➀Anacondaのインストールは[こちら](https://www.anaconda.com/distribution/)

➁Anaconda Promptを起動し,[Cartopy](https://scitools.org.uk/cartopy/docs/latest/#)をcondaコマンドでインストール
```
conda install -c conda-forge cartopy
```

# 使用方法

➀Anaconda Promptを起動し,"PreContour_Py"ディレクトリに移動する.
```
cd ***/PreContour_Py
```

➁"default_contour.py"か"customized_contour.py"を実行.
```
python default_contour.py
Or
python customized_contour.py
```
 
# その他
* サンプルデータ"PreContour_Py/csv/201710.csv"は,["気象庁-過去の気象データ"](https://www.data.jma.go.jp/obd/stats/etrn/index.php)から作成しました.
* カラーバーは,["気象庁ホームページにおける気象情報の配色に関する設定指針"](https://www.jma.go.jp/jma/kishou/info/colorguide/120524_hpcolorguide.pdf)を参考にしました.

# 作成者
タマキ コウダイ
 
# ライセンス
"PreContour_Py"は,"MITLicense"が適用されます.
