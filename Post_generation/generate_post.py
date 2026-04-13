import Post_generation.few_short as fs
import json
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


model=ChatMistralAI(model='mistral-small-2506')



def prompt():


    prompt=ChatPromptTemplate.from_messages([
        ("system"
        """     you are  AI expert in writing engaging post on LinkedIn ,like an profressional influncers,
                your task is to generate the  post base on :
                -topic,
                -language,
                -length(short/medium/short) as specified 

                if reference is not present generate the post by you own like an profressional influncer with bese on
                language,lenght and topic        
        """),
        ('user', """generate the post based on the following no Preamble:
                    topic:{topic}
                    length:{length}
                    language:{language}
         
                    Reference:{reference_text}
         
          """)])
         
    return prompt


def generate_post(length, language,topic):
    few_short =fs.FewShotPosts()
    posts = few_short.get_filtered_posts(length, language, topic)

    Prompt=prompt()
    
    reference_text="use the following examples as refernce for the writing style\n"
    if posts:
       
        for i,j in enumerate(posts):
          
            reference_text+=f"\n\nExample {i+1}: {j['text']}"
            if i==1:
               break
          
    else:
        reference_text = "None"
    

    chain=Prompt|model

    output = chain.invoke({
        "topic":topic,
        "length": length,
        "language": language,
        "reference_text": reference_text
    })

    return output.content




    


  