#!/usr/bin/env python
import sys
from WebScrapingAgentAutomationCrew.crew import WebScrapingAgentAutomationCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'url': 'https://eniad.ump.ma',
        'data_type': 'articles',
        'storage_params': './data/output.json',
        'frequency': 'daily'
    }
    WebScrapingAgentAutomationCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'url': 'https://eniad.ump.ma',
        'data_type': 'articles',
        'storage_params': './data/output.json',
        'frequency': 'daily'
    }
    try:
        WebScrapingAgentAutomationCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        WebScrapingAgentAutomationCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'url': 'https://eniad.ump.ma',
        'data_type': 'articles',
        'storage_params': './data/output.json',
        'frequency': 'daily'
    }
    try:
        WebScrapingAgentAutomationCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: main.py <command> [<args>]")
        sys.exit(1)

    command = sys.argv[1]
    if command == "run":
        run()
    elif command == "train":
        train()
    elif command == "replay":
        replay()
    elif command == "test":
        test()
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)