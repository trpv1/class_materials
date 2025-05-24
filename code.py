import streamlit as st

st.set_page_config(page_title="間接話法マスター", layout="wide")

# --- Emojis for visual aid ---
speech_bubble = "💬"
light_bulb = "💡"
warning_sign = "⚠️"
pencil = "✏️"
books = "📚"

st.title(f"{speech_bubble} 【中2英語】間接話法マスター！～誰が何を言ったかな？～")
st.caption("このページは、授業で使う「間接話法」のまとめです。")

st.markdown("---")

# --- 1. 間接話法って何？ ---
st.header(f"{light_bulb} 1. 間接話法って何？")
st.markdown("""
**直接話法 (Direct Speech)**: 「セリフ」をそのまま伝える方法。
* 例: He said, **"I am tired."** (彼は「私は疲れています」と言いました。)

**間接話法 (Indirect Speech / Reported Speech)**: 「セリフ」を伝言のように、文に組み込んで伝える方法。
* 例: He said **that he was tired.** (彼は疲れていると言いました。)
* ポイント: `that` は省略できることもあります！
""")

st.markdown("---")

# --- 2. 基本の形を見てみよう！ ---
st.header(f"{books} 2. 基本の形を見てみよう！")
st.markdown("伝えたい「セリフ」の種類によって、形が変わります。")

st.subheader("表でチェック！")
table_data = {
    "種類": ["**ふつうの文** (Statement)", "**Yes/No疑問文** (Yes/No Question)", "**疑問詞の疑問文** (Wh- Question)", "**命令文** (Imperative)"],
    "直接話法 (例)": [
        'She said, **"I** study math."',
        'He said to me, **"Are** you busy?"',
        'She said to me, **"Where do** you live?"',
        'He said to me, **"Open** the door."\n\nShe said to me, **"Don\'t** run."'
    ],
    "間接話法 (例)": [
        'She said (that) **she** studied math.',
        'He asked me **if [whether] I was** busy.',
        'She asked me **where I lived**.',
        'He told me **to open** the door.\n\nShe told me **not to** run.'
    ],
    "ポイント": [
        "動詞の形が変わる！ (`study` → `studied`)\n代名詞も変わる！ (`I` → `she`)",
        "`ask 人 if SV...` か `ask 人 whether SV...`\n語順は「主語 + 動詞」になる！",
        "`ask 人 疑問詞 SV...`\n語順は「疑問詞 + 主語 + 動詞」！",
        "`tell 人 to 動詞の原形`\n否定は `tell 人 not to 動詞の原形`\n(丁寧な依頼なら `ask 人 to ...` も使う)"
    ]
}
st.table(table_data)

st.markdown("---")

# --- 3. ココが変わる！注意ポイント ---
st.header(f"{warning_sign} 3. ココが変わる！注意ポイント")

st.subheader("① 時制の一致 (Sequence of Tenses)")
st.markdown("""
主な動詞 (said, told, asked) が過去形なら、セリフの中の動詞も過去形に合わせるのが基本です！
* `am / is` → **`was`**
* `are` → **`were`**
* `do / does` → **`did`** (動詞が過去形になる)
* `will` → **`would`**
* `can` → **`could`**
* `have / has` (動詞) → **`had`**
* ※例外もありますが、まずはこの基本をしっかり覚えましょう！
""")

st.subheader("② 代名詞 (Pronouns)")
st.markdown("""
話し手や聞き手によって `I`, `my`, `me`, `you` などが変わります。誰から誰へのメッセージか考えよう！
* 例: He said, "**I** like **your** bag."
    * → He said that **he** liked **my** bag. (もし「私に」言った場合)
    * → He said that **he** liked **her** bag. (もし「彼女に」言った場合)
""")

st.subheader("③ 時・場所を表す言葉 (Time and Place expressions)")
st.markdown("""
セリフの中の時や場所を表す言葉も、伝える時点に合わせて変わることがあります。
* `now` → **`then`** (その時)
* `today` → **`that day`** (その日)
* `yesterday` → **`the day before`** / **`the previous day`** (前の日)
* `tomorrow` → **`the next day`** / **`the following day`** (次の日)
* `this / these` → **`that / those`**
* `here` → **`there`**
* `ago` → **`before`**
""")
st.markdown("例: \"I will go **tomorrow**,\" she said. → She said she would go **the next day**.")

st.markdown("---")

# --- 練習してみよう！ ---
st.header(f"{pencil} 練習してみよう！")
st.markdown("""
次の文を間接話法に書き換えてみましょう。
1.  Ken said, "I play soccer."
    * Ken said that \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
2.  She said to me, "Are you a student?"
    * She asked me \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
3.  My mother said to me, "Study hard."
    * My mother told me \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_.
""")

st.markdown("---")
st.info("この内容は授業の板書を元に作成されています。しっかり復習しましょう！ 💪")
