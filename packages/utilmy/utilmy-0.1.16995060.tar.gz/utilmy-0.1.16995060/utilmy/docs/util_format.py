""" Tools to format all python code automatically

#### Remove all Docstring, comments:

    python $dirutilmy/docs/util_format.py     run_clean  --dirin youpath/**/*.py   --diroot yourpath/   --dirout yourpath2/   --dryrun 1 







"""

import os 
from utilmy import log 


def run_clean(dirin, diroot=None, dirout=None, dryrun=1, tag="", checkcode=1, verbose=0):
    """ 
        python src/utils/utilmy_base.py run_clean --dirin "ztmp/*.py" --diroot "ztmp/"    --dirout ztmp/ztmp2/  --dryrun 0
    
    """
    from utilmy import glob_glob, os_makedirs, log
    import re, ast, traceback
    flist = glob_glob(dirin)
    log('N Files', len(flist))
    for fi in flist:
        if verbose>0: log(fi)
        try :
            with open(fi, 'r') as file1:
                data = file1.read()

            data = code_clean_dc(data)
            
            if checkcode>0:
                # log('checkcode')
                try:
                    ast.parse(data)
                except Exception as e:
                    log(fi, ":", e)
                    log(e)
                    traceback.print_exc()  # Remove to silence any errros
                    continue
            
            fi2 = fi
            if dirout is not None and str(diroot) in fi:
                fi2 = fi.replace(diroot, dirout)
                
            fi2 = fi2.replace(".py", f"{tag}.py" ) 
                
            os_makedirs(fi2)    
            if dryrun == 0 :        
                with open(fi2, 'w') as file1:
                    file1.write(data)
                    log('done', fi2)       
            else:
                log('dryrun', fi2)       
        except Exception as e :
            log(fi, e)   



def code_clean_dc(code):
    # Define markers for triple double quotes and triple single quotes
    DOC_DQ = '"""'
    DOC_SQ = "''''"
    
    code = code.split("\n")

    codenew = ""
    is_open_doc_string = False

    for line in code:
        line2 = line.strip()
        if line2.startswith((DOC_DQ, DOC_SQ)) and line2.endswith((DOC_DQ, DOC_SQ)) and len(line2) > 3 :
            is_open_doc_string = False
            continue
        
        if line.strip().startswith((DOC_DQ, DOC_SQ)) :
            is_open_doc_string = not is_open_doc_string
            continue  # Skip 

        if not is_open_doc_string :
            codenew += line + "\n"
            
    return codenew[:-1] 



if __name__ == "__main__":
    fire.Fire()


