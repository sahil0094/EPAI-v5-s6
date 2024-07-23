# EPAI-v5-s6

<h1 align="center">Closures</h1>

<h2 align="center"> Assignment Question </h2>

1. Write a closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable - 
2. Write a closure that gives you the next Fibonacci number - 
3. We wrote a closure that counts how many times a function was called. Write a new one that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts - 
4. Modify above such that now we can pass in different dictionary variables to update different dictionaries - 

No readme or no docstring for each function, or no test cases, 0. Write test cases to check boundary conditions that might cause your code to fail. 

<h2 align="center"> Assignment Solution </h2>

Here we have various small tasks as mentioned above, so lets take them one at a time

### Tasks

#### **Task 1**

In this task we need to create a function to check each function has docstring and docstring should be of 50 character each. here we create docstring_cls function which takes the function who has to be checked as a parameter. here we have defined `docstr_len` which is the minimun character count. Then we have defined another function `docstring_check` which is a closure which takes in docstr_len as non local parameter and then checks its length by fetching the dfocstring of the function. It returns a True if docstring is more than 50 characters else returns false

#### **Task 2**

In this Task we need a function to calculate the next fibonacci number, here we define `first` and `second` number as free variables i.e. will be used by `generate_my_next_number` closure and that closure will add these numbers and then will update the value of these numbers and then will return the added result



#### **Task 3**

This task is slight addition to the previous task, here we define 4 functions i.e. `add`, `mul`, `sub`, and `div`. in this task we keep a global dictionary `fn_cnt_dict` to have a check on how many times each operation is being called. so here we define a function `counter` which takes in function as a parameter, the    non local variable  cnt_add, cnt_mul, cnt_div is the value obtained from the key of the global dictioanry as function name. Here we define a closure called inner which takes in  `a` and `b` as parameters, which are the numbers over which each operation will be perfomed. The function updated the global dictionary and returns the count

#### **Task 4**

In this task we need to calculate how many times a function is being called, so to do that we define a `counter_dict` function with cnt_add, cnt_mul, cnt_div  as non local variable. Then we defined `inner` function which updates the variable value and returns it.

### Test Cases

There are test case for to check the working of each task function. There are some general test cases of checking documentation of the project and the python files,There are testcases to check to whether they are acutally closures or not.

---
