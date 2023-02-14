# import requests
from flask import Flask, request, send_from_directory, render_template
import openai
import os

api_key = os.environ.get("api_key")
if api_key:
    openai.api_key = api_key
else:
    raise "No API key found in Environment Variable (api_key)"

app = Flask(
    __name__,
)


@app.route("/tryChat", methods=["GET", "POST"])
def tryChat():
    a = request.form.get("mydata")  # 获取ajax中mydata的内容，也就是输入的内容
    word = str(a)
    Chatword = chat(word)  # 返回应答
    return Chatword


def chat(text):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            # model="text-curie-001",
            prompt=text,
            temperature=0,
            max_tokens=2000,
        )
        return response["choices"][0]["text"]
    except openai.error.RateLimitError as err:
        return "openai.error.RateLimitError: " + str(err)


# def smallchatbot(msg):
#     url = f"http://api.qingyunke.com/api.php?key=free&appid=0&msg={msg}"  # 请求地址
#     html = requests.get(url)
#     content = html.json()["content"]
#     con = str(content)
#     c = con.replace("{br}", "\n")  # 对其返回的{br}进行转换转换为换行
#     return c


@app.route("/")
def search():
    # return send_from_directory("templates/", "ChatBot.html")
    return render_template("ChatBot.html")


if __name__ == "__main__":
    app.run()
