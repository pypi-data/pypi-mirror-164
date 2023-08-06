# witertools.

witertools provides:
- functions that take a function that returns and iterator, and return a function that returns list.  
- wrappers around built in functions that return iterators (filter, map, and zip)
- wrappers around the functions in itertools except count, cycle, and repeat
- wrappers around the functions in more_itertools 

The motivation as that itertools and more-itertools in particular have functions that return iterators, but very frequently 
the desired result is a list. Over and over in code you will see repeated code of calling list on the result of a function
that produces an interator.  You will even see it in most examples in the [more-itertools api](https://more-itertools.readthedocs.io/en/stable/api.html).  



## Wrappers Around Functions that Return Iterators
In witertools:
iterator_to_list_function will take a function that returns an iterable, and return a function that returns a list.

```
>>> from witertools import *
>>> f=iterator_to_list_function(filter)
>>> w.filter(lambda s: True, [3,4,5])     
[3, 4, 5]
```

iterator_name_to_list_function will take a module object and a function name, and return a function that returns a list.
```
>> g=iterator_name_to_list_function(__builtins__,"filter") 
>>> g(lambda s : True , [1,2]) 
[1, 2]
```

## Wrappers Around Built in Functions
To use a wrapper around a built in function, just use a function from the same name from the 
witertools package.
```
>>> import witertools as w 
>>> w.filter(lambda s: True, [3,4,5])
[3, 4, 5]
```

which replaces

```>>> list(filter(lambda s: True, [3,4,5]))
[3, 4, 5]
```

## Wrappers Around itertools 

Use a function from the witertools.itertools namespace, with the same name as the function in the itertools namespace.

```>>> import witertools.itertools as i      
>>> i.chain([1,3],[4,5])
[1, 3, 4, 5]
```

## Wrappers Around more-itertools

 Use a function from the witertools.more_itertools namespace, with the same name as the function in the more-itertools namespace.  You will need to install more-itertools to use these functions, as more-itertools as not a prequisite of witertools.

```
>>> from witertools.more_itertools import chunked
>>> chunked([1, 2, 3, 4, 5, 6], 3)
[[1, 2, 3], [4, 5, 6]]
```

There are a few functions in more_itertools that do not return iterables.  For example, nth_or_last.
These functions are still wrapped in witertools.more_itertools but will result in a traceback.

```
>>> from witertools.more_itertools import  nth_or_last
>>> nth_or_last([0, 1, 2, 3], 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Program Files (x86)\Python39-32\lib\site-packages\witertools\iterator_to_list.py", line 7, in as_list
    return list(iterator_function(*args,**kwargs))
TypeError: 'int' object is not iterable
```

