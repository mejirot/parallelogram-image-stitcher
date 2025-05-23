# 平行四辺形画像結合ツール

画像を平行四辺形に切り抜き、それらを横に並べて1枚の横長画像を生成するPythonスクリプト。

## 概要

このツールは、指定されたフォルダ内の複数の画像を平行四辺形状に切り抜き、それらを横に並べて1枚の画像に結合します。主にスクリーンショットやゲーム画面のキャプチャなどを並べて表示したい場合に便利です。

## 機能

- 画像を平行四辺形状に切り抜きます（右側が傾いた形）
- 切り抜いた画像を指定した重なり具合で横に並べます
- 結果を1枚の横長画像として保存します

## 必要条件

- Python 3.6以上
- Pillowライブラリ

## インストール方法

```bash
pip install Pillow
```

## 使用方法

1. 画像を `img` フォルダに配置します
2. スクリプトを実行します:

```bash
python parallelo_combine.py
```

3. 作成された `parallelogram_combined.png` が出力されます

## カスタマイズ

スクリプト内の以下のパラメータを変更することで、結果をカスタマイズできます：

- `skew_factor` - 平行四辺形の傾斜の度合い（大きいほど傾きが強くなります）
- `overlap` - 画像同士の重なりの割合（0.0～1.0）

```python
# 例：傾斜を強くし、重なりを減らす場合
overlap = 0.3    # 重なりの割合 (0.0〜1.0)
skew_factor = 0.3  # 傾斜の強さ
```

## サンプル

このツールは以下のような画像を生成します：

- 複数のスクリーンショットが平行四辺形状に切り抜かれ、横に並んだ状態

## 作者

Created in 2025-05-10

## ライセンス

このプロジェクトはオープンソースとして自由に使用・改変可能です。