import streamlit as st

st.set_page_config(page_title="間接話法マスター", layout="wide")

# --- Emojis for visual aid ---
speech_bubble = "💬"
light_bulb = "💡"
warning_sign = "⚠️"
pencil = "✏️"
books = "📚"
star = "⭐"
graduation_cap = "🎓"

st.title(f"{speech_bubble} 【中2英語】間接話法マスター！～誰が何を言ったかな？～")
st.caption("このページは、授業で使う「間接話法」のまとめです。しっかり理解して、テストや受験に役立てよう！")

st.markdown("---")

# --- 1. 間接話法って何？ ---
st.header(f"{light_bulb} 1. 間接話法って何？")
st.markdown("""
**直接話法 (Direct Speech)**: 人が言った「セリフ」をそのまま `“ ”` (クォーテーションマーク) を使って伝える方法。
* 例: He said, **"I am tired."** (彼は「私は疲れています」と言いました。)

**間接話法 (Indirect Speech / Reported Speech)**: 人が言った「セリフ」の内容を、他の人に伝える形で表現する方法。`“ ”` は使わない。
* 例: He said **that he was tired.** (彼は疲れていると言いました。)
* ポイント: `that` は「～ということ」という意味。ふつうの文（肯定文）を間接話法にするときによく使われるけど、省略できることも多いよ！
""")

st.markdown("---")

# --- 2. 基本の形を見てみよう！ ---
st.header(f"{books} 2. 基本の形を見てみよう！")
st.markdown("伝えたい「セリフ」の種類によって、間接話法の形が変わるよ。")

st.subheader("📝 表でチェック！基本パターン")
table_data = {
    "種類": [
        "**ふつうの文** (Statement)",
        "**Yes/No疑問文** (Yes/No Question)",
        "**疑問詞の疑問文** (Wh- Question)",
        "**命令文** (Imperative)"
    ],
    "直接話法 (例)": [
        'She said, **"I** study math."',
        'He said to me, **"Are** you busy?"',
        'She said to me, **"Where do** you live?"',
        'He said to me, **"Open** the door."\n\nShe said to me, **"Don\'t** run."'
    ],
    "間接話法 (例)": [
        'She said (that) **she** studied math.',
        'He asked me **if I was** busy.\n(He asked me **whether I was** busy.)',
        'She asked me **where I lived**.',
        'He told me **to open** the door.\n\nShe told me **not to** run.'
    ],
    "ポイント解説": [
        "`say` の後ろに `(that) + 主語 + 動詞`。動詞の形や代名詞が変わる！",
        "`ask 人 if [whether] 主語 + 動詞...`。\n`if` か `whether` を使う。「～かどうか」という意味。\n語順は「主語 + 動詞」になるのが超重要！",
        "`ask 人 疑問詞 + 主語 + 動詞...`。\n疑問詞はそのまま使う。\nこれも語順は「主語 + 動詞」！",
        "肯定の命令: `tell 人 to 動詞の原形`\n否定の命令: `tell 人 not to 動詞の原形`\n丁寧な依頼なら `ask 人 to ...` も使うよ。"
    ]
}
st.table(table_data)

st.markdown("---")

# --- 3. ココが変わる！注意ポイント ---
st.header(f"{warning_sign} 3. ココが変わる！注意ポイント")

st.subheader("① 時制の一致 (Sequence of Tenses)")
st.markdown("""
「彼が言った」「彼女は尋ねた」のように、伝える動詞 (said, told, asked) が過去形のとき、セリフの中の動詞も過去の形に合わせるのが基本ルール！ これを**時制の一致**というよ。

* `am / is` → **`was`**
* `are` → **`were`**
* 現在形の動詞 (例: `study`, `go`) → **過去形の動詞** (例: `studied`, `went`)
* `will` → **`would`**
* `can` → **`could`**
* `may` → **`might`**
* `have / has + 過去分詞` (現在完了) → **`had + 過去分詞`** (過去完了)

※でも、下で説明する「例外」もあるから注意！
""")

st.subheader("② 代名詞 (Pronouns)")
st.markdown("""
誰が話しているのか、誰に話しているのかによって、セリフの中の `I`, `my`, `me`, `you` などが変わるよ。文全体の意味を考えて、適切な代名詞を選ぼう！
* 例: He said to me, "**I** like **your** bike."
    * → He told me that **he** liked **my** bike.
""")

st.subheader("③ 時・場所を表す言葉 (Time and Place expressions)")
st.markdown("""
セリフが言われた時・場所と、それを伝えている時・場所が違う場合、これらの言葉も変わることが多いよ。
* `now` (今) → **`then`** (その時)
* `today` (今日) → **`that day`** (その日)
* `yesterday` (昨日) → **`the day before`** / **`the previous day`** (前の日)
* `tomorrow` (明日) → **`the next day`** / **`the following day`** (次の日)
* `this / these` (これ/これら) → **`that / those`** (それ/それら)
* `here` (ここに) → **`there`** (そこに)
* `... ago` (～前に) → **`... before`** (～前に)
""")
st.markdown("例: \"I will call you **tomorrow**,\" she said. → She said she would call me **the next day**.")

