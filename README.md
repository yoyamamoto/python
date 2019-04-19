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
- お気楽 Python プログラミング入門
http://www.nct9.ne.jp/m_hiroi/light/index.html#python
- tkinter GUI モジュール
https://docs.python.org/ja/3.6/library/tkinter.html#tkinter-modules
- PythonのGUI Toolkit比較(Tkinter, PyQt5, wxPython) パーティクルのアニメーション
https://pid123.blogspot.com/2017/08/python-gui-toolkit.html
- PythonのTkinterを使ってみる
https://qiita.com/nnahito/items/ad1428a30738b3d93762


## 仮想環境構築 インストール
- python 3.3以上から、vertualenvはpythonに組み込まれ、venvという仮想環境を構築できるがある模様。

### 仮想環境構築
    # python 3.6.8をインストール
    # Powershellで仮想環境を一時的に実行する方法
    Set-ExecutionPolicy RemoteSigned -Scope Process
    # 仮想環境ENV（*任意）を構築する ← tensorflowを使うにはpython 3.6.6以下でないといけないのでversion指定をする
    $ python -m venv ./ENV
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

# 進捗
- python標準機能venvで仮想環境を構築し、無事tensorflowをインストールできたとおもったら、アクセスが拒否されましたとエラーが出てきてオコ。

# 問題点20190412
- Win10 64bit、Python3.6.8のインストール時に、全ユーザ共通フォルダ/root/"program file"/へインストールすると、pipでパッケージをインストールした際に環境Pathが設定されない。
- Win10 64bit、python3.6.8でvirtualenvをpipでインストールすると環境構築後の./ENV/Scripts/フォルダ内にactivateが生成されない。
- gitとGithubを上手く使えなくて挫折しそう

# Gitメモ
## Gitコマンド
- git init                      ：空のリポジトリを作成
- git branch                    ：ブランチの一覧
- git branch -r                 ：リモートブランチの一覧
- git branch ブランチ名          ：ブランチの作成
- git branch -d ブランチ名       ：ブランチの削除
- git branch -m ブランチ名       ：ブランチ名の変更
- git checkout ブランチ名        ：ブランチへ移動
- git add ファイル名             ：ファイル名をステージング
- git add -u                    ：変更したファイルをすべてステージング
- git rm --cached ファイル名     ：ステージング上（リモートブランチ）にあるファイルを削除
- git commit -m 'メッセージ'     ：ステージングしたファイルにメッセージを付けてコミット
- git commit -a -m 'メッセージ'  ：変更したファイルをステージングしてメッセージを付けてコミット（add+commit）
- git reset --soft HEAD~2       ：コミット履歴のみ2件バックデート
- git reset --hard HEAD~2       ：コミット履歴とファイルを2件バックデート
- git rebase -i HEAD~2          ：コミット履歴2件分のメッセージを編集 or 削除してバックデート
- git rebase --continue         ：リベースした後はコンテニューしとく？？？？←なんで？
- git push                      ：コミットをリモートブランチへ登録
- git push --delete ブランチ名   ：リモートブランチを削除
- git pull origin ブランチ名     ：リモートブランチの最新データをダウンロードして同名のローカルブランチへマージ
- git fetch                     ：fetch＋merge ＝ pull リモートブランチから、ブランチ、タグなどを取得
- git merge ブランチ名           ：masterブランチに移動した状態で行う。マージ後はリモート origin/masterへpushする
- git push origin master        ：masterブランチをチェックアウトした状態で、origin/masterへpush
- git merge --abort             ：マージをいったん取り消す
- git diff ファイル名とかブランチ名とか：差分ファイルの確認色々。Githubを使っている場合はオンラインGUI上で確認できる
- git log                       ：コミットログを見る。Github(以降 同上)
- git mv 変更前ファイル名 変更後  ：ファイル名の変更。
- git clean -xn ディレクトリ     ：追跡対象となっていないファイルを削除。-nオプションで実際には実行されない。-xで.gitignoreも対象に。

## Gitの七不思議
- ローカル・リモートブランチdevelopを消して、新たに同名のローカルブランチdevelopを作り直すと、消したはずのファイルが復活している。なんで？？？？？？？
- rebase -i HEAD~10 とかのrebaseコマンドでコミット履歴 だけ を削除したいのにファイルまで戻る。reset soft をたたくとエラーがです。なんで？？？？？？？？？？

