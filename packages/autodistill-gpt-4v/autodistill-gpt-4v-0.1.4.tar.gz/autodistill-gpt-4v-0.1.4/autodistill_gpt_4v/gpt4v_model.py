import base64
import os
from dataclasses import dataclass

import numpy as np
import supervision as sv
from autodistill.detection import CaptionOntology, DetectionBaseModel
from openai import OpenAI

HOME = os.path.expanduser("~")


@dataclass
class GPT4V(DetectionBaseModel):
    ontology: CaptionOntology

    def __init__(self, ontology: CaptionOntology, api_key, prompt: str = None):
        self.client = OpenAI(api_key=api_key)
        self.ontology = ontology
        self.prompt = prompt

    def predict(self, input, classes: list = None) -> sv.Classifications:
        if classes is None:
            classes = {k:k for k in self.ontology.prompts()}

        payload = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"What is in the image? Return the class of the object in the image. Here are the classes: {', '.join(classes)}. You can only return one class from that list." if self.prompt is None else self.prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,"
                            + base64.b64encode(open(input, "rb").read()).decode(
                                "utf-8"
                            ),
                        }
                    },
                ],
            }
        ]

        response = self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=payload,
            max_tokens=300,
        )

        class_ids = self.ontology.prompts().index(response.choices[0].message.content.lower().split(":")[-1].strip())

        return sv.Classifications(
            class_id=np.array([class_ids]),
            confidence=np.array([1]),
        )
