

import numpy as np

# Assign 1,000 simulated user profiles
num_users = 1000

# Initialize an empty list for user names
user_names = []

# Loop through a range of numbers equal to num_users
for i in range(1, num_users + 1):
    # Create a user name string for each number and append it to the list
    user_name = "User" + str(i)
    user_names.append(user_name)

# Convert the list of user names to a NumPy array
user_names = np.array(user_names)

# Randomly simulate account categories for each user profile from given choices
user_types = np.random.choice(["Residential", "Business", "Educational"], num_users)

# Pair user_profiles and user_types into 2D array 
user_profiles = np.column_stack((user_names, user_types))

# Print sample user profiles
print("Sample User Profiles:")
print(user_profiles[:5])

# List of 12 months in year 2024
months = [
    "Jan2024", "Feb2024", "Mar2024", "Apr2024",
    "May2024", "Jun2024", "Jul2024", "Aug2024",
    "Sep2024", "Oct2024", "Nov2024", "Dec2024"
]

