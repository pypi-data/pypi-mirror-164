"""
indi game engine
"""

import os.path
from _igeEffekseer import *

try:
    import igeCore as core
except:
    print('ERROR: igeCore is NOT installed')
    sys.exit(1)

textures = {}
def f_texture_loader(name, type):
    tex = core.texture(name)
    textures[name] = tex
    print("efk_texture loaded: " + name + " => " + str(tex.id))
    return (tex.width, tex.height, tex.id, tex.numMips > 1)

texture_loader(f_texture_loader)

def isHiddenFolder(path):
    if path.find('/.') != -1 or path.find('\\.') != -1 :
        return True
    return False

def findEfkfcFiles(path):
    list = []
    for root, dirs, files in os.walk(path):
        if isHiddenFolder(root): continue
        for fname in files:
            name, ext = os.path.splitext(fname)
            if ext == '.efkefc':
                list.append(os.path.join(root, fname))
    return list

def replaceExt(file, ext):
    name, extold = os.path.splitext(file)
    return name + ext

def openEditor():
    try:
        import subprocess
        dirname = os.path.dirname(__file__)
        exePath = os.path.join(dirname, "Tool/Effekseer.exe")
        subprocess.run(exePath)
    except:
        print("ERROR: Effekseer is NOT installed")

def exportEfk(inputFile, outputFile):
    try:
        import subprocess
        dirname = os.path.dirname(__file__)
        exePath = os.path.join(dirname, "Tool/Effekseer.exe")
        cl = exePath + " -cui -in "+ inputFile  + " -e " + outputFile
        print("convert : " + inputFile)
        subprocess.run(cl)
    except:
        print("ERROR: Effekseer is NOT installed")

def exportAllEfk(sourceDir, destDir):
    effList = findEfkfcFiles(sourceDir)
    for file in effList:
        outfile = os.path.normpath(file.replace(sourceDir, destDir, 1))
        outfile = replaceExt(outfile, '.efk')
        exportEfk(file, outfile)
