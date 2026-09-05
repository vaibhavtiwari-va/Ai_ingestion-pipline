from fuzzywuzzy import process
from litellm import completion
import pandas as pd
import os

# Free API Keys Setup (Environment Variables)
os.environ["GEMINI_API_KEY"] = "YOUR_GEMINI_KEY"
os.environ["GROQ_API_KEY"] = "YOUR_GROQ_KEY"

# 1. Multi-tier Fallback Engine
def extract_with_fallback(prompt_text):
    models = ["gemini/gemini-1.5-flash", "groq/llama3-8b-8192"]
    
    for model in models:
        try:
            response = completion(model=model, messages=[{"role": "user", "content": prompt_text}])
            return response.choices[0].message.content
        except Exception as e:
            print(f"⚠️ {model} Failed, switching to next model... Error: {e}")
    return "Fallback Failed"

# 2. Deterministic Entity Resolution
def resolve_entities():
    seed_canonical_list = ["OpenAI", "Anthropic", "Cohere", "Mistral AI", "Runway"]
    df = pd.read_csv("startups.csv")
    
    mapping_log = []
    resolved_names = []
    
    for raw_name in df['entityName']:
        best_match, score = process.extractOne(raw_name, seed_canonical_list)
        canonical = best_match if score > 80 else raw_name
        resolved_names.append(canonical)
        mapping_log.append({"Raw_Name": raw_name, "Canonical_Name": canonical, "Match_Score": score})
        
    df['entityName'] = resolved_names
    df.to_csv("startups_canonical.csv", index=False)
    pd.DataFrame(mapping_log).to_csv("entity_mapping_log.csv", index=False)
    print("✅ Step 2 Complete: Entity Resolution & LLM Fallback Chain Ready!")

if __name__ == "__main__":
    resolve_entities()