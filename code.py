import streamlit as st
import random

# 単位換算の基本情報
UNIT_INFO = {
    "長さ (m)": {
        "基本単位": "m (メートル)",
        "例": [
            "1 km = 1000 m",
            "1 m = 100 cm",
            "1 cm = 10 mm"
        ],
        "問題": [
            {"q": "2 km = □ m", "a": 2000, "unit": "m"},
            {"q": "300 cm = □ m", "a": 3, "unit": "m"},
            {"q": "5 m = □ cm", "a": 500, "unit": "cm"},
            {"q": "1.5 km = □ m", "a": 1500, "unit": "m"},
            {"q": "2500 m = □ km", "a": 2.5, "unit": "km"},
            {"q": "50 mm = □ cm", "a": 5, "unit": "cm"},
            {"q": "12 cm = □ mm", "a": 120, "unit": "mm"},
            {"q": "0.5 m = □ cm", "a": 50, "unit": "cm"},
        ]
    },
    "重さ (g)": {
        "基本単位": "g (グラム)",
        "例": [
            "1 kg = 1000 g",
            "1 t = 1000 kg"
        ],
        "問題": [
            {"q": "3 kg = □ g", "a": 3000, "unit": "g"},
            {"q": "5000 g = □ kg", "a": 5, "unit": "kg"},
            {"q": "0.5 kg = □ g", "a": 500, "unit": "g"},
            {"q": "2 t = □ kg", "a": 2000, "unit": "kg"},
            {"q": "1500 kg = □ t", "a": 1.5, "unit": "t"},
            {"q": "2.5 kg = □ g", "a": 2500, "unit": "g"},
            {"q": "700 g = □ kg", "a": 0.7, "unit": "kg"},
            {"q": "0.2 t = □ kg", "a": 200, "unit": "kg"},
        ]
    },
    "かさ (L)": {
        "基本単位": "L (リットル)",
        "例": [
            "1 L = 1000 mL",
            "1 L = 10 dL",
            "1 dL = 100 mL"
        ],
        "問題": [
            {"q": "4 L = □ mL", "a": 4000, "unit": "mL"},
            {"q": "2000 mL = □ L", "a": 2, "unit": "L"},
            {"q": "0.7 L = □ mL", "a": 700, "unit": "mL"},
            {"q": "3 L = □ dL", "a": 30, "unit": "dL"},
            {"q": "50 dL = □ L", "a": 5, "unit": "L"},
            {"q": "1.5 L = □ mL", "a": 1500, "unit": "mL"},
            {"q": "250 mL = □ dL", "a": 2.5, "unit": "dL"},
            {"q": "0.3 dL = □ mL", "a": 30, "unit": "mL"},
        ]
    },
    "面積 (m²)": {
        "基本単位": "m² (平方メートル)",
        "例": [
            "1 km² = 1000000 m²",
            "1 m² = 10000 cm²",
            "1 a = 100 m²",
            "1 ha = 10000 m²"
        ],
        "問題": [
            {"q": "2 m² = □ cm²", "a": 20000, "unit": "cm²"},
            {"q": "30000 cm² = □ m²", "a": 3, "unit": "m²"},
            {"q": "1 a = □ m²", "a": 100, "unit": "m²"},
            {"q": "5 ha = □ m²", "a": 50000, "unit": "m²"},
            {"q": "0.5 km² = □ m²", "a": 500000, "unit": "m²"},
            {"q": "200 m² = □ a", "a": 2, "unit": "a"},
            {"q": "30000 m² = □ ha", "a": 3, "unit": "ha"},
        ]
    },
    "体積 (m³)": {
        "基本単位": "m³ (立方メートル)",
        "例": [
            "1 m³ = 1000000 cm³",
            "1 L = 1000 cm³",
            "1 mL = 1 cm³"
        ],
        "問題": [
            {"q": "2 m³ = □ cm³", "a": 2000000, "unit": "cm³"},
            {"q": "5000000 cm³ = □ m³", "a": 5, "unit": "m³"},
            {"q": "3 L = □ cm³", "a": 3000, "unit": "cm³"},
            {"q": "4000 cm³ = □ L", "a": 4, "unit": "L"},
            {"q": "0.5 m³ = □ L", "a": 500, "unit": "L"}, # 1 m³ = 1000 L
            {"q": "250 mL = □ cm³", "a": 250, "unit": "cm³"},
        ]
    },
    "時間": {
        "基本単位": "秒 (びょう)",
        "例": [
            "1 分 = 60 秒",
            "1 時間 = 60 分",
            "1 時間 = 3600 秒"
        ],
        "問題": [
            {"q": "3 分 = □ 秒", "a": 180, "unit": "秒"},
            {"q": "120 秒 = □ 分", "a": 2, "unit": "分"},
            {"q": "2 時間 = □ 分", "a": 120, "unit": "分"},
            {"q": "90 分 = □ 時間 □ 分", "a": "1 時間 30 分", "unit": ""}, # 答えの形式を調整
            {"q": "1 時間 = □ 秒", "a": 3600, "unit": "秒"},
            {"q": "7200 秒 = □ 時間", "a": 2, "unit": "時間"},
            {"q": "1.5 時間 = □ 分", "a": 90, "unit": "分"},
            {"q": "45 分 = □ 時間", "a": 0.75, "unit": "時間"}, # 小学生向けには難しいかも？分数で答える形式も検討
        ]
    },
    "速さ (時速)": {
        "基本単位": "時速 km/時",
        "例": [
            "時速 60 km は、1分間に 1 km 進む速さ",
            "秒速 10 m は、1分間に 600 m (0.6 km) 進む速さ"
        ],
        "問題": [
            # 時速と分速
            {"q": "時速 36 km = 分速 □ m", "a": 600, "unit": "m"}, # (36 * 1000) / 60
            {"q": "分速 500 m = 時速 □ km", "a": 30, "unit": "km"}, # (500 * 60) / 1000
            # 時速と秒速
            {"q": "時速 72 km = 秒速 □ m", "a": 20, "unit": "m"}, # (72 * 1000) / 3600
            {"q": "秒速 15 m = 時速 □ km", "a": 54, "unit": "km"}, # (15 * 3600) / 1000
            # 道のり = 速さ × 時間
            {"q": "時速 40 km で 2 時間進むと □ km", "a": 80, "unit": "km"},
            {"q": "分速 60 m で 10 分進むと □ m", "a": 600, "unit": "m"},
            # 時間 = 道のり ÷ 速さ
            {"q": "100 km の道のりを 時速 50 km で進むと □ 時間", "a": 2, "unit": "時間"},
            {"q": "1200 m の道のりを 分速 200 m で進むと □ 分", "a": 6, "unit": "分"},
            # 速さ = 道のり ÷ 時間
            {"q": "3 時間で 150 km 進むときの速さは 時速 □ km", "a": 50, "unit": "km"},
            {"q": "5 分で 1000 m 進むときの速さは 分速 □ m", "a": 200, "unit": "m"},
        ]
    }
}

