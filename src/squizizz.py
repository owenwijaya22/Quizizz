import requests, json


def get_keys(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def get_input(keys):
    code = input('Code: ')
    key = keys[0]
    return code, key


def build_api_url(code, key):
    api_url = f'https://squiz.mrcyjanek.net/api5.php?code={code}&version=5&key={key}'
    return api_url

def get_response(api_url):
    response = requests.get(api_url)
    print(response.json())
    return response.json()


def parse(quizInfo):
    allAns = {}
    for question in quizInfo["answers"]:
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
                if question["structure"]["options"][int(
                        answerC)]["text"] == "":
                    answer.append(question["structure"]["options"][int(
                        answerC)]["media"][0]["url"])
                else:
                    answer.append(
                        question["structure"]["options"][int(answerC)]["text"])
        #image question
        if len(question["structure"]["query"]["media"]) > 0:
            questionStr = f'<br> <img src="{question["structure"]["query"]["media"][0]["url"]}"> <br>'
        #image question with text
        elif len(question["structure"]["query"]["media"]) > 0 and len(
                question["structure"]["query"]["text"]) > 0:
            questionStr = question["structure"]["query"]["media"][0][
                "url"] + question["structure"]["query"]["text"]
        else:
            questionStr = question["structure"]["query"]["text"]
        #adding green color to answer
        # if len(answer) > 1 and type(answer) == list:
        #     for x in answer
        #         x = f'<p style="color:MediumSeaGreen;">' + ''.join(x.split('<p>'))

        #     #multiple answers
        if '<p>' in answer or '</p>' in answer:
            answer = f'<p style="color:MediumSeaGreen;">' + ''.join(
                answer.split('<p>'))
        else:
            answer = f'<p style="color:MediumSeaGreen;">{answer}</p>'
        allAns[questionStr] = answer


def rewrite_keys(keys, filename):
    keys.pop(0)
    with open(filename, 'w') as file:
        json.dump(keys, file)


def main(filename=r'C:\Users\owenw\vscode\projects\Discord\data\keys.json'):
    keys = get_keys(filename)
    code, key = get_input(keys)
    api_url = build_api_url(code, key)
    quizInfo = get_response(api_url)
    rewrite_keys(keys, filename)
    parse(quizInfo)


main()
