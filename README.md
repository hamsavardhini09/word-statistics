CS6065
P1 Docker


Please use below steps to load docker image run wordstatistics

Extract gz file by changing current directory to download folder
gzip -d wordstatistics.tar.gz

load tar file into docker using load -i option
docker load -i wordstatistics.tar

Run loaded image using below command
docker run -d -p 5555:5555 wordstatistics /home/startme.sh

If there are any issues with startme, update first line in startme to below command and run again
#!/bin/bash

To edit startme first login in to docker instance
docker run -it -p 5555:5555 wordstatistics 

go to /home forlder
cd /home

edit startme file using vi
vi startme.sh

After file is successfull edited and saved. execute below command 
sh startme.sh

Also verify under /home fikder all folders have 777 permissions. To give permissions use below command
chmod 777 *

Please use below url to access application
http://localhost:5555/wordstatistics


There is a option to post a file of text with "the_file" parameter and post to te same URL using postman extension of chrome or poster plugin in firefox.
Similar to get statistics post also will give similar statistics of text in the given file.


The optput is json formatted word statistics. Input is text and is given to find some statistics such as number of words,unique words, unique words-word count, duplicate words, duplicate words count, words with vowels, words with vowel percentage, words with consonents, words wit consonents percentage, top 10 words frequency, words begin with vowels.

Future scope:
Its good to add some more statistics like character statstics, sentence statistics, string operations and sentiment for the given sentences. A nice UI like textalyser.net will help user to understand about the text feeded to application. Future works like Twitter Tweets, Blogger Data, Facebook Feeds will help companies to know analyse what words customers are using mode while talking about them.



