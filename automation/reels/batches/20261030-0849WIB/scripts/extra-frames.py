import json,subprocess
items=json.load(open('out/manifest.json'))
for i in items:
 subprocess.run(['ffmpeg','-v','error','-y','-i',i['local_path'],'-vf',"select='eq(n,119)+eq(n,125)+eq(n,145)+eq(n,610)+eq(n,930)',scale=270:480,tile=5x1",'-frames:v','1',f'out/{i["id"]}-transition-contact.jpg'],check=True)
print('Final transitions and hold zooms extracted')
