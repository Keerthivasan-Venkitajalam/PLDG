# PLDG

### **Problem: Optimize Feature Rollout in a Product-Led Growth Platform**

#### **Problem Statement:**

You are tasked with rolling out a new feature in a Product-Led Growth (PLG) platform. The goal is to enable the feature for a limited number of users to monitor performance and engagement before a full launch. You are given a list of users and their engagement scores. Your task is to select the **top `k` users with the highest engagement scores** and ensure the rollout is fair by selecting users with **unique engagement scores**.

Write a function that takes a list of users with their engagement scores and an integer `k`, and returns the top `k` users with the highest **unique engagement scores**. If there are not enough unique scores to select `k` users, return as many as possible.

#### **Input Format:**
- A list of tuples `users` where each tuple contains a string (user ID) and an integer (engagement score): `[(user_id, score), ...]`
- An integer `k` representing the number of users to select.

#### **Output Format:**
- A list of user IDs representing the selected users with the highest unique engagement scores, sorted in descending order of scores.

#### **Constraints:**
- \(1 \leq \text{len(users)} \leq 10^5\)
- \(0 \leq \text{engagement score} \leq 10^9\)
- \(1 \leq k \leq 10^5\)

#### **Example:**

```plaintext
Input:
users = [("user1", 100), ("user2", 200), ("user3", 200), ("user4", 300), ("user5", 400), ("user6", 100)]
k = 3

Output:
['user5', 'user4', 'user2']
```

#### **Explanation:**
- The unique engagement scores are `[400, 300, 200, 100]`.
- The top 3 unique scores are `[400, 300, 200]`.
- The users with these scores are `["user5", "user4", "user2"]`.

---


### **Step-by-Step Explanation**

1. **Initialize a dictionary** `score_to_user` to store the highest engagement score and associate it with a unique user ID. This ensures that only unique scores are considered.
   
2. **Iterate through the `users` list** and populate the dictionary. If a score is not already present in the dictionary, add it with the corresponding user ID.

3. **Extract and sort the unique scores** in descending order.

4. **Select the top `k` scores** from the sorted list. If there are fewer than `k` unique scores, the entire list is used.

5. **Retrieve the user IDs** corresponding to the top `k` unique scores and return them.

---

### **Complexity Analysis**

- **Time Complexity**: \(O(n \log n)\) – Sorting the unique scores dominates the complexity, where \(n\) is the length of the `users` list.
- **Space Complexity**: \(O(n)\) – Storing up to \(n\) unique scores in the dictionary.

This problem is efficient and scalable for large datasets, making it suitable for real-world PLG platforms where user engagement data can be extensive.
