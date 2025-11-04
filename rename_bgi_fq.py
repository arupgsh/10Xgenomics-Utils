from glob import glob
import os

'''
Renames the BGI sequencing files to an Illumina-like format for Cell Ranger count.
Warning: Renames all files with an fq extension in the current directory.
Usage: python3 rename_bgi_fq.py
'''

#list all fq.gz files
fq_l = glob("*/*.fq.gz")

#rename the fq files
for fq in fq_l:
    fq = fq.rstrip(".fq.gz")
    fq_d = fq.split('/')[0]
    fq_f = fq.split('/')[1].split('_')

    if int(fq_f[2]) < 3:
        fq_n = f'{fq_f[0]}_S{fq_f[0]}_{fq_f[1]}_R{fq_f[2]}_001'
    else:
        fq_n = f'{fq_f[0]}_S{fq_f[0]}_{fq_f[1]}_I{int(fq_f[2])-2}_001'

    fq_p = f'{fq_d}/{fq_n}.fastq.gz'
    fqp_old = fq+'.fq.gz'
    print(f'Renaming: {fqp_old} -> {fq_p}')
    os.rename(fqp_old,fq_p)
