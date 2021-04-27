import requests
import json

def get_response():
    pin = input('Pin: ')
    url = f"https://abstract.land/api/quizizz/?pin={pin}"

    headers = {
        'authority': 'abstract.land',
        'accept': '*/*',
        'scheme': 'https',
        'Origin': 'https://quizizz.rocks',
        'Referer': 'https://quizizz.rocks/',
        'accept-encoding': 'gzip, deflate',
        "accept-language": "en-US,en;q=0.9,id;q=0.8",
        'DNT': '1',
    }

    r = requests.get(url, headers=headers)
    quizInfo = r.json()
    with open('./data/raw.json', 'w') as file:
        json.dump(quizInfo, file)
    return quizInfo
def parse(quizInfo):
    allAns = {}
    for question in quizInfo["questions"]:
        if question["type"] == "MCQ":
            #? Single answer
            if question["structure"]["options"][int(
                    question["structure"]["answer"])]["text"] == "":
                #? Image answer
                answer = question["structure"]["options"][int(
                    question["structure"]["answer"])]["media"][0]["url"]
            else:
                answer = question["structure"]["options"][int(
                    question["structure"]["answer"])]["text"]
        elif question["type"] == "MSQ":
            #? Multiple answers
            answer = []
            for answerC in question["structure"]["answer"]:
                if question["structure"]["options"][int(answerC)]["text"] == "":
                    answer.append(question["structure"]["options"][int(answerC)]
                                ["media"][0]["url"])
                else:
                    answer.append(
                        question["structure"]["options"][int(answerC)]["text"])
        #image question
        if len(question["structure"]["query"]["media"]) > 0:
            questionStr = f'<br> <img src="{question["structure"]["query"]["media"][0]["url"]}"> <br>'
        #image question with text
        elif len(question["structure"]["query"]["media"]) > 0 and len(question["structure"]["query"]["text"]) > 0:
            questionStr = question["structure"]["query"]["media"][0]["url"] + question["structure"]["query"]["text"]
        else:
            questionStr = question["structure"]["query"]["text"]
        #adding green color to answer
        # if len(answer) > 1 and type(answer) == list:
        #     for x in answer
        #         x = f'<p style="color:MediumSeaGreen;">' + ''.join(x.split('<p>'))
                
        #     #multiple answers
        if '<p>' in answer or '</p>' in answer:
            answer = f'<p style="color:MediumSeaGreen;">' + ''.join(answer.split('<p>'))
        else:
            answer = f'<p style="color:MediumSeaGreen;">{answer}</p>'
        allAns[questionStr] = answer

    with open("./data/answers.html", "w", encoding="utf-8") as f:
        for i in allAns.keys():
            f.write(f'QUESTION: {i} <br><br> ANSWER :{allAns[i]}<br><br>')
quizInfo = get_response()
parse(quizInfo)

import os
os.startfile(r"C:\Users\owenw\vscode\projects\Quizizz\data")
os.startfile(r"C:\Users\owenw\vscode\projects\Quizizz\data\answers.html")
