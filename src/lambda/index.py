import os
import json
import openai
from pytube import YouTube

# TODO: Implement testing
def handler(event, context):
    
    WHISPER_DOLLAR_PRICE_MINUTE = 0.006

    url = event['url']
    key = os.environ.get('OPENAI_KEY')
    
    videoId = url.split('v=')[1]
    filename = f"/tmp/{videoId}.mp3"
    
    yt = YouTube(url)

    yt.streams.filter(only_audio=True).first().download(filename=filename)
    
    price = yt.length/60 * WHISPER_DOLLAR_PRICE_MINUTE
    print("price: ${price}")
    
    openai.api_key = key
    audio_file= open(filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)['text']
    
    # TODO: Add paragraphs(needs calculation of token size)
    # promt = "Rewrite the following text formatted with paragraphs: " + text_answer[0:2000]
    # completion = openai.Completion.create(model="gpt-3.5-turbo-instruct", prompt=promt, max_tokens=2000)
    # print(completion.choices[0].text)
    # with open(f"{videoId}.txt", "w") as text_file:
    #    text_file.write(transcript)
        
    return {
        'statusCode': 200,
        'body': json.dumps(transcript)
    }
