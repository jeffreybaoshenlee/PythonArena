import os 
def search_file(filename,search_path,pathsep=os.pathsep): 
    for path in search_path.split(pathsep):
        candidate=os.path.join(path,filename)
        if os.path.isfile(candidate):
            return os.path.abspath(candidate)
    return None
search_path='/bin'+os.pathsep+'/users/bin'
find_file=search_file('output.txt',search_path)
if find_file:
    print("file 'output.txt' found at = %s" % find_file)
else:
    print("file output.txt not found")