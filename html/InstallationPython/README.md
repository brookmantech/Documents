#Python環境の立ち上げ方

ここでは  

>・windows7 x32  
>・Anaconda（Continuum Analytics社製Pythonディストリビューション

を使用し、画像処理ができるところまで進めてみます。  

オールインワンでAnacondaらくちんです。

##Anacondaのダウンロード

https://www.continuum.io/ からダウンロードします。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/01.JPG" width="400">

Python3.xと2.7は互換性が低く、2.7は開発も終わっています。  
用途的に特に困ることもないのでおとなしく3.xを選びましょう

x64/x32はPCに合わせましょう。  
過去x64はバグが多かったようですが、解決されてきているようです。  
メモリサイズ考えるとx64の方がいいかもしれません。しりませんが。

##Anacondaのインストール

###1.ダウンロードが終わったら、ダブルクリック。

[Next]を押して次に進みましょう。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/02.JPG" width="400">

###2.ライセンス条項

ちゃんと読みましょう。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/03.JPG" width="400">

###3.インストール先アカウント選択

社内PCの場合は、管理者に確認しましょう。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/04.JPG" width="400">

続いてインストール先を聞かれますので、問題がなければそのまま[Next]

###4.環境変数、PythonのVerの登録

特に問題なければそのまま両方?で。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/05.JPG" width="400">

あとはそのまま、[Finish]まで進めましょう。  
最後にAnaconda CLOUD勧められますが、特に無視しても問題ありません。

##OpenCVパッケージのインストール

Anacondaでは標準で複数のパッケージが導入済みですがOpenCVは入っていません。  
導入しましょう。  
Anacondaではcondaというパッケージ管理システムが使えます。

スタートメニューからAnaconda Promptを立ち上げます

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/06.JPG" width="400">
<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/07.JPG" width="400">

以下のコマンドを入力します

> c:\\\>conda install -c https://conda.anaconda.org/menpo opencv3

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/08.JPG" width="400">

既に入っている場合はバージョンチェックしてくれます。 

が

管理者実行していなかったために怒られてしまいました。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/09.JPG" width="400">

その場合はショートカットアイコンを右クリックして[管理者として実行(A)]で起動しなおしましょう。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/10.JPG" width="400">

[y]を入力して次に進みます。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/11.JPG" width="400">

今度はうまくいったようです。  
それでは、そのまま下記のようにコマンド入力して、Pythonからインストールの可否もチェックもしてみましょう。

> c:\\\>python  
> \>\>\>import cv2  
> \>\>\>cv2.\_\_version\_\_  

なんでcv"2"やねん。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/12.JPG" width="400">

大丈夫そうです。

##IDEの使用

コマンドプロンプトでそのままプログラミングしても構いませんが  
折角なのでIDE（統合開発環境）を使用してrichにプログラミングしましょう。

AnacondaではSpyderがインストールされています。  
ふたたび、スタートメニューからSpyderを立ち上げます。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/06.JPG" width="400">

起動時にネットワークセキュリティー訊かれます。

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/13.JPG" width="400">

セキュリティー設定をした後に、もしかするとアップデート案内が表示されるかもしれません。  
無慈悲な心で閉じてしまいましょう。  
（condaからupdateできます）

<img src="https://raw.githubusercontent.com/brookmantech/Documents/master/html/InstallationPython/image/14.JPG" width="400">

無事？起動して準備完了です。  
お疲れさまでした。
