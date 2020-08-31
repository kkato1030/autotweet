# Tweet Automation Test

Selenium の扱い方をカンタンに学ぶため Twitter にてツイートを行う実装をしました。
非常に簡易的な実装ですが Selenium の使い方をざっくり確認するためにご利用ください。

## 動作環境

以下の環境で動作を確認しています。

- macOS Catalina
- Python 3.8
- Google Chrome version 85

Chrome および Python のインストールは必須となりますので事前に実行しておいてください。

## 留意事項

- このスクリプトは 2020/08/31 に作成されています
- twitter.com の仕様の変更により正常に動かなくなる場合がありますのでご注意ください
- このスクリプトを用いて大量のツイートを投稿するような利用方法はおやめください(あくまでもSeleniumのテスト用のスクリプトであることご留意ください)

## Set up

**Clone**

```
$ git clone https://github.com/kkato1030/autotweet.git
$ cd autotweet
```

**Install Package**

通常インストール

```
$ pip install -r requirements.txt
```

(補足) pipenv を用いたインストール

```
$ pipenv install
```

**Set Username / Password**

Twitter ログイン用の Username / Password を設定します

```
$ cp login.json.test login.json
$ vi login.json
```

## Use

以下コマンドで Twitter のページが立ち上がり、自動でツイートが投稿されます。

```
$ export PATH=$PATH:`chromedriver-path`  # 新しくterminalを開く度、実行
$ python tweet.py
```

## エラーが発生したら

`This version of ChromeDriver only supports Chrome version xx` というエラーが発生する場合、ご利用のChromeバージョンが古い可能性があります。
アップデートがないか確認していただき、最新の Chrome をインストールしてください。
