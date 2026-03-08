import streamlit as st
import random

st.title("カスタムサラダをつくろう！")

# サラダのベース
bases = [
    "ロメインレタス",
    "ほうれん草",
    "ケール",
    "ロメインレタスとほうれん草",
    "ロメインレタスとケール",
    "ほうれん草とケール",
    "ロメインレタスとワイルドライス",
    "ほうれん草とワイルドライス",
    "ケールとワイルドライス",
]

st.header("🥬 ベースを選ぶ")

if st.button("ベースを選ぶ"):
    st.session_state.selected_base = random.choice(bases)

if "selected_base" in st.session_state:
    st.write(f"**{st.session_state.selected_base}**")

# トッピング
toppings = [
    "自家製クルトン",
    "レッドオニオン",
    "グリルドコーン",
    "赤キャベツ",
    "アップル",
    "シラントロ（パクチー）",
    "キャロット",
    "レーズン",
    "ウォルナッツ",
    "サンフラワーシールド",
    "アーモンド",
    "追加ワイルドライス",
    "オリジナルチキン（35g）",
    "ローストポテト",
    "ボイルドエッグ",
    "ロースト豆腐",
    "ブラックビーンズ",
    "スパイシーブロッコリー",
    "トマト",
    "セロリ",
    "オレンジ",
]

st.header("🥗 トッピングを選ぶ")

if st.button("トッピングを選ぶ"):
    st.session_state.selected_toppings = random.sample(toppings, 4)

if "selected_toppings" in st.session_state:
    for topping in st.session_state.selected_toppings:
        st.write(f"**{topping}**")

# プレミアムメニュー
premium_items = [
    "春野菜ミックス",
    "ローストトマト",
    "アボカド（1/4）",
    "トマト×２",
    "チェダーチーズ",
    "オリジナルチキン",
    "サラダチキン",
    "グリルドサーモン",
    "アボカド（1/2）",
    "パルメザンチーズ",
    "ホワイトチーズ",
    "追加ロメインレタス",
    "追加ほうれん草",
    "追加ケール",
    "なし",
    "なし",
    "なし",
]

st.header("⭐ プレミアムメニューを選ぶ")

if st.button("プレミアムメニューを選ぶ"):
    st.session_state.selected_premium = random.choice(premium_items)

if "selected_premium" in st.session_state:
    st.write(f"**{st.session_state.selected_premium}**")

# ドレッシング
dressings = [
    "グリーンゴッデスドレッシング",
    "ジャパニーズソイビネグレット",
    "ワフー・ゴマドレッシング",
    "クリーミーシラチャードレッシング",
    "マイルドシラチャードレッシング",
    "バルサミックビネグレット",
    "メキシカンハニービネグレット",
    "シーザードレッシング",
    "バターミルククランチドレッシング",
    "キャロットチリビネグレット",
    "バジルオニオンドレッシング",
    "レモンスクイーズ",
    "ライムスクイーズ",
    "エキストラバージンオリーブオイル",
    "シラチャーソース",
    "ドレッシングなし",
]

st.header("🫒 ドレッシングを選ぶ")

if st.button("ドレッシングを選ぶ"):
    st.session_state.selected_dressing = random.choice(dressings)

if "selected_dressing" in st.session_state:
    st.write(f"**{st.session_state.selected_dressing}**")

# コンディメンツ
condiments = [
    "ソルト",
    "ブラックペッパー",
    "なし",
    "なし",
    "なし",
]

st.header("🧂 コンディメンツを選ぶ")

if st.button("コンディメンツを選ぶ"):
    st.session_state.selected_condiment = random.choice(condiments)

if "selected_condiment" in st.session_state:
    st.write(f"**{st.session_state.selected_condiment}**")

# 全て選択されたら完成メッセージを表示
if all(
    key in st.session_state
    for key in [
        "selected_base",
        "selected_toppings",
        "selected_premium",
        "selected_dressing",
        "selected_condiment",
    ]
):
    st.header("🎉 カスタムサラダ完成！")

# リセットボタン
st.divider()
if st.button("🔄 リセット"):
    for key in [
        "selected_base",
        "selected_toppings",
        "selected_premium",
        "selected_dressing",
        "selected_condiment",
    ]:
        if key in st.session_state:
            del st.session_state[key]
    st.rerun()
