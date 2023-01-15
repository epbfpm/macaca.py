from requests import request
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = 'write me a song'

response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.6,
        )
print(response)



# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-002",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))
#
#     result = request.args.get("result")
#     return render_template("index.html", result=result)
#
#
# def generate_prompt(x):
#     return
#
# key = "Write something"
#
# generate_prompt(key)
