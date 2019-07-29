#!/usr/bin/env python3
import subprocess


def _process_rofi_output(s):
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

    #strings[x] = "'" + strings[x] + "'"
    
    last_query = strings[0].strip()
    results = []

    for ss in strings[1:]:
        if (ss.strip()==last_query) or (ss.strip()==''):
            pass
        else:
            results.append(ss)

    return(last_query, results)


def run_rofi(rofi_command, inputs):
    p = subprocess.Popen(rofi_command.split(), stdout = subprocess.PIPE, stdin = subprocess.PIPE)
    p.stdin.write("\n".join(inputs).encode('utf-8'))
    s=p.communicate()[0].decode('utf-8')
    return process_rofi_output(s)




print(run_rofi('rofi -dmenu "$@" -no-sort -l 50 -i -p Copy -format Fq -width 2500 -multi-select', ['these', 'are', 'your', 'choices']))




