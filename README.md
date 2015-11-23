# BomodaPractice

Q1a:
Count the number of posts mentioning each of the included brand names as well as the users who mentioned them. Hint: Pay attention to the variation of names. 

command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py

Q1b:
List the top 10 users and locations (as province level in China and nation level worldwide) for total posts.

Top 10 users:
command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer1.py

Top 10 locations:
command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k2,2 | python reducer2.py

Q2a:
Find the date that has the highest number of posts mentioning each of the brands
command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py

Q2b:
Find the peak hour with the most posts.
command line>