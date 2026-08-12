from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# Load API Key from .env
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)



def analyze_resume(resume_text,usergoal):
    promt =  f"""
    
You are a senior software engineer and hiring manager.

Evaluate the resume based on the user's goal.

User goal: "{usergoal}"

STRICT RULES:
-Extract only relevant skills for this goal.
-Remove irrelevant tools [excel for beckend,etc].
-Identify real gaps.
-Generate roadmap only for missing fields.

Return only JSON:
{{
"skills":[],
"missing_skills":[],
"roadmap":[],
"interview_question":[]
}}
Resume:
{resume_text}

"""   
    try:
        response = client.chat.completions.create(
            model="gpt-4-mini",
            temperature=0.3,
            messages=[
                {"role": "system", "content": "you are a strict hiring manager."},
                {"role": "user", "content": promt}
            ]
        )
        content = response.choices[0].message.content.strip()
        start=content.find("{")
        end=content.rfind("}")+1
        
        return json.loads(content[start:end])
        
    except Exception as e:
      return {
          "skills": [],
          "missing_skills": [],
          "roadmap": [],
          "interview_question": [],
      }
        