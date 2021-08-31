#!/usr/bin/env python
# coding: utf-8

# # Python Pre-Work Review - Loops and Functions
# 
# Your first pair programming exercise!
# 
# Feel like you missed what pair programming is supposed to be all about? [Check out the writeup in the Recipe for Success document](https://docs.google.com/document/d/1ralB2OeWVMZdWWG0mf8U7-cy-M5Xe01toxbmQGlB1AY/edit#heading=h.hsv76gt73puu)

# ## Learning goals:
# 
# Today we will:
# 
# - Revisit what we can do with for loops, using dictionaries
# - Recognize function arguments, and write functions both with and without arguments (and with default values!)
# - Write functions that build up from for loops
# 
# Some new things we're bringing up that may not have been covered before:
# 
# - using `.items()` with dictionaries to call both the dictionary keys and the dictionary values
# - formatting f-strings to print a certain number of decimal places
# 
# ## Scenario
# 
# ![cat pushing a shopping cart](images/cat_shopping_cart.jpg)
# 
# Who has ever gotten to the cash register at Costco, or Whole Foods, or Target, then seen the total and asked, _"How did I spend that much?!"_ 
# 
# We have a grocery list of items and prices, but we do not have infinite money (unfortunately), so let's use Python help us manage our shopping and expenses.

# ### For Loops:
# 
# Let's revisit for loops. Below, we have a list of items, and a separate list of costs. Let's build up to where we can write a loop to print each item, its cost, and the total of our grocery list.

# In[61]:


# Run this cell without changes
# Here is our grocery list
items = ['cheese', 'whole milk', 'kefir', 'tofu four-pack', 'kale', 'oranges', 
         'ham', "ben & jerry's"]

# Here is our cost list
cost = [2.79, 3.42, 4.50, 12.00, 2.75, 3.64, 25.00, 5.29]


# Let's make that a little nicer looking. 
# 
# Create a `for` loop that prints each item in the list with "I need to buy: " + item:

# In[62]:


# Write your for loop
for item in items:
    print('I need to buy: ' + item)


# Okay, we want to work through a dictionary, so what can you do to convert those two lists to a single dictionary?
# 
# (You can also write up that dictionary manually, that works too!)

# In[63]:


# Replace None with appropriate code to create your dictionary
grocery_dict = dict(zip(items, cost))


# In[64]:


# Check your work
grocery_dict


# So let's now add the total grocery bill at the end for these items:
# 
# (use the dictionary's values, not the cost list from before!)

# In[69]:


# Calculate your sum
total = 0
for number in grocery_dict.values():
    total += number
    
print(total)    


# Gah! What if we're trying to be frugal?
# 
# One way to do that would be to not buy any item that's more expensive than $10.
# 
# Here's a hint: `.items()` will create two variables from a dictionary, one with the keys and one with the values. Let's use `.items()`, conditionals, and a for loop to only add items that are cheaper then $10 to our total:

# In[70]:


# Code here to only add items to our total if they're <$10
frugal_sum = 0
for key, value in grocery_dict.items():
    if value < 10:
        frugal_sum += value
    


# In[67]:


# Check your work
print(frugal_sum)


# ### Functions:
# 
# Just a note - it's always best practice to follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) standards when writing Python code. The [standard for function names](https://www.python.org/dev/peps/pep-0008/#function-and-variable-names) is that they are lowercase, separated by underscores - same as variable names.

# #### Quiz question!  `print` vs `return` ?
# 
# Can you describe the difference between `print` and `return` as a function output? 
# 
# - 
# 

# #### Back to our shopping list:
# 
# Adapt your shopping list's for loop into a function that takes a dictionary, where the key is the name of the item and the value is its cost, and only adds items if they are less than $10. 
# 
# It should return the total cost without items that cost more than $10.

# In[71]:


# You may want to paste your previous for loop here
frugal_sum = 0
for key, value in grocery_dict.items():
    if value < 10:
        frugal_sum += value


