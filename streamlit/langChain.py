# Way - 1:-------------------------------------------
import os
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = 'sk-proj-aBrd2SA2sFuF0k35oVkoT3BlbkFJds4Gl3fk3rKg4fQcya3i'

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



# Way - 2:-------------------------------------------
import os
from langchain_openai import OpenAI
os.environ['OPENAI_API_KEY'] = 'sk-proj-aBrd2SA2sFuF0k35oVkoT3BlbkFJds4Gl3fk3rKg4fQcya3i'

name = llm("What is the capital of Bangladesh?")   # ====== Error # ====== Error 
print(name)




import os
from langchain_openai import OpenAI
os.environ['OPENAI_API_KEY'] = 'sk-proj-aBrd2SA2sFuF0k35oVkoT3BlbkFJds4Gl3fk3rKg4fQcya3i'
openai = OpenAI()
prompt = "What is the capital of Bangladesh?"
response = openai.ask(prompt) # ====== Error # ====== Error = name 'ask' is not defined
name = response['answer']

