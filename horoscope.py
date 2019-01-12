import random
from datetime import datetime as dt

times = ["утром", "днём", "вечером", "ночью", "после обеда", "перед сном"]
advices = ["ожидайте", "предостерегайтесь", "будьте открыты для"]
promises = ["гостей из забытого прошлого", "встреч со старыми знакомыми",
            "неожиданного праздника", "приятных перемен"]


def generate_prophecies(total_num=5, num_sentences=3):
    prophecies = []

    for i in range(total_num):
        forecast = ""
        for j in range(num_sentences):
            t = random.choice(times)
            a = random.choice(advices)
            p = random.choice(promises)

            full_sentence = f"{t.title()} {a} {p}."
            if j != num_sentences - 1:
                full_sentence = full_sentence + " "

            forecast = forecast + full_sentence

        prophecies.append(forecast)

    return prophecies

# def generate_page(head, body):
#     page = f"<html>{head}{body}</html>"
#     return page

# def generate_head(title):
#     head = f"""<head>
#     <meta charset='utf-8'>
#     <title>{title}</title>
#     </head>
#     """
#     return head

# def generate_body(header, paragraphs):
#     body = f"<h1>{header}</h1>"
#     for p in paragraphs:
#         body = body + f"<p>{p}</p>"
#     body = body + "<p>_______________________________________________________</p>"
#     body = body + "<p><a href=\"about.html\">О реализации</a>"
#     return f"<body>{body}</body>"

# def save_page(title, header, paragraphs, output="index.html"):
#     fp = open(output, "w", encoding="utf-8")
#     today = dt.now().date()
#     page = generate_page(
#         head=generate_head(title),
#         body=generate_body(header=header, paragraphs=paragraphs)
#     )
#     print(page, file=fp)
#     fp.close()


# #####################

# today = dt.now().date()

# save_page(
#     title="Гороскоп на сегодня",
#     header="Ваши предсказания на " + str(today),
#     paragraphs=generate_prophecies(3, 4),
# )

# #Создание about.html
# a_head = "<head><meta charset='utf-8'><title>О чем это все</title></head>"
# a_h1 = "<h1>О чем это все</h1>"
# a_body_p = "<img src=\"zod.jpg\" width=\"100\"/>"

# a_body_g = "<ol><li>Времена дня:<ul>"
# for i in range(len(times)):
#     a_body_g = a_body_g + "<li>" + times[i] + "</li>"

# a_body_g = a_body_g + "</ul></li><li>Глаголы:<ul>"

# for i in range(len(advices)):
#     a_body_g = a_body_g + "<li>" + advices[i] + "</li>"

# a_body_g = a_body_g + "</ul></li><li>События:<ul>"

# for i in range(len(promises)):
#     a_body_g = a_body_g + "<li>" + promises[i] + "</li>"

# a_body_g = a_body_g + "</ul></li></ol>"

# a_body_s = "<p><a href=\"index.html\">На главную</a>"

# pagea = f"<html>{a_head}{a_h1}{a_body_p}{a_body_g}{a_body_s}</html>"

# fa = open("about.html", "w", encoding="utf-8")
# print(pagea, file=fa)
# fa.close()