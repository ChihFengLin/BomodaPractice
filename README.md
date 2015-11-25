# BomodaPractice

Data Location:
https://drive.google.com/file/d/0B5ADI2usunVQOGU5RE5tT281Tzg/view?usp=sharing

Q1a:
Count the number of posts mentioning each of the included brand names as well as the users who mentioned them. Hint: Pay attention to the variation of names. 

* **command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py**

Q1b:
List the top 10 users and locations (as province level in China and nation level worldwide) for total posts.

**Top 10 users:**
**command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer1.py**

**Top 10 locations:**
**command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k2,2 | python reducer2.py**

Q2a:
Find the date that has the highest number of posts mentioning each of the brands

**command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py**

Q2b:
Find the peak hour with the most posts.

**command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1| python combiner.py | sort -k1,1 | python reducer.py**

Q3:
Tokenize the comments and retrieve the top 10 mentioned Chinese terms associated with each brand from the texts. You may use 3rd party libraries such as Jieba to complete this task.

**command line> for file in /path/to/the/comment/; do cat $file | python mapper.py; done | sort -k1,1 | python combiner.py | python mapper2.py | LC_ALL='C' sort -k1,1 | python reducer.py**

Q4a: 
Count the number of reposts and comments per day (as separate counts), per brand

This command line can get number of comments per day per brand

**command line> for file in /path/to/the/comment/; do cat $file | python mapper1.py; done | sort -k1,1| python combiner1.py | sort -k1,1 | python reducer1.py**

This command line can get number of reposts per day per brand

**command line> for file in /path/to/the/reposts/; do cat $file | python mapper2.py; done | sort -k1,1 | python combiner2.py | sort -k1,1 | python reducer2.py**

Q4b: Plot the count over the entire timeframe (For this problem, currently I only analyze comments data. For repost data, there are some bugs.)

**command line> cat comment_statistic.txt | python plotgraph.py**


