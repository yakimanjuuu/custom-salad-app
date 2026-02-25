# カスタムサラダをつくろう！

毎回同じメニューを選んでしまうあなたへ。
サラダの具材をガチャ感覚でランダムに提案してくれるWebアプリです。
新しい組み合わせとの出会いが、いつもの食事を少し楽しくしてくれるかもしれません。

## アプリを使ってみる

https://custom-salad-app-hbzysewpfftbqtmpwavfn8.streamlit.app/

## こんな人におすすめ

- いつも同じ具材ばかり選んでしまう
- 新しい食材の組み合わせを試してみたい
- サラダのマンネリを打破したい

## 特徴

- 具材をランダムに提案（Python の `random` を使用）
- ブラウザだけで動くのでインストール不要
- 何度でもガチャを回して新しい組み合わせを発見できる

## 使用技術

- Python
- Streamlit
- random（Python 標準ライブラリ）

## ローカルで動かす場合
```bash
pip install -r requirements.txt
streamlit run app.py
```

## ファイル構成

| ファイル | 内容 |
|---|---|
| `app.py` | アプリ本体 |
| `requirements.txt` | 必要なライブラリ一覧 |
