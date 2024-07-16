# Way - 1:-------------------------------------------
import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = 'use here my api key'

openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(api_key=openai_api_key)

prompt_template = PromptTemplate(
    input_variables=["question"],
    template="Q: {question}\nA:"
)

chain = LLMChain(llm=llm, prompt=prompt_template)

question = "What is the capital of Bangladesh?"

name = chain.run(question)   # ====== Error # ====== Error  ======= Use invoke instead.

print(name)

