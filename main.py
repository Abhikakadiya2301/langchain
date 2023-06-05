from langchain.llms import OpenAI
from key import OPENAI_API_KEY
llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.9)

text = input("prompt:")
#text = "christmas creative tweet for food delivery company"
print(llm(text))
