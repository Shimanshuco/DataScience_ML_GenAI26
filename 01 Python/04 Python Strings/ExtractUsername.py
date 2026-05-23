# Extract username from a given email. 
# Eg if the email is himanshusingh@gmail.com
# then the username should be himanshusingh

def extract_username(email):
    index = email.index('@')  # Find the index of '@' in the email
    username = email[:index]  # Extract the substring from the start to the index of '@'
    return username

email = "himanshusingh@gmail.com"
print(extract_username(email))  # Output: himanshusingh
