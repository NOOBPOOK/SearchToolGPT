import guidance
from SearchPackage.Search import SerpAPIWrapper
from dotenv import dotenv_values

config = dotenv_values(".env")
SERPAPI_API_KEY = config.get("SERPAPI_API_KEY")

'''
This chat model is basically for searching things on the web rather than answering complex questions. Here 
first data is fed to a search engine Google, which transforms it to context and this context is passed on
to the LLM for more refined output 
'''


#Contains the code for a normal Guidance llm chat bot
def gpt(ques):
    #Building a LLM with GPT3.5
    guid = guidance.llms.OpenAI("gpt-3.5-turbo")
    #Chat Dialog reference
    result = guidance('''
    {{#system~}}
    You are a fast search assistance.
    {{~/system}}

    {{#user~}}
    Please try to answer this question
    {{query}}
    Use this text as a context
    {{search query}}
    {{~/user}}

    {{#assistant~}}
    {{gen 'answer' temperature=0.2 max_tokens=1000}}
    {{~/assistant}}

    {{#user~}}
    Now combine the all the answers generated.
    {{~/user}}

    {{#assistant~}}
    {{gen 'answer' temperature=0 max_tokens=1000}}
    {{~/assistant}}

    ''',
    llm = guid)

    #USER QUERY
    ok = result(query = ques, search = search)
    print(ok)

def search(st):
    search = SerpAPIWrapper(serpapi_api_key = SERPAPI_API_KEY,search_engine="google")
    try:
        ok = search.run(st)
        return "According to Google, " + ok
    except:
        return "No good results found"

question = input("Ask your Query to search Engine >>   ")
gpt(question)