# Rename BGI Fastqs

If you have received fastq files from BGI sequencing in the following format `Cell Ranger count` may not be able locate them and this script renames the fastq files to a Illimina like format.

```bash
#example input file names
folder_1:
a_L1_1.fq.gz  a_L1_2.fq.gz  a_L1_3.fq.gz  a_L1_4.fq.gz

folder_2:
b_L1_1.fq.gz  b_L1_2.fq.gz  b_L1_3.fq.gz  b_L1_4.fq.gz
```

Run the script in the parent directory.

```bash
python3 rename_bgi_fq.py
```

```bash
#example output names
folder_1:
a_S1_L1_I1_001.fastq.gz  a_S1_L1_I2_001.fastq.gz  a_S1_L1_R1_001.fastq.gz  a_S1_L1_R2_001.fastq.gz
```