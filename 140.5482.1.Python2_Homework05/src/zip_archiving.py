import zipfile
import os
import glob
import shutil
os.chdir("V:\\workspace\\Python2_Homework05")

def arch(path="V:\\workspace\\Python2_Homework05\\src"):
    
    if path.endswith(os.sep):
        path = path[0:-1]
        
    tp = os.path.basename(path)+os.sep
    archive_f = tp+".zip"
    #print(os.path.abspath(archive_f))
    f = glob.glob(os.path.join(path,'*.*'))
    zf = zipfile.ZipFile(archive_f, "w")
    for el in f:
        if os.path.isfile(el):
            zf.write(os.path.join(tp, os.path.basename(el)))
            #print(os.path.join(tp,os.path.basename(el)))
    zf.close()
    z = zipfile.ZipFile(archive_f, "r")
    ret_z = z.namelist()
    z.close()
    
    return ret_z

if __name__ == "__main__":
    x = arch()
    for el in x:
        print(el)
    