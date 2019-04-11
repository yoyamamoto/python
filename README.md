# PythonとGithubを適当に覚えるはろーわーるど
はろーわーるど

## やりたい
- ０１） 人物が映った写真をアップロードすると、自動で人物を自動判別して切り抜いてくれる。fork元サービス：https://www.remove.bg/
- ０２） スマホで写真を撮ると自動で釣った魚が何か判別してくれる。

## ざっくりとした流れ
０１）
1. OpenCVをインストールします。https://docs.opencv.org/master/d3/d52/tutorial_windows_install.html
1. JPG or PNGファイルをアップロードします。
1. OpenCVが良い感じに色々やってくれます。
1. 切り抜かれた画像が出力・保存されます。

０２）
1. TensorFlowで画像認識させます。https://www.tensorflow.org/
1. チュートリアル通りに作ります。
1. なんかいい感じにできます。

※ TensorFlowで画像認識「〇〇判別機」を作る
https://qiita.com/too-ai/items/4fad0239b8b3c465fe6d

## Pythonの基本
- Pythonビギナーズガイド（導入編）
https://qiita.com/egoa56/items/d39463ee9d8ba032666b
- Pythonビギナーズガイド（変数・配列編）
https://qiita.com/egoa56/items/a74e1aa64bec603d15cd
- Pythonビギナーズガイド（関数編）
https://qiita.com/egoa56/items/03a9ce47ac46981d9e8b
- Pythonのコードをきれいに書くコツ
https://qiita.com/yinawekuky/items/28d973a653e9825ed582
- Pythonの公式ドキュメント 9. クラス
https://docs.python.org/ja/3/tutorial/classes.html#class-definition-syntax

## 仮想環境構築 インストール
- 公式
https://virtualenv.pypa.io/en/stable/installation/
- Qiita virtualenvでpython環境を管理する
https://qiita.com/caad1229/items/325ca5c8ad198b0ebce7

### 仮想環境構築
    # Powershellで仮想環境を一時的に実行する方法
    Set-ExecutionPolicy RemoteSigned -Scope Process
    # 仮想環境ENV（*任意）を構築する ← tensorflowを使うにはpython 3.6.6以下でないといけないのでversion指定をする
    $ virtualenv --no-site-packages ./ENV
    # 仮想環境を起動
    $ ./ENV/Scripts/activate
    # 仮想環境を終了
    (ENV)$ deactivate
    # 仮想環境（ENV）へパッケージのインストール
    (ENV)$ pip install --upgrade pip
    (ENV)$ pip list
    (ENV)$ pip install パッケージ
    (ENV)$ pip install --upgrade tensorflow
    (ENV)$ python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"

https://www.tensorflow.org/install/pip

## gitとGithubを上手く使えなくて挫折しそう
## .gitignore処理
