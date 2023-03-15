# import requests
from flask import Flask, request, send_from_directory, render_template
import openai
import os

chat_model = os.environ.get("model")
api_key = os.environ.get("api_key")
if api_key:
    openai.api_key = api_key
else:
    raise "No API key found in Environment Variable (api_key)"

app = Flask(
    __name__,
)


@app.route("/chat", methods=["GET", "POST"])
def chat():
    a = request.form.get("mydata")  # Get user input
    word = str(a)
    reply = get_reply(word)  
    return reply

# For GPT 3+ models, use ChatCompletion API, openai.ChatCompletion.create
# For older models, use Completion API, openai.Completion.create
def get_reply(text):
    try:
        # response = openai.Completion.create(
        #     model=chat_model,
        #     # model="text-curie-001",
        #     prompt=text,
        #     temperature=0,
        #     max_tokens=4096,
        # )
        # return response["choices"][0]["text"]
        response = openai.ChatCompletion.create(
            model=chat_model,
            temperature=0,
            max_tokens=2048,
            messages=[
                {"role": "user", "content": text},
                ]
            )
        content = response['choices'][0]['message']['content']
        content = content.replace('\n', '<br />')
        return content
    except openai.error.RateLimitError as err:
        return "openai.error.RateLimitError: " + str(err)

@app.route("/")
def search():
    # return send_from_directory("templates/", "ChatBot.html")
    return render_template("ChatBot.html")


if __name__ == "__main__":
    app.run()