st.markdown("---")

# --- 豆知識＆受験のヒント ---
st.header(f"{graduation_cap} 4. 豆知識＆受験のヒント")

st.subheader(f"{star} 豆知識1：なぜ間接話法を使うの？")
st.markdown("""
お話やニュース記事、日常会話などで、誰かが言ったことを他の人に分かりやすく、そしてスムーズに伝えるために間接話法はとても便利だよ。長い会話や複数の人の発言をまとめるときにも役立つんだ。
""")

st.subheader(f"{star} 豆知識2：「that」はいつ省略できる？")
st.markdown("""
ふつうの文（肯定文）を間接話法にするときに使う接続詞の `that` は、特に会話などのくだけた場面ではよく省略されるよ。「She said (that) she was happy.」のように、`that` があってもなくても意味は通じるんだ。ただし、フォーマルな文章では `that` を入れることが多いよ。
""")

st.subheader(f"{graduation_cap} 受験のヒント1：時制の一致の「例外」に注意！")
st.markdown("""
時制の一致には大事な例外がある！これはテストでよく狙われるポイントだよ。
1.  **普遍の真理・変わらない事実**: 地球が丸い、１年は12ヶ月など、昔も今も変わらない事実。
    * He said, "The earth **is** round." → He said that the earth **is** round. (❌ `was` にしない)
2.  **現在の習慣的な行為**: 今も変わらず続けている習慣。
    * She said, "I **get up** at six every day." → She said that she **gets up** at six every day. (彼女が今もその習慣を続けているなら ❌ `got up` にしないことが多い)
3.  **歴史上の事実**: 過去に起こった歴史的な出来事。
    * Our teacher said, "World War II **ended** in 1945." → Our teacher said that World War II **ended** in 1945. (元々過去形なので、過去完了にはしない)
""")

st.subheader(f"{graduation_cap} 受験のヒント2：間接疑問文の語順は鉄則！")
st.markdown("""
間接話法で疑問文を伝えるとき（間接疑問文）の語順は、**`[ask 人] + 疑問詞 / if / whether + 主語 + 動詞 ...`** の形が絶対！
元の疑問文が `Are you ...?` や `Do you ...?` のような語順でも、間接疑問文では必ず「主語 + 動詞」の普通の文の語順に戻すこと。これは入試でも頻出だから、何度も練習して完璧にしよう！
* 間違いやすい例: He asked me where **did I live**. (❌)
* 正しい形: He asked me where **I lived**. (⭕️)
""")

st.subheader(f"{graduation_cap} 受験のヒント3：「say」と「tell」の使い分けをマスター！")
st.markdown("""
* **`tell`**: 後ろに必ず「誰に」伝えるかを表す目的語 (例: `me`, `him`, `Tom`) が来る。
    * `tell 人 (that) ...` (人に～だと言う)
    * 例: He **told me** (that) he was sleepy.
* **`say`**: 後ろに「誰に」を直接続けることは基本的にない。
    * `say (that) ...` (～だと言う)
    * 例: He **said** (that) he was sleepy.
    * もし `say` で「誰に」を言いたい場合は `say to 人 (that) ...` となるけど、間接話法では `tell 人` を使う方がずっと自然だよ。
""")

st.markdown("---")

# --- 練習してみよう！ ---
st.header(f"{pencil} 5. 練習してみよう！")
st.markdown("次の文を間接話法に書き換えてみよう。答えはすぐ下にあるよ！")

practice_questions = [
    ("Ken said, \"I play soccer.\"", "Ken said that **he played soccer**."),
    ("She said to me, \"Are you a student?\"", "She asked me **if I was a student**.\n(She asked me **whether I was a student**.)"),
    ("My mother said to me, \"Study hard.\"", "My mother told me **to study hard**."),
    ("He said, \"I will go to the park tomorrow.\"", "He said that **he would go to the park the next day**."),
    ("Yumi said to us, \"Where did you find this old coin?\"", "Yumi asked us **where we had found that old coin**.\n(または、文脈により Yumi asked us where we found that old coin. も可)")
]

for i, (q, a) in enumerate(practice_questions):
    st.subheader(f"問題 {i+1}")
    st.markdown(f"Q: {q}")
    with st.expander("答えを見る"):
        st.markdown(f"A: {a}")
    st.write("") # Add a little space

st.markdown("---")
st.success("これで間接話法の基本はバッチリ！何度も復習して、自分のものにしよう！ 💪")
st.balloons()
