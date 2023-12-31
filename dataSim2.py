"""
Telecom User Data Simulator with Visualizations:

This script generates simulated data for telecom users, including user profiles 
and their monthly usage data, including data consumption, voice call minutes, and 
text messages over the year 2024.

"""

# DATA SIMULATION
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

# Initialize empty list for monthly data
monthly_usage_data = []

# Defines function, assigns 3 different tiers conditioned on data usage per user
def plan_category(data_usage, voice_call_minutes, text_messages):
    """
    Categorizes a telecom user into a plan based on their usage data.

    Parameters:
    data_usage (float): The amount of data used by the user in GB.
    voice_call_minutes (int): Total minutes of voice calls made by the user.
    text_messages (int): Number of text messages sent by the user.

    Returns:
    str: The category of the plan - 'Premium', 'Unlimited', or 'Basic'.
    """
    if data_usage >= 251 and data_usage <= 799:
        return "Premium"
    elif data_usage >= 800 or voice_call_minutes >= 2001 or text_messages >= 3750:
        return "Unlimited"
    else:
        return "Basic"

# For loop to iterate through each month, randomly, assigning data values
for month in months:

    # Simulate data usage between 0.1GB to 1000GB
    data_usage = np.random.uniform(0.1, 1000, num_users)

    # Simulate voice call minutes between 0 to 3000 minutes
    voice_call_minutes = np.random.randint(0, 3001, num_users)

    # Simulate text messages between 0 to 5000
    text_messages = np.random.randint(0, 5001, num_users)

    # Initialize empty list for plan categories
    plan_categories = []

    # For loop iterates through 'ith' index of each data category
    for i in range(num_users):
        user_data_usage = data_usage[i]
        user_voice_call_minutes = voice_call_minutes[i]
        user_text_messages = text_messages[i]

        # Calls function with variable
        user_plan_categories = plan_category(user_data_usage, user_voice_call_minutes, user_text_messages)

        # Appends function call variable to plan_categories list
        plan_categories.append(user_plan_categories)
        
# Stacks 1D arrays into 2D arrays of columns, and each row represents users values for that month
    month_data = np.column_stack((user_names, [month]*num_users, data_usage, voice_call_minutes, text_messages, plan_categories))
    
    # Appends month_data to monthly_usage_data
    monthly_usage_data.append(month_data)   

# stacks 2D arrays vertically into a single 2D array
monthly_usage_data = np.vstack(monthly_usage_data) 

# Print a summary or sample of the complete dataset
print("\nComplete Data Sample:")
print(monthly_usage_data[:10])


# DATA VISUALIZATION
"""
This section converts the simulated telecom user data into a pandas DataFrame for easier manipulation. 
Then it converts specific columns from strings to numeric types for accurate analysis. Finally, it 
uses matplotlib to create histograms that visualize the distribution of data usage, voice call minutes, and text 
messages for the telecom users.

"""

import pandas as pd

# Convert monthly_usage_data array into DataFrame for more efficient data manipulation
column_names = ["userName", "monthYear", "dataUsage", "voiceCallMinutes", "textMessages", "planCategory"]  
df = pd.DataFrame(monthly_usage_data, columns=column_names)

# Convert monthly_usage_data from strings to numeric types for accurate numerical analysis
df["dataUsage"] = pd.to_numeric(df["dataUsage"])
df["voiceCallMinutes"] = pd.to_numeric(df["voiceCallMinutes"])
df["textMessages"] = pd.to_numeric(df["textMessages"])

import matplotlib.pyplot as plt

# Histogram for dataUsage
df["dataUsage"].hist(bins=20, ec= "black")
plt.title("Data Usage Distribution")
plt.xlabel("Data Usage (GB)")
plt.ylabel("Frequency")
plt.show()

# Histogram for voiceCallMinutes
df["voiceCallMinutes"].hist(bins=20, ec= "black")
plt.title("Voice Call Minutes Distribution")
plt.xlabel("Voice Call Minutes")
plt.ylabel("Frequency")
plt.show()

# Histogram for textMessages
df["textMessages"].hist(bins=20, ec= "black")        
plt.title("Text Messages Distribution")
plt.xlabel("Text Messages")
plt.ylabel("Frequency")
plt.show()