# Streamlitアプリの開始
st.title("小学生のための単位換算ノート ✏️")

st.header("はじめに")
st.write("""
私たちの身の回りには、ものの長さや重さ、かさなどを表す「単位」がたくさんあります。
例えば、えんぴつの長さを「cm (センチメートル)」で表したり、牛乳の量を「L (リットル)」で表したりしますね。
大きな単位と小さな単位を自由に変えられるようになると、計算がしやすくなったり、ものの大きさを比べやすくなったりします。
このノートで、いろいろな単位の換算をマスターしましょう！
""")

st.header("例題を見てみよう 💡")
for unit_name, info in UNIT_INFO.items():
    st.subheader(f"単位の種類: {unit_name}")
    if info["例"]:
        for ex in info["例"]:
            st.markdown(f"- {ex}")
    else:
        st.write("この単位の例題は準備中です。")
    st.write("---")


# 練習問題セクションの作成
st.header("れんしゅうもんだいを やってみよう！ ✍️")

# セッションステートの初期化
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'show_results' not in st.session_state:
    st.session_state.show_results = {} # 各カテゴリごとの結果表示状態

# 各単位カテゴリごとに問題と解答入力欄を作成
for category_id, (unit_name, info) in enumerate(UNIT_INFO.items()):
    st.subheader(f"{unit_name} の問題")

    # カテゴリごとの結果表示状態を初期化
    if category_id not in st.session_state.show_results:
        st.session_state.show_results[category_id] = False

    # 問題をランダムにシャッフル（任意）
    # random.shuffle(info["問題"]) # 同じ問題順でやりたい場合はコメントアウト

    category_answers = {}
    for i, q_data in enumerate(info["問題"]):
        question_key = f"{category_id}_{i}" # 各質問にユニークなキーを割り当てる
        user_answer = st.text_input(
            f"問 {i+1}: {q_data['q']}",
            key=question_key,
            value=st.session_state.answers.get(question_key, "") # 前回の入力を保持
        )
        category_answers[question_key] = {"user_input": user_answer, "data": q_data}

    st.session_state.answers.update(category_answers) # 入力された答えをセッションステートに保存

    # "こたえあわせをする" ボタン
    if st.button(f"{unit_name} のこたえあわせをする", key=f"check_button_{category_id}"):
        st.session_state.show_results[category_id] = True

    # 結果表示
    if st.session_state.show_results[category_id]:
        st.subheader(f"{unit_name} の こたえ と かいせつ")
        correct_count = 0
        total_questions = len(info["問題"])

        for i, q_data in enumerate(info["問題"]):
            question_key = f"{category_id}_{i}"
            user_input = st.session_state.answers.get(question_key, {}).get("user_input", "")
            correct_answer = str(q_data["a"])
            unit = q_data["unit"]

            is_correct = False
            # 時間の問題で "X 時間 Y 分" の形式の場合の正誤判定を簡易的に行う
            if "時間" in q_data["q"] and "分" in q_data["q"] and isinstance(q_data["a"], str):
                # ユーザー入力と正解を比較（より厳密な比較が必要な場合は正規表現など）
                if user_input.replace(" ", "") == correct_answer.replace(" ", ""):
                    is_correct = True
            else:
                try:
                    if user_input and float(user_input) == float(correct_answer):
                        is_correct = True
                except ValueError:
                    pass # 数字に変換できない入力は不正解とする

            if is_correct:
                correct_count += 1
                st.markdown(f"問 {i+1}: {q_data['q']} <font color='green'>せいかい！</font> こたえ: {correct_answer} {unit}", unsafe_allow_html=True)
            else:
                st.markdown(f"問 {i+1}: {q_data['q']} <font color='red'>まちがい</font> こたえ: {correct_answer} {unit}", unsafe_allow_html=True)
                # 簡単な解説（例を参考に）
                if unit_name == "長さ (m)":
                    if "km" in q_data["q"] and "m" in q_data["q"].split("=")[1]: # km -> m
                        st.caption(f"ヒント: 1 km は 1000 m だから、{q_data['q'].split('=')[0].split(' ')[0]} × 1000 を計算します。")
                    elif "cm" in q_data["q"] and "m" in q_data["q"].split("=")[1]: # cm -> m
                        st.caption(f"ヒント: 100 cm は 1 m だから、{q_data['q'].split('=')[0].split(' ')[0]} ÷ 100 を計算します。")
                elif unit_name == "重さ (g)":
                    if "kg" in q_data["q"] and "g" in q_data["q"].split("=")[1]: # kg -> g
                        st.caption(f"ヒント: 1 kg は 1000 g だから、{q_data['q'].split('=')[0].split(' ')[0]} × 1000 を計算します。")
                # 他の単位の解説も同様に追加できます

        st.write(f"**{unit_name} のせいせき: {total_questions} 問中 {correct_count} 問せいかい！**")
        if st.button(f"{unit_name} のもんだいをもういちどとく", key=f"retry_button_{category_id}"):
            st.session_state.show_results[category_id] = False
            # 解答をクリア（任意）
            for i in range(len(info["問題"])):
                question_key = f"{category_id}_{i}"
                if question_key in st.session_state.answers:
                    st.session_state.answers[question_key] = ""
            st.rerun() # ページを再読み込みして問題を再表示

        st.write("---")

st.sidebar.header("単位換算ノートについて")
st.sidebar.info(
    "このアプリは、小学生が単位換算を楽しく学べるように作られました。\n\n"
    "たくさんの問題を解いて、単位博士を目指そう！"
)

