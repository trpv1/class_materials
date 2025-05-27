import streamlit as st

st.set_page_config(page_title="重要動詞＆群動詞マスター", layout="wide")

# --- Emojis for visual aid ---
dictionary_icon = "📖"
bulb_icon = "💡"
warning_icon = "⚠️"
pencil_icon = "✏️"
star_icon = "⭐"
graduation_cap_icon = "🎓"
runner_icon = "🏃" # For phrasal verbs - verb + particle running together

st.title(f"{dictionary_icon} 【中2・中3英語】重要動詞・群動詞マスター！")
st.caption("基本動詞と群動詞を使いこなして、表現力をアップさせよう！")

st.markdown("---")

# --- 1. 基本動詞のチカラを知ろう！ ---
st.header(f"{bulb_icon} 1. 基本動詞のチカラを知ろう！")
st.markdown("""
英語の基本動詞 (例: `take`, `get`, `make`, `have`, `look`) は、サッカーでいうパスやドリブルのようなもの。とっても基本的だけど、組み合わせ次第でたくさんの意味を表せるスーパーマンなんだ！
いくつかの使い方を見てみよう。
""")

st.subheader("🔹 `take` の使い方")
st.markdown("""
* `take a picture` (写真を撮る): Can you **take a picture** of us?
* `take a walk` (散歩する): Let's **take a walk** in the park.
* `take care of ~` (～の世話をする): I **take care of** my dog.
* `It takes (人) 時間 to do ~` (～するのに時間がかかる): **It took me** three hours **to finish** the homework.
    * この `It takes ... to ...` の形は超重要！
""")

st.subheader("🔹 `make` の使い方")
st.markdown("""
* `make breakfast/lunch/dinner` (朝食/昼食/夕食を作る): My father sometimes **makes breakfast**.
* `make a mistake` (間違いを犯す): Don't worry if you **make a mistake**.
* `make A B` (AをBの状態にする): This song **makes me happy**. (この歌は私を幸せにする。)
    * `make + 人/モノ + 形容詞/名詞` の形を覚えよう！
""")

st.subheader("🔹 `get` の使い方")
st.markdown("""
* `get to ~` (～に到着する): We **got to** the station at noon.
* `get on / get off` (乗り物に乗る/降りる): I **get on** the bus at 7:30. / Please **get off** at the next stop.
* `get up` (起きる): What time do you usually **get up**?
* `get + 形容詞` (～の状態になる): It's **getting dark**. (暗くなってきた。)
""")

st.subheader("🔹 `have` の使い方")
st.markdown("""
* `have breakfast/lunch/dinner` (食事をとる): I **had lunch** with my friends.
* `have a good time` (楽しい時を過ごす): We **had a good time** at the party.
* `have to + 動詞の原形` (～しなければならない): You **have to** study hard. (助動詞のような働き)
""")

st.subheader("🔹 `look` の使い方")
st.markdown("""
* `look at ~` (～を(意識して)見る): **Look at** this picture!
* `look + 形容詞` (～のように見える): You **look happy** today.
* `look for ~` (～を探す): I'm **looking for** my keys. (これは群動詞でもあるよ！)
""")

st.markdown("---")

# --- 2. 群動詞ってなかまだれ？ ---
st.header(f"{runner_icon} 2. 群動詞 (Phrasal Verbs) ってなかまだれ？")
st.markdown("""
**群動詞**とは、「動詞 + 副詞」や「動詞 + 前置詞」がセットになって、まるで新しい一つの単語のように特別な意味を持つようになったものだよ。
慣れるまでは少し大変だけど、使えるようになると表現がグッと豊かになる！セットで覚えよう！
""")

st.subheader("よく使う群動詞リスト")
phrasal_verbs_data = {
    "群動詞": [
        "`look for ~`",
        "`look after ~`",
        "`look forward to ~ing`",
        "`find out`",
        "`give up`",
        "`turn on` / `turn off`",
        "`put on`",
        "`call back`",
        "`get along with ~`"
    ],
    "主な意味": [
        "～を探す",
        "～の世話をする (≒ take care of ~)",
        "～するのを楽しみに待つ",
        "～を見つけ出す、知る",
        "あきらめる",
        "（電気製品など）をつける / 消す",
        "（衣服など）を身に着ける",
        "電話をかけ直す",
        "～と仲良くやる"
    ],
    "例文": [
        "I'm **looking for** my lost cat.",
        "She **looks after** her younger brother.",
        "I'm **looking forward to seeing** you.",
        "He **found out** the truth.",
        "Never **give up** your dream!",
        "Please **turn on** the TV. / Don't forget to **turn off** the lights.",
        "It's cold. You should **put on** your coat.",
        "I'll **call** you **back** later.",
        "Do you **get along with** your classmates?"
    ]
}
st.table(phrasal_verbs_data)
st.markdown("特に `look forward to ~ing` の `-ing` に注意！ `to` が前置詞だからだよ。(詳しくはヒントで！)")

