import streamlit as st
import requests
import json
import os

# StreamlitアプリケーションのUIを定義
def app():
    st.title('記事情報送信アプリ')

    # ユーザー入力欄を設定
    explanation_prompt = st.text_area("カスタムされた解説用のプロンプトを入力してください。", height=150)
    prompt = st.text_area("カスタムされた要約用のプロンプトを入力してください。", height=150)
    title = st.text_input("記事のタイトルを入力してください。")
    article_url = st.text_input("記事のURLを入力してください。")

    # 送信ボタン
    if st.button('送信'):
        # JSONデータを組み立て
        data = {
            "explanation_prompt": explanation_prompt,
            "prompt": prompt,
            "items": [
                {
                    "title": title,
                    "canonical": [
                        {
                            "href": article_url
                        }
                    ]
                }
            ]
        }
        
        # 特定のURLにPOSTリクエストを送信
        url = os.getenv('POSTURL')
        
        try:
            response = requests.post(url, json=data)
            
            # レスポンスのステータスコードと本文を表示
            if response.status_code == 200:
                st.success('成功: レスポンスコード {}'.format(response.status_code))
                st.json(response.json())
            else:
                st.error('エラー: レスポンスコード {}'.format(response.status_code))
        except Exception as e:
            st.error(f'送信中にエラーが発生しました: {e}')

# Streamlitアプリケーションを実行
if __name__ == '__main__':
    app()
