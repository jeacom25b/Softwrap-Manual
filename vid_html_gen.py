import os
from os import path
import re

vid_ext = set('mp4 mkv m4v ogg'.split())
def ext_replace(file_name, ext):
    return re.sub(f'({"|".join(vid_ext)})$', ext, file_name)

def minify(string):
    return re.sub('\s+', ' ', string)

vid_embed_dir = path.join('docs', 'vid_embed')
if not path.isdir(vid_embed_dir):
    os.mkdir(vid_embed_dir)

for folder, dirs, files in os.walk('docs'):
    for file in files:
        if file.lower().split('.')[-1] in vid_ext:
            page = minify(f'''
            <body>
                <video width="100%" height="100%" autoplay loop muted playsinline
                src="..{'/'.join([folder.lstrip('docs'), file])}" style='max-width:100%'></video>
            </body>
            ''')
            html_name = ext_replace(file, 'html')
            print(f'creating {html_name} for', file)
            with open(path.join(vid_embed_dir, html_name), 'w') as f:
                f.write(page)
                pass
