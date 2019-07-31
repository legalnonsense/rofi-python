#!/usr/bin/env python3
import subprocess

class rofi_python:
    """Use python to run Rofi and get output from it.
       You must pass the entire rofi command as an argument."""

    def __init__(self):
        pass 
    
    def __process_rofi_output(self, s):
        """Private method to process Rofi's output and return data in the form of (last_query [string], results [list])"""
        ts=s.split('\n')
        strings=[]

        for x in range(len(ts)):
            for s in ts[x].split("''"):
                strings.append(s)

        for x in range(len(strings)):
            strings[x] = strings[x].strip()
            try: 
                if strings[x][0] == "'":
                    strings[x]=strings[x][1:]
                if strings[x][-1] == "'":
                    strings[x]=strings[x][:-1]
            except: pass 
        last_query = strings[0].strip()
        results = []
        for ss in strings[1:]:
            if (ss.strip()==last_query) or (ss.strip()==''):
                pass
            else:
                results.append(ss)
        return(last_query, results)

    def run(self, rofi_command, inputs):
        """Run Rofi with rofi_command (a command line string)
                     and inputs (a list of items to choose from)
           Returns a list in the format (last_query, results)"""
        p = subprocess.Popen(rofi_command.split(), stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        p.stdin.write("\n".join(inputs).encode('utf-8'))
        s=p.communicate()[0].decode('utf-8')
        return __process_rofi_output(s)


    def dump(self, rofi_command, inputs, rofi_search_text):
        """Run Rofi with rofi_command (a string), inputs (a list of choices), and rofi_search (the search text)
           Returns inputs, filtered using rofi_search
           Don't pass the -dump argument, or the -filter argument. Both of these are added to your rofi command automatically."""
        rofi_command += " -dump"
        rofi_command += " -filter " + rofi_search_text
        p = subprocess.Popen(rofi_command.split(), stdout = subprocess.PIPE, stdin = subprocess.PIPE)
        p.stdin.write("\n".join(inputs).encode('utf-8'))
        s=p.communicate()[0].decode('utf-8')
        return __process_rofi_output(s)



if __name__=="__main__":
    rofi = rofi_python()

    rofi_command = 'rofi -dmenu "$@" -no-sort -l 50 -i -p Copy -format Fq -width 2500 -multi-select'
    rofi_list =  ['these', 'are', 'your', 'choices']
    rofi_search_text = 'r'

    p = subprocess.Popen('find /home/jeff/Dropbox -type d'.split(), stdout=subprocess.PIPE)
    out = p.communicate()
    

    #Print(rofi.run(rofi_command, rofi_list))
    dump=rofi.dump(rofi_command, rofi_list, rofi_search_text)
    print(rofi.run(rofi_command, dump[1]))
    








