# Backup_of_folders_and_creation_of_databases_WP
Backup of folders and creation of databases For Windows By Python

フォルダを別の場所にコピー（バックアップ）しつつ、内容をデータベース化するツールです。  
バックアップするだけならツールを見かけるが、データベース化は無いため別途作成  
データベース化は差分バックアップを効率化するために利用を想定

以下の環境で作成
* 言語：Python3　（スクリプト系の言語の学習が目的、また、ライブラリが豊富なため）
* OS：Windows10 Home
  * 各種設定は日本
* その他ツール
  * Visual Studio Code
  * Chat GPT（困ったときに利用）

---
2024/07/19時点
* 実行方法
  * コマンドプロンプト起動
  * ソースファイルの有る場所をカレントディレクトリとする
  * 実行方法
    > python BackupAndDatabase.py コピー元フォルダ コピー先フォルダ
  * 実行コマンド例
    > python BackupAndDatabase.py E:\test\写真 D:\temp
* 実行結果の例
    > 0% (0MB/2,078MB)  
10% (212MB/2,078MB)  
20% (420MB/2,078MB)  
30% (626MB/2,078MB)  
40% (833MB/2,078MB)  
50% (1,040MB/2,078MB)  
60% (1,247MB/2,078MB)  
70% (1,457MB/2,078MB)  
80% (1,663MB/2,078MB)  
90% (1,872MB/2,078MB)  
100% (2,078MB/2,078MB)  

* コピー元フォルダ または コピー先フォルダ が存在しない場合はエラーメッセージを表示して終了する

* コードに関するメモ
  * sys.argvを使用してコマンドライン引数を処理し、コピー元フォルダとコピー先フォルダを取得
  * os.path.existsを使用してフォルダの存在を確認し、存在しない場合はエラーメッセージを表示
  * shutil.copytreeを使用してフォルダをコピーし、進捗状況を表示