st.markdown("---")

# --- 3. 【発展】無生物主語の文 ---
st.header(f"{bulb_icon} 3. 【発展】無生物主語の文に慣れよう！")
st.markdown("""
英語では、人だけでなく「モノ」や「コト」が主語になる文（無生物主語構文）がよく使われるよ。
日本語に直訳すると不自然なこともあるけど、英語ではとても自然な表現なんだ。

* 例1: **The news made us surprised.**
    * 直訳：その知らせは私たちを驚かせた。
    * 自然な日本語：その知らせを聞いて私たちは驚いた。
* 例2: **This road takes you to the library.**
    * 直訳：この道はあなたを図書館へ連れて行く。
    * 自然な日本語：この道を行けば図書館に着きます。
* 例3: **A short walk brought him to the park.**
    * 直訳：短い散歩が彼を公園へ連れてきた。
    * 自然な日本語：少し歩くと彼は公園に着いた。

無生物主語の文に慣れると、英語のニュースや読み物が理解しやすくなるよ！
""")

st.markdown("---")

# --- 4. 豆知識＆受験のヒント ---
st.header(f"{graduation_cap_icon} 4. 豆知識＆受験のヒント")

st.subheader(f"{star_icon} ヒント1：群動詞の目的語の位置（特に [動詞 + 副詞] タイプ）")
st.markdown("""
群動詞の中でも「動詞 + **副詞**」のタイプ (例: `turn on`, `put on`, `give up`) は、目的語の位置にルールがあるよ。
1.  目的語が**名詞** (例: the TV, your coat) の場合：
    * `turn on **the TV**` (動詞 + 副詞 + 目的語)  ⭕️
    * `turn **the TV** on` (動詞 + 目的語 + 副詞)  ⭕️
2.  目的語が**代名詞** (例: it, them, him, her) の場合：
    * `turn **it** on` (動詞 + 目的語代名詞 + 副詞) ⭕️ **これだけ！**
    * `turn on **it**` (動詞 + 副詞 + 目的語代名詞) ❌ ダメ！

「動詞 + **前置詞**」のタイプ (例: `look for ~`, `listen to ~`) は、目的語は必ず前置詞の後に来るよ。(例: `look for **him**`)
この区別はテストで狙われやすいから、しっかり覚えよう！
""")

st.subheader(f"{star_icon} ヒント2：「look forward to ~ing」の `to` は前置詞！")
st.markdown("""
`look forward to ~ing` (～するのを楽しみに待つ) の `to` は、不定詞の `to` (to + 動詞の原形) ではなく、**前置詞**なんだ。
前置詞の後ろには名詞か動名詞 (`~ing`) が来るルールだから、`look forward to see you` (❌) ではなく、`look forward to **seeing** you` (⭕️) となるよ。
これも超頻出ポイント！
""")

st.subheader(f"{star_icon} ヒント3：第5文型 (SVOC) を作る主な動詞")
st.markdown("""
「主語 + 動詞 + 目的語 + 補語」(S + V + O + C) の形で、「OをCの状態にする/呼ぶ/保つ」などの意味を表す文型だよ。
この形をとる代表的な動詞を覚えておこう。
* `make O C`: OをCの状態にする (例: The movie **made me sad**.)
* `call O C`: OをCと呼ぶ (例: We **call him Ken**.)
* `keep O C`: OをCの状態に保つ (例: Please **keep your room clean**.)
* `find O C`: OがCだとわかる、気づく (例: I **found the book interesting**.)
* `name O C`: OをCと名付ける (例: They **named their dog Pochi**.)
SVOCは長文読解や英作文で重要だよ。
""")

st.markdown("---")

# --- 5. 練習してみよう！ ---
st.header(f"{pencil_icon} 5. 練習してみよう！")
st.markdown("次の( )に適切な語句を選んだり、書き入れたりしてみよう。答えは「答えを見る」をクリック！")

