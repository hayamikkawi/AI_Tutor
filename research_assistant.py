# This file is aimed to understand the agent-loop, state, and memory 
# State is the source of truth for a task that is currrently happening
# It's structured such that it influences the agent loop and allows the system
# to keep a structured form of the ongoing task instead of messy logs.

import os 
from dotenv import load_dotenv
from openai import OpenAI
import json

state = {
    "task": "Find and summarize 5 research papers about RAG",
    "papers_found": [], 
    "papers_summarised": [], 
    "status": "not_started"
}

def add_paper(state, paper): 
    state['papers_found'].append(paper)

def summarize_paper(state, paper):
    state['summarized_paper'].append(paper)

concept_state = {
    "user_query": "Research Agentic AI concepts", 
    "concepts": [], 
    "target_number": 5, 
    "status": "in_progress"
}

# simulate search (in a real agent, it will use a search tool)
def search_concepts(query, already_found):

    all_concepts = [
        "Tool calling",
        "Agentic workflows",
        "State management",
        "Memory",
        "Planning"
    ]

    return [
        concept for concept in all_concepts
        if concept not in already_found
    ][:2]

# simulate an llm 
def llm_decide(state): 
    if len(state["concepts"]) < state["target_number"]:
        return "search"
    return "finish"

# update state
def collect_concepts(state):
    # as if it took the query and did a search
    results = search_concepts(state['user_query'], state['concepts'])
    state['concepts'].extend(results)
    return state

def run_agent(state): 
    while True: 
        action = llm_decide(state)
        if action == "search": 
            collect_concepts(state)
        elif action == "finish":
            state['status'] = 'completed'
            break
    return state


final_state = run_agent(concept_state)
print(final_state)