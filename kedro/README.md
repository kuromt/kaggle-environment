[ドキュメント](https://kedro.readthedocs.io/en/stable/index.html)を読む

- kedro CLIのコマンド

```
root@d922d0431deb:~/get-started# kedro --help
Usage: kedro [OPTIONS] COMMAND [ARGS]...

  Kedro is a CLI for creating and using Kedro projects For more information,
  type ``kedro info``.

  When inside a Kedro project (created with `kedro new`) commands from the
  project's `kedro_cli.py` file will also be available here.

  Command line tools for manipulating a Kedro project.

Options:
  -V, --version  Show version and exit
  -v, --verbose  See extensive logging and error stack traces.
  -h, --help     Show this message and exit.

Global commands from Kedro
Commands:
  docs     See the kedro API docs and introductory tutorial.
  info     Get more information about kedro.
  new      Create a new kedro project.
  starter  Commands for working with project starters.

Project specific commands from /root/get-started/kedro_cli.py
Commands:
  activate-nbstripout  Install the nbstripout git hook to automatically...
  build-docs           Build the project documentation.
  build-reqs           Build the project dependency requirements.
  catalog              Commands for working with catalog.
  install              Install project dependencies from both...
  ipython              Open IPython with project specific variables loaded.
  jupyter              Open Jupyter Notebook / Lab with project specific...
  lint                 Run flake8, isort and (on Python >=3.6) black.
  package              Package the project as a Python egg and wheel.
  pipeline             Commands for working with pipelines.
  run                  Run the pipeline.
  test                 Run the test suite.
```

- パイプライン
    - 構成概念
        - Node: 処理単位. 関数. inputとoutputに名前をつける.
        - Pipeline: Nodeをつなげたもの. Nodeを複数与えて定義する.
        - DataCatalog: 扱うデータを宣言する.
        - Runner: Pipelineを実行するもの. PipelineとDataCatalogを扱う.
    - PipelineとDataCatalogが実験の再現性の肝
        - パラメータはパイプラインの外のProjectで管理
    - DataCatalogで扱えるデータ
        - 主にデータフォーマットごとに用意されている
            - データの用途(Bio, Geo)、ファイル形式（Parquet、CSV、Excel、Json, YAML）
        - 特定の処理エンジンで処理した結果を受け取るものもある
            - APIDataSet（HTTPで取得するデータ）, SQLTableDaset, SparkDataSet, TensorFlowModelDataSet
- Project
    - coockie-cutterの設定に従ってプロジェクトのディレクトリを作る
    - kedro newで作成する
    - kedro startersコマンドはProkectのboilerplateをカスタマイズできる
        - `kedro new --starter=https://github.com/quantumblacklabs/kedro-starter-pyspark.git`
        - ブランチやタグに設定があったとしても `--checkout` オプションで指定できる
            - `images`とか`commerce`のようなタグを用意しておけば用途ごとに使えるということ？
    - kedro runのオプション`--env`で実行するconfigを切り替えられる
        - conf/<env> のディレクトリにある設定を使った実行になる
        - 環境変数で指定することもできる
        ```bash
        root@d922d0431deb:~/get-started# export KEDRO_ENV=hoge
        root@d922d0431deb:~/get-started# kedro run 
        Traceback (most recent call last):
        File "/usr/local/bin/kedro", line 8, in <module>
            sys.exit(main())
        File "/usr/local/lib/python3.6/site-packages/kedro/framework/cli/cli.py", line 725, in main
            cli_collection()
        File "/usr/local/lib/python3.6/site-packages/click/core.py", line 829, in __call__
            return self.main(*args, **kwargs)
        File "/usr/local/lib/python3.6/site-packages/click/core.py", line 782, in main
            rv = self.invoke(ctx)
        File "/usr/local/lib/python3.6/site-packages/click/core.py", line 1259, in invoke
            return _process_result(sub_ctx.command.invoke(sub_ctx))
        File "/usr/local/lib/python3.6/site-packages/click/core.py", line 1066, in invoke
            return ctx.invoke(self.callback, **ctx.params)
        File "/usr/local/lib/python3.6/site-packages/click/core.py", line 610, in invoke
            return callback(*args, **kwargs)
        File "/root/get-started/kedro_cli.py", line 221, in run
            context = load_context(Path.cwd(), env=env, extra_params=params)
        File "/usr/local/lib/python3.6/site-packages/kedro/framework/context/context.py", line 893, in load_context
            context = context_class(project_path=project_path, **kwargs)
        File "/usr/local/lib/python3.6/site-packages/kedro/framework/context/context.py", line 252, in __init__
            self._setup_logging()
        File "/usr/local/lib/python3.6/site-packages/kedro/framework/context/context.py", line 530, in _setup_logging
            conf_logging = self.config_loader.get("logging*", "logging*/**", "**/logging*")
        File "/usr/local/lib/python3.6/site-packages/kedro/config/config.py", line 160, in get
            "or is not a valid directory: {0}".format(conf_path)
        ValueError: Given configuration path either does not exist or is not a valid directory: /root/get-started/conf/hoge
        ```
        - confを引き継いで一部を上書きすることも可能
            - 事情があってconfに従えない場合に便利
- DataCatalog
    - `catalog.yaml`に宣言
    - 保存場所以外に、ロードするときのDateのフォーマットやsplitの扱い方、ヘッダの有無などを記述できる
    - Transformerを使うとDataCatalogのデータをロードしたあとにhookできる
        - データのバリデーションやロードにかかる時間を測定したり、データ変換することもできる
        - 独自Transformerを作ることも可能
    - catalog.yamlの中で`versioned: True`にすることでバージョニングも可能
        - バージョンのデータはローカルに保存
        - バージョンの名前は`YYY-MM-DDThh.mm.ss.sssZ`
        - バージョンを指定する場合の例
        ```
        kedro run --load-version="cars.csv:YYYY-MM-DDThh.mm.ss.sssZ"
        ```
- Pipeline
    - PipeLineはモジュール化可能
        - 必ずREADME.mdを含んでいる必要がある。ここにパイプラインの説明を書くことを想定。
        - Pipelineごとにrequirement.txtを記述
    - `kedro pipeline package`コマンドでモジュール化したパイプラインをパッケージング
    - Pieplineをつなぎあわせるとき、同一の名前空間でConflictが発生する場合は自分で名前を変えること
    - Pipelineにはタグ付可能
- Runner
    - SequentialRunnerとParallelRunnerがある
        - ParallelRunnerではSparkDatasetが使えないことに注意
    - 自作のRunnerを作ることも可能
    - Pieplineの一部のNodeのみを実行することも可能(PertialRun)
        - タグで指定したりNodeを指定したり
        - デバッグするのに良さそう
- hook
    - Kedroの処理のいくつかでhookできる. hook処理でmlflowのtracking serverにメトリクスを送ることも可能.
    - 用意されているhook. errorが発生したときだけ呼ばれるhookがあるのは便利
        - after_catalog_created
        - before_node_run
        - after_node_run
        - on_node_error
        - before_pipeline_run
        - after_pipeline_run
        - on_pipeline_error
- plugin
    - kedroコマンドを拡張できる
        - kedroのPipelineをAirflowに変換するコマンドも


- 不明点
    - requirement.txtとrequirement.inの二つが同じディレクトリにできて内容は一緒。requirement.inは何に使われる？
        - 答え: `Note that src/requirements.in contains “source” requirements, while src/requirements.txt contains the compiled version of those and requires no manual updates.`
    - DataCatalogでHDFSやS3にあるデータをどうやって表現してどうやって取得する？コードで撮ってくるのか自動的にローカルにダウンロードするのか。
        - データの表現方法
            - pythonモジュールのfsspecで抽象化. protcol + url or pathでデータの保存場所を表現
        - ダウンロード方法
        ```
        # ioはDataCatalogのインスタンス
        cars = io.load("cars")  # data is now loaded as a DataFrame in 'cars'
        gear = cars["gear"].values
        ```
        - PertitionedDataはlazy loadされる
            - s3を使う場合の例
            ```yaml
            new_partitioned_dataset:
            type: PartitionedDataSet
            path: s3://my-bucket-name
            dataset: pandas.CSVDataSet
            filename_suffix: ".csv"
            ```



- typo in doc
    - リンク切れ
        - 02_get_started `kedro new --starter=https://github.com/quantumblack/kedro-starter-pyspark.git` -> `kedro new --starter=https://github.com/quantumblacklabs/kedro-starter-pyspark.git`
    - typo
        - 05_data `The are two ways` -> `They are two ways`