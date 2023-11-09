import os
from base64 import b64decode

import openai
from openai import OpenAI as API

from autonomous import log


class OpenAI:
    def __init__(self):
        self.client = API(api_key=os.environ.get("OPENAI_KEY"),)

    def generate_image(
        self,
        prompt,
        **kwargs
    ):
        images = []

        try:
            response = self.client.images.generate(
                 model="dall-e-3", prompt=prompt, response_format="b64_json", **kwargs
            )
        except Exception as e:
            log(f"{e}\n\n==== Error: fall back to lesser model ====")
            images = ["https://picsum.photos/400/?blur"]
        else:
            for index, image_dict in enumerate(response.data):
                image_data = b64decode(image_dict.b64_json)
                images.append(image_data)
        return images

    def generate_json(self, text, primer_text="", functions=None):
        json_data = {
            #"response_format":{ "type": "json_object" },
            "messages":[
                {
                    "role": "system",
                    "content": f"{primer_text}. Your output must be a JSON object.",
                },
                {
                    "role": "user",
                    "content": text,
                },
            ]
        }

        if isinstance(functions, (list, tuple)):
            json_data.update({"functions": functions})
        elif functions is not None:
            json_data.update({"function_call": {"name": functions["name"]}})
            json_data.update({"functions": [functions]})

        
        #try:
        response = self.client.chat.completions.create(model="gpt-4", **json_data)
        # except Exception as e:
        #     log(f"{type(e)}:{e}\n\n==== Error: fall back to lesser model ====")
        #     response = self.client.chat.completions.create(
        #         model="gpt-3.5-turbo", **json_data
        #     )
        # breakpoint()
        try:
            result = response.choices[0].message.function_call.arguments
        except Exception as e:
            log(f"{type(e)}:{e}\n\n Unable to generate content ====")
            return e

        return result

    def generate_text(self, text, primer_text=""):
        json_data= {"messages" :
            [
                {
                    "role": "system",
                    "content": primer_text,
                },
                {
                    "role": "user",
                    "content": text,
                },
            ]
        }
        
        try:
            response = self.client.chat.completions.create(model="gpt-4", **json_data)
        except Exception as e:
            log(f"{type(e)}:{e}\n\n==== Error: fall back to lesser model ====")
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo", **json_data
            )
        # breakpoint()
        try:
            result = response.choices[0].message.content
        except Exception as e:
            log(f"{type(e)}:{e}\n\n Unable to generate content ====")
            return e

        return result

    def summarize_text(self, text, primer=""):
        message = [
            {
                "role": "system",
                "content": f"You are a highly skilled AI trained in language comprehension and summarization.{primer}",
            },
            {"role": "user", "content": text},
        ]
        try:
            response = self.client.chat.completions.create(
                model="gpt-4", temperature=0, messages=message
            )
        except Exception as e:
            log(f"{type(e)}:{e}\n\n==== Error: fall back to lesser model ====")
            response = self.client.chat.completions.create(
                model="gpt-4", temperature=1, messages=message
            )
        # breakpoint()

        try:
            result = response.choices[0].message.content
        except Exception as e:
            log(f"{type(e)}:{e}\n\n Unable to generate content ====")
            return e

        return result
