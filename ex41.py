import random
from urllib.request import urlopen
import sys

WORD_URL="http://learncodehehardway.org/words.txt"
WORD =[]

PHRASES={
        "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
        "class %%%(object):\n\tdef __ init__(self,***)":
        "class %%% has-a __init__that takes self and ***para
        "class %%%(object):\n\tdef ***(self,@@@)":
        "class %%% has-a function *** that takes self and @@@
        "***=%%%()":
        "Set *** to an instance of class %%%.",
        "j***.***(@@@)":
        "From *** get the*** attribute and set it to '***'."
        }

#do they want to drill phrases first 
if len(sys.argv)==2 and sys.argv[1]=="english":
    PHRASE_FIRST=True
else:
    PHRASE_FIRS=False

#load up the world from the website
for world in urlopen(WORLD_URL).readlines():
    WORDS.append(str(word.strip(),encoding="utf-8"))


    def convert (snippet ,phrase):
        class_names=[w.capitalice()for win
                     random.sample(WORLD,snipper.count("%%%"
           other_names=random.sample(WORLD,snipper.count("***")
               results=[]
               param_name=[]

               for i.in range(0,snippet.count("@@@")):
               param_count=random.randit(1,3)
               param_names.append(','.join(
                   random.sample(WORDS.param_count)))

               for sentence in snippet ,phrase:
               result=sentence[:]

               #fake class names
               for world in class names:
               result=result.replace("%%%",word,l)
               #fake other name
               for word in other_names:
               result=result.replace("***",word ,l)

               #fake parameter lists
               for word in param_names:
               result=result.replace("@@@",word,l

                   return resluts


                   #keep going until they hit CTRL_D
                   try:
                   while True:
                   snippets=list(PHRASES.keys())
                   random.shuffle(snippets)

                   for snippet in snippets:
                   phrase=PHRASES[snippet]
                   question,answer=convert(snippet,phrase)
                   if PHRASE_FIRST:
                   question,answer=answer,question

                   print(question)

                   input(">")
                   print(f"ANSWER"{answer}\n\n")
                   except EOFError:
                   print("\nBye")
