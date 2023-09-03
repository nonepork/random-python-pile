import zipfile
import os

path=os.getcwd()

def unzip_rename(src):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        if s.endswith(".zip"):
            with zipfile.ZipFile(s) as zf:
                zf.extractall(pwd=b'infected')
                extractedname = zf.namelist()[0]
                if "vbs" in s:
                    os.rename(src+"\\"+extractedname, s.replace("(vbs).zip", ".vbs.notyet"))
                else:
                    os.rename(src+"\\"+extractedname, s.replace(".zip", ".exe.notyet"))

unzip_rename(path)
