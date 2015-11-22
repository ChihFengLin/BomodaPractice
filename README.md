# BomodaPractice

Q1a:
Count the number of posts mentioning each of the included brand names as well as the users who mentioned them. Hint: Pay attention to the variation of names. 

<command line>
for file in <path to the file>; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py

Q1b:
List the top 10 users and locations (as province level in China and nation level worldwide) for total posts.

<command line>