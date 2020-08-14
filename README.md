# How to build

```
$ docker-compose build
```

# How to run

create .env file

```.env
MYSQL_ROOT_PASSWORD="mlflow-password"
MYSQL_DATABASE="mlflow"
MYSQL_USER="mlflow"
MYSQL_PASSWORD="mlflow-password"
TZ="Asia/Tokyo"
```

run containers.

```
$ docker-compose up -d 
```

# How to use

- Mlflow: http://localhost
- Jupyter: http://localhost:8080
  - password is required. Look log.
  ```
  $ docker-compose logs notebook
  ```

# In Notebok

1. After Creating New API Token for Kaggle, copy `kaggle.json` to `data/notebook` directory.

2. In notebook, copy `kaggle.json` to `$HOME/.kaggle/`.

3. Getting Completition's file.

```
jovyan@6f527af2d99b:~$ mkdir .kaggle
jovyan@6f527af2d99b:~$ mv kaggle.json .kaggle/
Error: no such option: --project_name

# create kedro project. i.e. titanic
jovyan@6f527af2d99b:~$ kedro new
Project Name:
=============
Please enter a human readable name for your new project.
Spaces and punctuation are allowed.
 [New Kedro Project]: titanic

Repository Name:
================
Please enter a directory name for your new project repository.
Alphanumeric characters, hyphens and underscores are allowed.
Lowercase is recommended.
 [titanic]: titanic

Python Package Name:
====================
Please enter a valid Python package name for your project package.
Alphanumeric characters and underscores are allowed.
Lowercase is recommended. Package name must start with a letter or underscore.
 [titanic]: titanic

Generate Example Pipeline:
==========================
Do you want to generate an example pipeline in your project?
Good for first-time users. (default=N)
 [y/N]: N

# load competition data
jovyan@6f527af2d99b:~$ kaggle competitions download -c titanic -p titanic/data/01_raw/
Warning: Your Kaggle API key is readable by other users on this system! To fix this, you can run 'chmod 600 /home/jovyan/.kaggle/kaggle.json'
Downloading titanic.zip to titanic/data/01_raw
  0%|                                                                                                                                         | 0.00/34.1k [00:00<?, ?B/s]
100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 34.1k/34.1k [00:00<00:00, 4.18MB/s]
```


# memo

- kedo newでプロジェクトを作る
- 最初の試行錯誤
    - `data/01_raw/`にあるデータから欠損値を補ったりone-hot encodinfしたtrain用データを作る.
        - assertを使ってtraindataのvalidationを実施する
            - 文字列データを許すのかなど全てこの段階で終わらせる
            - 意図した変換があればコメントやvalidationで記録しておく
                - validationのコードで足りないものは必ずコメントも書く 
    - 作ったtrain_dataをCataLogDatasetに登録する
        - あわせてmlflowのartifactに登録する
    - 整形が終わった学習用データを02_intermediateにCSVファイルとして保存
    - 上記のCSVをmlflowのartifactにも保存
- notebookをpythonスクリプトに変換
    ```
    $ jovyan@6f27db85a99d:~/titanic/src$ jupyter nbconvert --to script eda.ipynb
    ```

# 疑問

- catalog.yamlは人間が書くのかAPIを操作すると自動的にかかれるのかどっち？
    - 今のところ自分で書かないといけなさそう.ある程度固まったらデータをファイルに保存したあとにcatalog.ymlに記述する。
        - DataCatalod.addやDataCatalog.saveにcatalog.yamlにメタ情報を追記する機能はなかった
    - 記述したファイルはmlflowのartifactに登録して、catalog.ymlでもそれに対応した方法で書いておくのが良さそう。
        - つまり、生データの試行錯誤がある程度終わったらmlflowのexperimentを作成するのがよい
- 中間データをmlflowのartifactの場所に指定すればいいのか、kedroの02_intermediateの下に配置すればいいのか分からない
    - mlflowのartifactの場所を02_intermediateにすれば解決しそうだが、mlflowのartifactはデータの永続化が必要なのでコンテナ起動時に外部ストレージをあらかじめマウントしておく必要がある一方で、コンテナが立ち上がったとkedroのprojectの作成コマンドを叩くまでは02_intermediateディレクトリが存在しないのであらかじめマウントすることはできない
    - mlflowのget_artifactとkedroのcatalog.ymlがそれぞれ別々のパスを指すことになる
        - mlflowのartifactはバックアップと見なすのがいい？
        - それとも02_intermediateではなくcatalog.ymlでartifactを指す？ただそれだとせっかくのディレクトリ構造を統一しようとする試みが破綻する。。。