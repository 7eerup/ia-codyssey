from flask import Flask, request, render_template
import os
from io import BytesIO
from gtts import gTTS
import base64

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    error = None
    audio = None
    input_text = ''  # 초기화

    if request.method == 'POST':
        input_text = request.form.get('input_text')
        lang = request.form.get('lang', DEFAULT_LANG)

        if not input_text:
            error = "텍스트를 입력하세요."

            print(f"[ERROR] {error}")
        else:
            try:
                fp = BytesIO()
                tts = gTTS(text=input_text, lang=lang)
                tts.write_to_fp(fp)
                fp.seek(0)

                # mp3 데이터를 base64 인코딩하여 HTML에 embed
                audio = base64.b64encode(fp.read()).decode('utf-8')

            except Exception as e:
                error = f"TTS 변환 중 오류가 발생했습니다. {e}"

    return render_template('index.html', error=error, audio=audio)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
