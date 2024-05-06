import os
from git import Repo
import datetime as dt
tgl = dt.datetime.now().strftime("%y%m%d_%H%M%S")
os.chdir('../downloadadmin')
import shutil
shutil.make_archive('HEINZO', 'zip', '/content/images')
full_local_path = "/content/downloadadmin"

backupname = "/content/downloadadmin/HEINZO.zip"
backup = ('/content/downloadadmin/H' + str(tgl) + '.zip')
os.rename(backupname, backup)


repo = Repo(full_local_path)
repo.git.add("-A")
repo.index.commit("admin")

#repo = Repo(full_local_path)
origin = repo.remote(name="origin")
origin.push()


os.chdir('..')
