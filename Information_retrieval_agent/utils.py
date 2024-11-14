import os
import requests
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Function to get search results using SerpAPI
def get_search_results(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "engine": "google",
        "api_key": os.getenv("SERPAPI_KEY")
    }
    response = requests.get(url, params=params)

    if response.status_code != 200:
        return f"Error: {response.status_code}, {response.text}"

    data = response.json()
    snippets = [result['snippet'] for result in data.get('organic_results', [])]
    return snippets

# Function to extract information using an LLM
def extract_information_from_groq(companies, query_template):
    results = []
    groq_url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    # Process each company individually
    for company in companies:
        # Format the query for each company
        query = query_template.format(company=company)
        search_results = get_search_results(query)

        # Create a prompt that instructs Groq to extract specified fields
        prompt = (
            f"Based on the query '{query}', please extract relevant fields such as email and address, "
            f"from the following search results:\n\n"
        )
        prompt += "\n".join(search_results)

        # Request payload for Groq API, using 'messages' key as expected by the API
        payload = {
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            "model": "llama3-8b-8192"  # Adjust model if necessary
        }

        response = requests.post(groq_url, headers=headers, json=payload)
        
        if response.status_code == 200:
            extracted_info = response.json().get("choices", [])[0].get("message", {}).get("content", "")
        else:
            extracted_info = f"Error: {response.status_code}, {response.text}"

        # Append results for each company
        results.append({
            "Company": company,
            "Extracted Information": extracted_info
        })

    # Convert to DataFrame for structured output
    results_df = pd.DataFrame(results)
    return results_df
