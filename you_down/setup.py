from setuptools import setup 
import sys,py2exe , os 



sys.argv.append("py2exe")


setup(

options={'py2exe':{'bundle_files':1,"compressed":True}},
windows=[{'script':"you_down.py"}],
zipfile=None,

)