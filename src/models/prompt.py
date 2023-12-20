

import json
import re
import google.generativeai as genai
key = "AIzaSyCDrgkHCRUeM1OmW21z-nh1uH-Ql5N8ctM"


genai.configure(api_key=key)

generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

model = genai.GenerativeModel(model_name="gemini-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def get_response(name:str):
  prompt_parts = [
      "As a mobile phone specialist:\n"+f"{name}"+"\n\nIn what category is it placed and for what applications is it suitable?\n\nJust answer me as follows json data:\n{ \n\"category\":[\"category1\", \"category2\", ...],\n\"usages\": [\"usage1\", \"usage2\", ...]\n}\n\nThere is no need to provide additional explanations.\n",
  ]

  response = model.generate_content(prompt_parts)

  match = re.search(r"\{(?:[^{}]|(?:[^{}])*)\}", response.text)

  if match:
      json_data = match.group()
      parsed_json = json.loads(json_data)
      return parsed_json
  else:
      print("No JSON data found in the input text.")
  return None

def export_question_feature(question: str):
  prompt_parts = [
      "As a mobile phone specialist:\n"+f"{question}"+"\n\nIn what category is it placed and for what applications is it suitable?\n\nJust answer me as follows json data:\n{ \n\"category\":[\"category1\", \"category2\", ...],\n\"usages\": [\"usage1\", \"usage2\", ...]\n}\n\nThere is no need to provide additional explanations.\n\n\nLables of usages:\nStreaming videos\nGaming\nGeneral\nMultimedia\nPhotography\nBusiness\nVideo Streaming\nSocial Media\nWork\nEveryday use\nMessaging\nBrowsing\nEntertainment\nCommunication\nProductivity\nWeb Browsing\nBasic Photography\nLight Gaming\nLightweight Apps\nVideography\nCalling\nMessaging\nBrowsing\nContent creation\n\n",
  ]

  response = model.generate_content(prompt_parts)

  match = re.search(r"\{(?:[^{}]|(?:[^{}])*)\}", response.text)

  if match:
      json_data = match.group()
      parsed_json = json.loads(json_data)
      return parsed_json
  else:
      print("No JSON data found in the input text.")
  return None


# get_response(name="Realme 11 Pro Plus 5G 512/12 GB")