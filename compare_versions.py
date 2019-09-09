
# coding: utf-8

# In[8]:


# A helper function to determine if a version string is a valid version
# Returns True if it is not valid and returns False if it is valid
def not_valid_version(version):
    # assume the version string should start with a number, not '.' or other characters
    if not (version[0]>='0' and version[0]<='9'):
        return True
    
    for character in version:
        if character!='.' and not (character>='0' and character<='9'):
            return True
    
    return False


# In[9]:


# Function to compare two version strings 
# Input: two strings representing versions
# Output: 1, -1, or 0 if the first version is greater than/smaller than/the same as the second
def greater_than(v1, v2):
    # Check if the input strings are valid arguments
    if not_valid_version(v1):
        raise ValueError("The first input version string is not valid")
    if not_valid_version(v2):
        raise ValueError("The second input version string is not valid") 
    
    # extract versions
    ver1 = v1.split('.')
    ver2 = v2.split('.')
    
    # loop and compare until finishing checking one of the version string 
    while (len(ver1)!=0 and len(ver2)!=0):
        # return 1 if the first version is greater than the second
        if ver1[0]>ver2[0]:
            return 1
        # return -1 if the first version is greater than the second
        elif ver1[0]<ver2[0]:
            return -1
        else:
            ver1.pop(0)
            ver2.pop(0)
    
    # return 0 if the first version is the same as the second
    return 0        

