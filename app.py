import json
from fastapi import FastAPI

from src.models.prompt import export_question_feature


app = FastAPI()

@app.get("/")
def findProduct(question: str):
    features = export_question_feature(question)

    data = json.loads(open("data.json","r").read())
    points = {}
    for post in data:
        power = 0
        for item in features["usages"]:
            if (item in post["content"]["usages"]):
                power+=1

        points[post["post"]["random_key"]] = {
            "point": power,
            "post": post["post"]
        }

    return [x[1] for x in sorted(points.items(), key=lambda x: x[1]["point"], reverse=True)[:5]]

