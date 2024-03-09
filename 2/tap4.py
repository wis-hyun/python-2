import sys
src=sys.argv[1]
dst=sys.argv[2]

print(src, dst)

f=open(src)
tab_content = f.read()
f.close()
print(tab_content)
space_content = tab_content.replace('\t',' '*4)
print(space_content)