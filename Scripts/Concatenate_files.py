import os,shutil
f=open("/media/6A2CC16C2CC1343B/Projects/NLP/categorized_txt_files/fileappend.txt","a")
for r,d,fi in os.walk("/media/6A2CC16C2CC1343B/Projects/NLP/categorized_txt_files/607-AH/"):
    for files in fi:
        if files.endswith(".txt"):                         
            g=open(os.path.join(r,files))
            shutil.copyfileobj(g,f)
            g.close()
f.close()
