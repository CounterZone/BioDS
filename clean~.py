import os
rdir="./"
def ch(dir):
	for l in os.listdir(dir):
		path=os.path.join(dir,l)
		if os.path.isdir(path):
			ch(path)
		else:
			if l[-1]=='~':
				os.remove(path)
				print "Delete",path
ch(rdir)