practice_questions_verbs = [
    {
        "q_type": "choice",
        "question": "1. It (     ) me about an hour to get to school.",
        "options": ["takes", "makes", "has", "looks"],
        "answer_text": "takes\n解説: 「(人にとって)時間がかかる」は `It takes (人) 時間 to do ~` の形を使います。"
    },
    {
        "q_type": "choice",
        "question": "2. The coach's words (     ) the players confident.",
        "options": ["looked", "called", "made", "got"],
        "answer_text": "made\n解説: 「AをBの状態にする」は `make A B` (SVOC) の形です。「コーチの言葉は選手たちを自信がある状態にした」という意味。"
    },
    {
        "q_type": "choice",
        "question": "3. I am really looking forward to (     ) you this summer.",
        "options": ["see", "seeing", "saw", "be seen"],
        "answer_text": "seeing\n解説: `look forward to ~ing` で「～するのを楽しみに待つ」。この `to` は前置詞なので、後ろは動名詞(-ing形)です。"
    },
    {
        "q_type": "fill_in",
        "question": "4. Can you (     ) (     ) the music? It's too loud. (音楽の音量を下げてくれますか？)", # Clarified meaning
        "pre_answer": "turn down",
        "answer_text": "`turn down`\n解説: 「音量などを下げる」は `turn down` です。 `turn the music down` もOK。"
    },
    {
        "q_type": "fill_in_choice",
        "question": "5. My grandmother always (     ) care (     ) our cat when we are away.",
        "pre_answer": "takes / of",
        "answer_text": "`takes` / `of`\n解説: `take care of ~` で「～の世話をする」という意味の重要な群動詞です。"
    },
    {
        "q_type": "choice",
        "question": "6. He promised to call me back, but he never (     ).",
        "options": ["did", "does", "called", "made"],
        "answer_text": "did\n解説: 「彼は決して電話をかけ直さなかった」という意味。文脈から `call me back` の内容を `did` (しなかった) で受けています。 `He never called me back.` とも言えますが、選択肢からは `did` が適切。"
    },
    {
        "q_type": "fill_in",
        "question": "7. Please (     ) your shoes (     ) before entering the house. (靴を脱いでください)",
        "pre_answer": "take / off",
        "answer_text": "`take` / `off`\n解説: `take off ~` で「(衣服など)を脱ぐ」という意味です。`take your shoes off` の語順。"
    }
]

for i, item in enumerate(practice_questions_verbs):
    st.subheader(f"問題 {i+1}")
    if item["q_type"] == "choice":
        st.write(item["question"])
        answer = st.radio("選択肢:", item["options"], key=f"q{i}_verbs", label_visibility="collapsed")
        with st.expander("答えを見る"):
            # 修正箇所: 正解の選択肢と解説を分けて表示
            correct_answer_option = item["answer_text"].splitlines()[0]
            explanation = "\n".join(item["answer_text"].splitlines()[1:])
            st.markdown(f"**正解:** {correct_answer_option}")
            if explanation:
                st.markdown(explanation)
            
    elif item["q_type"] == "fill_in":
        user_input = st.text_input(item["question"], key=f"q{i}_verbs_fill") # ユーザー入力欄
        with st.expander("答えを見る"):
            st.markdown(f"**正解:** {item['pre_answer']}")
            st.markdown(item["answer_text"]) # こちらは pre_answer を含んだ解説でもOK
            
    elif item["q_type"] == "fill_in_choice": # 2つの穴埋めの場合
        question_parts = item["question"].split("(     )")
        if len(question_parts) < 3 : # Ensure there are at least two blanks
            question_parts.append("") # Add a placeholder if not
            question_parts.append("")

        cols = st.columns(2)
        with cols[0]:
            user_input1 = st.text_input(question_parts[0] + " (     ) " + question_parts[1], key=f"q{i}_verbs_fill1")
        with cols[1]:
             # Check if question_parts[2] exists
            second_blank_text = question_parts[2] if len(question_parts) > 2 else ""
            user_input2 = st.text_input(" (     ) " + second_blank_text, key=f"q{i}_verbs_fill2")


        with st.expander("答えを見る"):
            ans_parts = item["pre_answer"].split(" / ")
            st.markdown(f"**正解:** 1つ目の( ) `{ans_parts[0]}`  2つ目の( ) `{ans_parts[1]}`")
            st.markdown(item["answer_text"])


st.markdown("---")
st.success("たくさんの動詞や表現が出てきたね！一つ一つ例文と一緒に覚えて、使えるように練習しよう！ 💪")

