# just pasted somethere in your script, to help the time and the changes of the script.
from time import gmtime, strftime

start_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
with open('res_0723.txt', 'a') as f:
    f.write("the new run starts at : %s \n"%(start_time))
    f.write("the new change is: %s\n"%('YOUR COMMENTS'))
