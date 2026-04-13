import json
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import ast
from dotenv import load_dotenv


load_dotenv()

model=ChatMistralAI(model='mistral-small-2506')


def preprocess(raw_file_path,processed_file_path):


    enriched_post=[]

    with open(raw_file_path,'r', encoding="utf-8") as file:

        post_content=json.load(file)
    

        for post in post_content:

            
            meta_data=get_meta_data(post['text'])
            enhaced_post=post|meta_data
            enriched_post.append(enhaced_post)

    unified_tags=enhance_tag(enriched_post)


    for i in enriched_post:
       current_tag=i['tag']
       new_tags= {unified_tags[j] for j in current_tag}
       post['tag']=list(new_tags) 


    # dump the content in the into the new json file

    with open(processed_file_path,'w') as file:
        json.dump(enriched_post,file)
   

def get_meta_data(post):
        
    
    prompt=ChatPromptTemplate.from_messages([
        ('system',"""From the given post, identify
         - tag for it and keep only two- three most relevant tags
         -line count
         -The language used english and hinglish (hindi+english)
         -Retrun   in json object format  containing the keys line count,language,tag
         -striclty follow the json format
         -don't add any extraw thing other that which is not metioned output"""),
    ('user',"""post:{input} """) ])

    chain=prompt|model
    output=chain.invoke({'input':post})
    output_tags=JsonOutputParser().parse(output.content)

    return output_tags


def enhance_tag(enrich_post):

    unique_tags=set()
    for post in enrich_post:
        unique_tags.update(post['tag']) 

    tags_list=','.join(unique_tags)


    prompt = ChatPromptTemplate.from_messages([
    ('system', """
    You are a tag normalization expert.

    Task:
    - Merge similar tags into one unified tag.

    Rules:
    - Convert to lowercase, fix spelling (e.g., "likedin" → "linkedin")
    - Merge synonyms & similar meaning tags
    - Use short, common names (Title Case)
    - Each tag must map to ONE unified tag
    - Keep categories minimal

    Examples:
    - job hunting, job hunt ,job search ,job → Job Search
    - motivation, inspiration → Motivation
    - stress, depression → Mental Health
    - linkedin, likedin → LinkedIn
    - scam, fraud → Scam
    - burnout, workplace → Work Culture

    Output:
    Return ONLY JSON mapping:
    {{"tag1": "Unified Tag", "tag2": "Unified Tag"}}
    """),

    ('user', """
     {tags_list}
    """)
    ])


    
    chain=prompt|model
    output=chain.invoke({'tags_list':tags_list})
    output_tags=JsonOutputParser().parse(output.content)

    return output_tags

   

preprocess("Data/raw_post_data.json","Data/processed_post_data.json")

