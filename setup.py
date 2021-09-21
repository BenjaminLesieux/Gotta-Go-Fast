from subprocess import call

packages = ["pygame"]

for pack in packages:
    call("pip install " + pack, shell=True)
