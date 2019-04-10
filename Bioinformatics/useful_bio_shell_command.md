# Useful Bioinformatics One Liners
<hr>

## Source
* [The Williams lab @ Cornell University](http://williamslab.bscb.cornell.edu/?page_id=235 http://williamslab.bscb.cornell.edu/?page_id=287)
* [Stephen Turner's Github](https://github.com/stephenturner/oneliners)
* [Ming Tang's Github](https://github.com/crazyhottommy/bioinformatics-one-liners)
* [Zhigang Lu's Blog](https://zhiganglu.com/post/one-liners-collection/)
* [竹子-博客](http://www.cnblogs.com/peida/tag/%E6%AF%8F%E6%97%A5%E4%B8%80linux%E5%91%BD%E4%BB%A4/)

## Basic awk
Calculate Sum of column 1
```bash
awk '{sum+=$1} END {print sum}' file_name
```

Calculate Average of column 1
```bash
awk '{sum+=$1}END{print sum/NR}' file_name
```
<br>

## Basic sed
Trim leading and tailing white space
```bash
sed 's/^[ \t]*//;s/[ \t]*$//' file_name
```

Delete blank line
```bash
sed '/^$/d' file_name
```

Delete everything after target
```bash
sed -n '/target/,$!p' file_name
```

Delete everything before target
```bash
sed -n '/target/,$p' file_name
```

## Basic Tar
Create tar, gzip tar, bz2 Tar
```bash
tar -cvf tar_name.tar file_name
tar -zcvf tar_name.tar.gz file_name
tar -jcvf tar_name.tar.bz2 file_name
```

Extract
```bash
tar -xvf tar_name.tar file_name
tar -zxvf tar_name.tar.gz file_name
tar -jxvf tar_name.tar.bz2 file_name
```

List
```bash
tar -tvf tar_name.tar
tar -ztvf tar_name.tar.gz
tar -jtvf tar_name.tar.bz2
```
<br>

## Format related
Convert bam to fastq
```bash
samtools view file.bam | awk 'BEGIN {FS="\t"} {print "@" $1 "\n" $10 "\n+\n" $11}' > file.fq
```

Convert fastq to fasta
```bash
sed -n '1~4s/^@/>/p;2~4p' file.fq > file.fa
seqtk seq -a in.fq.gz > out.fa
```

Convert vcf to bed
```bash
sed -e 's/chr//' file.vcf | awk '{OFS="\t"; if (!/^#/){print $1,$2-1,$2,$4"/"$5,"+"}}' > file.bed
```
<br>

## Seqtk
Reverse complement of fasta/q
```bash
seqtk seq -r in.fq > out.fq
```

Extract sequences with names in file name.lst, one sequence name per line
```bash
seqtk subseq in.fq name.lst > out.fq
```

Extract sequences in regions contained in file reg.bed
```bash
seqtk subseq in.fa reg.bed > out.fa
```

Convert fastq to fasta
```bash
seqtk seq -a in.fq.gz > out.fa
```
<br>

## Quick Alias
Show the PATH
```bash
alias path='echo -e ${PATH//:/\\n}'
```

CDs
```bash
alias ..='cd ..'
alias ...='cd ../../'
alias ....='cd ../../../'
alias .....='cd ../../../../'
alias ......='cd ../../../../../'
alias u="cd ..;ls"
```

Ask before execute
```bash
alias mv="mv -i"
alias cp="cp -i"
alias rm="rm -i"
```

Extract function as suggested by Mendel Cooper in "Advanced Bash Scripting Guide"
```bash
extract () {
   if [ -f $1 ] ; then
       case $1 in
        *.tar.bz2)      tar xvjf $1 ;;
        *.tar.gz)       tar xvzf $1 ;;
        *.tar.xz)       tar Jxvf $1 ;;
        *.bz2)          bunzip2 $1 ;;
        *.rar)          unrar x $1 ;;
        *.gz)           gunzip $1 ;;
        *.tar)          tar xvf $1 ;;
        *.tbz2)         tar xvjf $1 ;;
        *.tgz)          tar xvzf $1 ;;
        *.zip)          unzip $1 ;;
        *.Z)            uncompress $1 ;;
        *.7z)           7z x $1 ;;
        *)              echo "don't know how to extract '$1'..." ;;
       esac
   else
       echo "'$1' is not a valid file!"
   fi
}
```

mkdir then cd
```bash
function mcd { mkdir -p "$1" && cd "$1";}
```

Refresh/Edit .bashrc/.bash_profile
```bash
alias refresh="source ~/.bashrc"
alias eb="vi ~/.bashrc"


alias refresh="source ~/.bash_profile"
alias eb="vi ~/.bash_profile"
```

Clear
```bash
alias c="clear"
```

Count seq number for FASTA
```bash
alias countfa="grep -c '^>'"
```

Count seq number for FASTQ
```bash
alias countfq="bioawk -cfastx 'END{print NR}'"
```
<br>
