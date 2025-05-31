import streamlit as st
from datetime import datetime

def main():
    # ページ設定 (絵文字は https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/ などで確認できます)
    st.set_page_config(
        page_title="すみれ組 クラスだより",
        page_icon="🌸",
        layout="wide", # wide にすると横幅が広がります
    )

    # 今日の日付を取得
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day

    # --- ヘッダー ---
    st.markdown(
        f"""
        <div style="text-align: center;">
            <h1 style="color: #DB7093; font-family: 'Arial Rounded MT Bold', sans-serif;">
                🌷 すみれ組 クラスだより 🌷
            </h1>
            <p style="font-size: 1.2em; color: #4682B4;">{year}年 {month}月 {day}日</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider() # 区切り線

    # --- メインコンテンツ ---
    col1, col2 = st.columns([2, 1]) # レイアウトを2:1に分割

    with col1:
        st.markdown("## 📢 今月のお知らせ")
        st.info(
            """
            - **運動会の練習が始まります！** 🏃💨
              - 動きやすい服装で登園してください。
              - 水筒を忘れずに持ってきましょう。
            - **親子遠足について** 🚌💨
              - 詳細は別途お手紙でお知らせします。お楽しみに！
            - **絵本の読み聞かせ会** 📚✨
              - 素敵なゲストティーチャーがいらっしゃいます。
            """
        )

        st.markdown("## 🌟 今月の目標")
        st.success(
            """
            - **お友達と仲良く元気いっぱい遊ぼう！** 😊🤝
            - **使ったものは自分でお片付けしよう！** 🧸➡️📦
            - **大きな声でご挨拶しよう！** 「おはよう！」「さようなら！」☀️👋
            """
        )

        st.markdown("## 🎶 今月のうた")
        st.markdown(
            """
            <div style="background-color: #FFF0F5; padding: 15px; border-radius: 10px;">
                <h4 style="color: #FF69B4;">🎵 おもちゃのチャチャチャ 🎵</h4>
                <p>みんなで楽しく歌いましょう！歌詞カードは保育室にあります。</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("") # 少しスペースを空ける

        st.markdown("## ✨ 今月の製作")
        st.warning(
            """
            - **こいのぼり製作** 🎏
              - みんなで大きなこいのぼりを作ります！
              - 完成したらお部屋に飾るのでお楽しみに！
            """
        )

    with col2:
        # --- サイドバー的な情報 ---
        st.markdown(
            """
            <div style="background-color: #E6E6FA; padding: 20px; border-radius: 10px; text-align: center;">
                <h3 style="color: #4B0082;">🌸 すみれ組のみんなへ 🌸</h3>
                <p>毎日元気いっぱいのすみれ組さん！<br>
                先生たちは、みんなの笑顔が大好きです😊<br>
                今月も楽しい思い出をたくさん作ろうね！</p>
                <p><strong>担任：さくら先生 🌸<br>
                       たんぽぽ先生 🌼</strong></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown("") # 少しスペースを空ける

        # 画像を表示 (例：幼稚園のロゴやクラスのイメージ画像など)
        # ローカルの画像ファイルを使う場合は、同じディレクトリに画像を配置してください。
        # 例: st.image("sumire_gumi.png", caption="すみれ組のお部屋の様子", use_column_width=True)
        # 今回はダミーのURLを使用します。
        try:
            st.image(
                "https://images.unsplash.com/photo-1576671080801-34675a045159?q=80&w=1000&auto=format&fit=crop", # フリー素材サイトの画像URL例
                caption="みんなで仲良く遊ぼうね！",
                use_column_width=True,
            )
        except Exception:
            st.caption("画像は準備中です...")

        st.markdown("---")
        st.markdown("### 持ち物リスト ✅")
        st.markdown(
            """
            - [ ] ハンカチ・ティッシュ
            - [ ] 上履き
            - [ ] コップ
            - [ ] 連絡帳
            - [ ] （月曜日）体操服
            """
        )

    st.divider()

    # --- フッター ---
    st.markdown(
        """
        <div style="text-align: center; margin-top: 30px;">
            <p style="font-size: 0.9em; color: gray;">
                〇〇幼稚園 すみれ組<br>
                TEL: 03-XXXX-XXXX
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ちょっとしたお楽しみ（アニメーション）
    if st.button("🎉 お楽しみボタン"):
        st.balloons()
        st.toast("今日も一日頑張ろう！🥳", icon="☀️")

if __name__ == "__main__":
    main()
