import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.interpolate
from mpl_toolkits.axes_grid1 import make_axes_locatable
from PIL import Image

def Ddraw():
    print("【はじめに】")
    print("csvファイルには,1列目に緯度データ,2列目に経度データ,3列目に降水量データを入力しておく必要があります.")
    print("プログラムを実行するには,最低3地点分のデータが必要となります")
    print("csvファイルに半角数字以外のデータが存在すると,プログラムが実行できません.")
    print("地図データはこの「csv_contour.py」と同じ階層に入れてください.")
    print("")
    print("次の質問Aに対して,0か1の半角数字で入力し,Enterキーを押してください.")
    i_see = int(input("A.【はじめに】が理解できましたか.【0:はい】【1:いいえ】: "))

    if i_see == 1:
        print("お手数ですが,再度実行してください.")

    else:
        #データを読み取る
        csv_name = input("csvファイルの名前を入力してください(拡張子はなくても良いです)【例:201710】: ")
        csv_read = np.loadtxt("./csv/" + ("{}").format(csv_name) + ".csv", delimiter=",")
        x = csv_read[:,1]
        y = csv_read[:,0]
        z = csv_read[:,2]

        #グリッドデータを作成する
        xi, yi = np.linspace(x.min()-0.1, x.max()+0.1, 100), np.linspace(y.min()-0.1, y.max()+0.1, 100)
        xi, yi = np.meshgrid(xi, yi)

        #降水量データを内挿する
        rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
        zi = rbf(xi, yi)

        #キャンパス描画(figureオブジェクトの作成)
        fig = plt.figure(figsize=(10,10))
        #plt.title('accumulated precipitation [mm] 2020/06 ', {'fontsize':15})

        #グラフをプロット(figureオブジェクトに属するaxesオブジェクトを作成)
        #引数の1,1,1は1行1列1個目のグラフ
        graph_title = input("描画するグラフのタイトルを入力してください: ")
        ax = fig.add_subplot(1, 1, 1,
        title=('{}').format(graph_title),
        xlabel='lon',ylabel='lat',
        projection=ccrs.PlateCarree())

        #地図描画
        ax.coastlines('10m')
        #県境と市町村境界を表示
        adm1_shapes = list(shpreader.Reader("./gadm36_JPN_shp/gadm36_JPN_1.shp").geometries())
        adm2_shapes = list(shpreader.Reader("./gadm36_JPN_shp/gadm36_JPN_2.shp").geometries())

        ax.add_geometries(adm2_shapes, ccrs.PlateCarree(),
                          edgecolor='gray', alpha=0.05)
        ax.add_geometries(adm1_shapes, ccrs.PlateCarree(),
                          facecolor='white',edgecolor='black',alpha=0.05)

        #描画範囲を指定
        ax.set_extent([xi.min(),xi.max(),yi.min(),yi.max()],ccrs.PlateCarree())

        #コンター図の作成.
        #カラーは気象庁の指針に従う.
        #カラーの閾値を設定する.
        level1 = input("レベル1の降水量閾値を半角数字で入力してください【例:0】: ")
        level2 = input("レベル2の降水量閾値を半角数字で入力してください【例:50】: ")
        level3 = input("レベル3の降水量閾値を半角数字で入力してください【例:100】: ")
        level4 = input("レベル4の降水量閾値を半角数字で入力してください【例:200】: ")
        level5 = input("レベル5の降水量閾値を半角数字で入力してください【例:300】: ")
        level6 = input("レベル6の降水量閾値を半角数字で入力してください【例:500】: ")
        level7 = input("レベル7の降水量閾値を半角数字で入力してください【例:800】: ")
        level8 = input("レベル8の降水量閾値を半角数字で入力してください【例:1200】: ")
        level9 = input("レベル9の降水量閾値を半角数字で入力してください【例:1800】: ")

        contour = ax.contourf(xi, yi, zi,levels=[level1,level2,level3,level4,level5,level6,level7,level8,level9],colors=['#f2f2ff','#a0d2ff','#218cff','#0041ff','#faf500',"#ff9900","#ff2800","#b40068"],
                    alpha=0.95, transform=ccrs.PlateCarree())

        #カラーバーの作成.
        clb = plt.colorbar(contour,pad=0.03,shrink=0.50)

        #コンター図の保存.
        dpi_value = input("保存する画像の解像度(dpi)を半角数字で入力してください【例:500】: ")
        fig.savefig("./img/"+ ('{}').format(graph_title) +".png",dpi=500)

        #画像を切り取って,上書き保存する.
        im = Image.open("./img/"+ ('{}').format(graph_title) +".png")
        im.crop((600, 1000, 4300, 4000)).save("./img/"+ ('{}').format(graph_title) +".png", quality=95)
