from flask import Flask, render_template, jsonify
import openai

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get/<string:user_input>')
def get_media(user_input):
    chat_response = openai.Chat(user_input)
    # split_response = chat_response.split('\n\n')

    # audio_list = []
    # image_list = []

    # for count, paragraph in enumerate(split_response):
    #     image_list.append(openai.Image(paragraph))

    #     openai.Audio(paragraph, f'audio{count}.mp3')
    #     audio_list.append(f'audio{count}.mp3')

    img_url = openai.Image(chat_response)
    openai.Audio(chat_response, '/static/audio/audio.mp3')
    
    response = {
        'audio_url': '/static/audio/audio.mp3',
        'image_url': img_url
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

