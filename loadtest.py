import requests
import concurrent.futures
import time
import random

# Configuration
DOMJUDGE_URL = "http://139.59.11.198:12345/api/contests/1/submissions"
# API_TOKEN = "c0k98bgecer97a63v4tv1f31v7"  # Replace with your DOMjudge API token
USERNAME = "your_username"  # Replace with your DOMjudge username
PASSWORD = "your_password"  # Replace with your DOMjudge password
NUM_TEAMS = 50  # Number of teams
SUBMISSION_INTERVAL = 0.1  # Time in seconds between each submission request

# Headers for authorization and content type
# headers = {
#     "Authorization": f"Bearer {API_TOKEN}",
#     "Content-Type": "application/json"
# }


# Submission payload template (customize as needed)
def create_submission_payload(team_id):
    # Each team submits a unique solution file and language
    return {
        "team_id": team_id,
        "problem_id": random.choice(["id1", "id2", "id3"]),  # Random problem
        "language_id": random.choice(["python3"]),
        "filename": f"solution_{team_id}.py",
        "sourcecode": "print('Hello, world!')"  # Example source code
    }

# Function to simulate a single team submission
def submit_solution(team_id):
    payload = create_submission_payload(team_id)
    try:
        response = requests.post(DOMJUDGE_URL, json=payload, auth=(USERNAME, PASSWORD))
        if response.status_code == 201:
            print(f"Team {team_id} submission successful!")
        else:
            print(f"Team {team_id} submission failed with status code: {response.status_code}")
    except Exception as e:
        print(f"Team {team_id} encountered an error: {e}")

# Function to simulate all teams submitting in parallel
def load_test_submissions():
    with concurrent.futures.ThreadPoolExecutor(max_workers=NUM_TEAMS) as executor:
        futures = []
        for team_id in range(1, NUM_TEAMS + 1):
            # Schedule the submission for each team
            futures.append(executor.submit(submit_solution, team_id))
            time.sleep(SUBMISSION_INTERVAL)  # Short delay to avoid hitting the server too hard at once

        # Wait for all submissions to complete
        for future in concurrent.futures.as_completed(futures):
            future.result()  # Trigger any exceptions caught by threads

# Run the load test
if __name__ == "__main__":
    print("Starting load test...")
    start_time = time.time()
    load_test_submissions()
    end_time = time.time()
    print(f"Load test completed in {end_time - start_time:.2f} seconds.")
