
# coding: utf-8

# In[1]:


# Question A
# Function to determine whether two line segments on x axis overlap
# Input: two tuples, one for the first line and the other for the second line
# Example: input (1,5) , (2,6)  returns True    input (1,5) , (6,8)  returns False
def line_overlap(line1, line2):
    if (line1[1]>=line2[0] and line1[1]<=line2[1]) or (line[0]>=line2[0] and line[0]<=line2[1]):
        return True
    else:
        return False


# In[2]:


print(line_overlap((1,5) , (2,6)))
print(line_overlap((1,5) , (6,8)))

