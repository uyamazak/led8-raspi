# led8-raspi
プロジェクトLED8 は Raspberry PiとFirebaseとVue.jsを用いて、uyamazak自宅に設置された8個のLEDを光らせるプロジェクトです。

このレポジトリは[Raspberry Pi Zero WH](https://amzn.to/2yisD3a)の上で動かすPythonのスクリプトです。

もう一つFirebase Hostingで動作させる**led8-firebase**が別レポジトリにあり、2つセットで動作します。

# 処理概要
1. **led8-firebase** によるFirestoreのCollectionへの書き込みを監視する
1. 書き込みされたら、データから光らせるLEDの配列を取得
1. 配列にあるキーのLEDを光らせる
1. n秒間更新が無かったら、[カメラ](https://amzn.to/2yjjxTy)で写真を取る（フラッシュ用に8個とは別の白色LEDを使用）
1. 写真のデータをFirebase Storageに保存して、公開用URLを作成する
1. 公開用URLとともに撮影時間などのデータをFirestoreに追加