# In[72]:


# Replace pass with the appropriate code
def calc_frugal_total(dictionary):
    '''
    Returns a frugal grocery list sum, that only includes items that cost less
    than $10
    
    Input: dictionary (expects key is item name, value is item cost)
    Output: sum (float)
    '''
    total = 0
    for key, value in dictionary.items():
        if value < 10:
            total += value
    return total


# In[73]:


# Run this cell without changes to check your work
calc_frugal_total(grocery_dict)


# ### Nested Dictionaries
# 
# Here is a more robust shopping list of nested dictionaries:

# In[74]:


# Run this cell without changes
shopping_dict = {'Groceries': {"ben & jerry's": 5.29, 'cheese': 2.79, 
                               'ham': 25.0, 'kale': 2.75, 'kefir': 4.5, 
                               'oranges': 3.64, 'tofu four-pack': 12.0, 
                               'whole milk': 3.42},
                 'House Supplies': {'toilet paper pack': 16.50, 
                                    'clorox spray': 6.43, 'kleenex': 2.50, },
                 'Pet Supplies': {'fancy grain-free kibble': 65.25, 
                                  'squeaky toy': 4.50, 'treats': 8.45}}


# Nested dictionaries call for nested for loops! Write a set of nested for loops that create a total grocery list, so we have just one list to take to the store and find what we need.

# In[75]:


# Code to write your nested loops
L = []
for item in shopping_dict.values():
    for i in item.keys():
        L.append(i)


# In[76]:


# Check your work
print(L)


# Now let's turn that into a function that, when given nested dictionaries, returns a list of each item as our grocery list to take with us to the store. It should also print our expected total, so we know how much we expect to spend.
# 
# Use [this link](https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings) for help in formatting the total to two decimal places using an f-string - not required, but it'll print out nicer!

# In[85]:


# Replace pass with appropriate code
def write_grocery_list(nested_dict):
    L = []
    total = 0
    for item in nested_dict.values():
        for i in item.keys():
            total += item[i]
            L.append(i)
    print(f"The total amount is {total:.2f}")
    return L        


# In[86]:


# Run this cell without changes to check your work
write_grocery_list(shopping_dict)


# ## Level Up:
# 
# Adapt your grocery function to do the following:
# 
# - flag expensive items that cost more than $20, and do not add them to your list
# 
# - block items that will push the total cost above $50
# 
# - print out the average cost per item on your list
# 
# It should still take in a nested dictionary, and return your grocery list.
# 
# **Extra bonus points:** add a [docstring](https://www.python.org/dev/peps/pep-0257/)! 
# 
# You can see an example of a docstring up above, where I used triple quotes (''') to write a multi-line string directly under where I defined my `calc_frugal_total` function. That multi-line string is a docstring, and you should get in the habit of using docstrings to describe expected behavior, as well as expected inputs and outputs, for your functions. Best part - after you've defined a function, you can call that docstring by running `help()` around your function, or by clicking into the parentheses after your function and clicking SHIFT+TAB in a juptyer notebook. Test it out!

# In[130]:


# Code your leveled-up function here
def write_grocery_list(nested_dict):
    '''
    Returns a frugal grocery list (that only includes items that each cost less
    than $20 and total shopping amount less than $50), 
    average cost per item and 
    total amount.
    
    Input: nested dictionary 
    Output: Grocery list, average cost per item, and total sum of that list
    '''
    L = []
    P = []
    total = 0
    for category, shop_list in nested_dict.items():
        for item, price in shop_list.items():
            if price < 20:
                if total > 50:
                    pass
                else:
                    total += price
                    P.append(price)
                    L.append(item)
                              
    print(f"The shopping list: {L}"), 
    print(f"The average cost per item: {P}") 
    print( )
    print(f"The total amount: {total:.2f}")
    return 


# In[131]:


# Check your work
write_grocery_list(shopping_dict)


# In[ ]:




