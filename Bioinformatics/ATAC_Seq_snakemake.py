#### ATAC-Seq Analysis Pipeline Testing Code
#### 04/08/19
#### Jiahao Huang

REP_INDEX = {"rep1", "rep2"}
INDEX_BT2 = ""
PICARD = ""



rule all:
    input:
        expand("bam/atac_seq_{rep}_bt2_hg38_sort.bam", rep=REP_INDEX),
        expand("bam/atac_seq_{rep}_bt2_hg38_sort_rmdup.bam", rep=REP_INDEX),
        expand("macs2_res/atac_seq_{rep}_peaks.narrowPeak", rep=REP_INDEX),

rule cutadapt:
    input:
        "raw_fastq/atac_seq_{rep}_R1.fq.gz"
        "raw_fastq/atac_seq_{rep}_R2.fq.gz"
    output:
        "fix_fastq/atac_seq_{rep}_R1.fq.gz"
        "fid_fastq/atac_seq_{rep}_R2.fq.gz"
    log:
        "fix_fastq/atac_seq_{rep}_cutadapt.log"
    shell:
        "cutadapt -j 4 --times 1 -e 0.1 -O 3 --quality-cutoff 25 \
        -m 50 -a AGATCGGAAGAGCACACGTCTGAACTCCAGTCAC \
        -A AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT \
        -o {output[0]} -p {output[1]} {input[0]} {input[1]} > {log} 2>&1"

rule bt2_mapping:
    input:
        "fix_fastq/atac_seq_{rep}_R1.fq.gz"
        "fid_fastq/atac_seq_{rep}_R2.fq.gz"
    output:
        "bam/atac_seq_{rep}_bt2_hg38.sam"
    log:
        "bam/atac_seq_{rep}_bt2_hg38.log"
    shell:
        "bowtie2 -x {INDEX_BT2} -p 4 -1 {input[0]} -2 {input[1]} -S {output} > {log} 2>&1"

rule bam_file_sort:
    input:
        "bam/atac_seq_{rep}_bt2_hg38.sam"
    output:
        "bam/atac_seq_{rep}_bt2_hg38_sort.bam"
    log:
        "bam/atac_seq_{rep}_bt2_hg38_sort.log"
    shell:
        "samtools sort -O BAM -o {output} -T {output}.temp -@ 4 -m 2G {input}"

rule remove_duplication:
    input:
        "bam/atac_seq_{rep}_bt2_hg38_sort.bam"
    output:
        "bam/atac_seq_{rep}_bt2_hg38_sort_rmdup.bam"
        "bam/atac_seq_{rep}_bt2_hg38_sort_rmdup.matrix"
    log:
        "bam/atac_seq_{rep}_bt2_hg38_sort_rmdup.log"
    shell:
        "java -Xms5g -Xmx5g -XX:ParallelGCThreads=4 \
        -jar {PICARD} MarkDuplicates \
        I={input} O={output[0]} M={output[1]} \
        ASO=coordinate REMOVE_DUPLICATES=true 2>{log}"

rule call_peak:
    input:
        "bam/atac_seq_{rep}_bt2_hg38_sort_rmdup.bam"
    output:
        "macs2_res/atac_seq_{rep}_peaks.narrowPeak"
    params:
        "atac_seq_{rep}",
        "macs2_res"
    log:
        "macs2_res/atac_seq_{rep}_peaks.log"
    shell:
        "macs2 callpeak -t {input} -f BAM -g hs --outdir {params[1]} -n {params[0]} -m 2 100 > {log} 2>&1"
