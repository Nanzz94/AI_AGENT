# Information Retrieval Agent
## Project Description
The Information Retrieval Agent is a Streamlit-based dashboard that enables users to extract information for specific entities (such as companies) from the web using search queries. It takes a list of entities from a CSV file and, for each one, formulates a custom query to retrieve specific information, such as email addresses, contact numbers, or other data points. The information is gathered using an API (such as Groq or SerpAPI), making it easy for users to automate information retrieval for a wide range of use cases.

## Setup Instructions
### Prerequisites
1.Python 3.8+: Make sure Python is installed on your system.

2.Install Dependencies: Use the **requirements.txt** file to install all necessary dependencies.

## Installation Steps
## 1.Clone the repository:

git clone https://github.com/yourusername/information-retrieval-agent.git

cd information-retrieval-agent

## 2.Install dependencies:


**pip install -r requirements.txt**

## 3.Set up environment variables:

Create a .env file in the project root directory to store your API keys. (See API Keys and Environment Variables section below.)

## 4.Run the application:


streamlit run main.py

# Usage Guide

1.Upload CSV File: Upload a CSV file containing the list of entities you want to retrieve information for. The file should have a column with the entities' names (e.g., company names).

2.Select Main Column: Choose the column in the CSV file that contains the entity names.

3.Define Custom Query: Enter a query template, such as Get me the email address of {company}. The {company} placeholder will be replaced by each entity in the selected column.

4.Run Information Retrieval: Click the "Run Information Retrieval" button. The app will generate search queries for each entity and retrieve relevant information based on the specified query template.

5.Download Results: Once the information is retrieved, you can download the results as a CSV file by clicking the "Download Results as CSV" button.

# API Keys and Environment Variables
This project requires access to external APIs for search results, which may include:

->  Groq API or SerpAPI: For retrieving search results from the web.

### To set up API keys:

1.Create a .env file in the root directory of the project.

2.Add your API key(s) to the .env file in the following format:


**GROQ_API_KEY=your_groq_api_key_here**

**SERPAPI_API_KEY=your_serpapi_key_here**

3.Ensure the code reads these environment variables when making requests.

# Advanced Features
->Advanced Query Templates: Allow users to extract multiple fields in a single prompt, such as “Get the email and address for {company}.

->Customizable Query Template: The query template supports dynamic customization for retrieving different types of information (e.g., email addresses, contact numbers).

->Downloadable Results: Easily download the retrieved information in a CSV file format.

->Flexible API Configuration: Supports different APIs like Groq or SerpAPI, allowing users to choose based on their needs.

# Note
I have provided a sample csv file to upload


