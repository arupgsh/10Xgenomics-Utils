from glob import glob
import shutil, os
import sys

'''
Copy and rename all the Web Summary files from all Cell Ranger count runs in the current directory's Reports folder.
Usage: python copy_10x_web_summary.py <parent directory path>
'''

html_list = glob(sys.argv[1]+'/*/outs/web_summary.html')

if not html_list:
    exit('No web summary files found!')

# create reports directory
os.makedirs('Reports', exist_ok=True)

for html in html_list:
    html_l = html.split('/')
    cp_name = f'Reports/{html_l[-3]}_{html_l[-1]}'
    print(f'Copying {html} to {cp_name}')
    shutil.copy(html,cp_name)
