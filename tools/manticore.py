import os
import shutil
import time

def run_manticore(p):
    (filename, contract, extra_args) = p
    coverage = None
    
    cdir = "temp/manticore_"+filename.replace("/","_")+".dir"
    shutil.rmtree(cdir, ignore_errors=True)
    os.mkdir(cdir)
    os.chdir(cdir)

    cmd = 'manticore ../../'+filename+' --contract '+contract+' '+extra_args+' --core.timeout 120 --txlimit 1 --core.procs 1 --evm.oog ignore > manticore.out 2> manticore.err'
    start = time.time()
    os.system(cmd)
    end = time.time()
   
    os.chdir('../..')
    return (filename, coverage, end - start)
