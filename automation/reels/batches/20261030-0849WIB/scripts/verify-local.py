from pathlib import Path
import subprocess,json,hashlib,re
items=json.load(open('out/manifest.json'));r=[]
for i in items:
 p=Path(i['local_path']);probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration,size:stream=codec_name,width,height,r_frame_rate,pix_fmt,sample_rate,channels','-of','json',str(p)],text=True));v=next(x for x in probe['streams'] if x.get('width'));a=next(x for x in probe['streams'] if x.get('codec_name')=='aac');assert v['width']==1080 and v['height']==1920 and v['codec_name']=='h264' and v['pix_fmt']=='yuv420p' and v['r_frame_rate']=='30/1';assert abs(float(probe['format']['duration'])-42)<.1;assert hashlib.sha256(p.read_bytes()).hexdigest()==i['sha256']
 audio=subprocess.run(['ffmpeg','-hide_banner','-i',str(p),'-af','volumedetect','-vn','-f','null','-'],capture_output=True,text=True,check=True);peak=float(re.search(r'max_volume: ([-\d.]+) dB',audio.stderr).group(1));assert peak<0
 r.append(dict(id=i['id'],size=i['size'],sha256=i['sha256'],output_path=i['output_path'],local_path=str(p.resolve()),gitsha=subprocess.check_output(['git','hash-object',str(p)],text=True).strip(),audio_peak_dbfs=peak,duration=42))
Path('out/slim-manifest.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
