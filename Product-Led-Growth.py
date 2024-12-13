from typing import List, Tuple

def top_k_unique_users(users: List[Tuple[str, int]], k: int) -> List[str]:
    # Create a dictionary to store the highest engagement score for each user
    score_to_user = {}
    
    # Iterate through the users and add them to the dictionary
    for user_id, score in users:
        if score not in score_to_user:
            score_to_user[score] = user_id
    
    # Extract the unique scores and sort them in descending order
    unique_scores = sorted(score_to_user.keys(), reverse=True)
    
    # Select the top k unique scores
    top_k_scores = unique_scores[:k]
    
    # Retrieve the corresponding user IDs for the top k scores
    result = [score_to_user[score] for score in top_k_scores]
    
    return result

# Example usage
users = [("user1", 100), ("user2", 200), ("user3", 200), ("user4", 300), ("user5", 400), ("user6", 100)]
k = 3
print(top_k_unique_users(users, k))  # Output: ['user5', 'user4', 'user2']
