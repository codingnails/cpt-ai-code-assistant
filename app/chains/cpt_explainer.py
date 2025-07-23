import os
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

load_dotenv()

class CPTExplainer:
    def __init__(self, model_name="gpt-4", temperature=0.3):
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)

        base_path = os.path.dirname(os.path.abspath(__file__))
        prompt_path = os.path.join(base_path, "..", "prompts")
        
        with open(os.path.join(prompt_path, "system_prompt.txt"), "r") as f:
            system_template = f.read()

        with open(os.path.join(prompt_path, "human_prompt.txt"), "r") as f:
            human_template = f.read()

        system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
        human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

        # Create chat prompt
        self.chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

        # Create chain
        self.chain = LLMChain(llm=self.llm, prompt=self.chat_prompt)

    def explain(self, cpt_code: str, short_description: str) -> str:
        return self.chain.run(cpt_code=cpt_code, short_description=short_description).strip()
