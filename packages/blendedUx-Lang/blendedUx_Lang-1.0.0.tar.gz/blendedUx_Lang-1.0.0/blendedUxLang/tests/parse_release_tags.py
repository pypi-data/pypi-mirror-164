import os, sys, json

with open('../jinja_release_tags.json', 'r') as myfile:
  release_dict = json.load(myfile)

ver_names = list(map(lambda x: x['name'], release_dict))
latest = ver_names[0]
ver_names = ver_names[1:]
builds = []
for ver in ver_names:
  parts = ver.split('.')
  if len(parts) == len(list(filter(lambda x : x.isdigit(), parts))) == 2 and len(builds)<=2:
    builds.append(ver)

for i in range(0, 3):
  os.putenv("VER_%s" %(i+1), builds[i]) 


  
