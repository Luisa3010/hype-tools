This is a collection of tools for analyzing HYPe sequences.

## Installation


...

## Several Tools 
# Todo Replace with actual commands

### HVD detection

This tool splits HYPe reads into HVDs (Hypervariable Domains) and conserved domains from FASTA files by identifying the positions of the 
specified start and end markers. It can process either a single FASTA file or a directory of FASTA files. Per default, the tool will use the HVD markers from G. pallida HYP1 and process all the reads.


```bash
 hypetools extract-hvds "path/to/folder/or/fasta/file.fasta" --hvd-markers "path/to/hvd/markers.fasta" --start-index 2 --end-index 5
```


### Synthetic data generation

This tool is to generate synthetic HYPe sequences. You can use it to create a synthetic data set to mimick real observed reads.
The synthetic data set contains reads from different categories, the user can specify the number of sequences to generate for each category.

- real observed reads - sampled from real data, that can be provided by the user. Per default, the tool will use the real observed HYP1 reads from G. pallida.
- hybrid reads - created by combining two real observed HYP1 reads
- random motif-based reads - created by combining a random number of motifs. The motifs can be provided by the user. Per default, the tool will use the motifs from G. pallida. HYP1. Motifs should be provided in fasta format.
- block-based reads - created by combining a random number of motifs, but following the block arrangement of real observed HYP1 reads. To use this, the user needs to provide a file containing the motifs in a fasta format. The fasta headers should contain the position of the motif in the HYP block. This format looks like this (Not a real example):

>YERGGG1_pos1 
ATGAGAGAGA
>YERGGG2_pos1
ATGAGAGGGA
>SNRGGG1_pos2
ATGAGAGAGG
>RDRGD1_pos3 
ATGAGAG


The reads are created and then mutated, which means indels and SNPs are introduced.
The mutation rate is on a per base pair basis. The rate is sampled from a normal distribution to resemble the mutation rate of real observed HYP1 reads.

The synthetic data set also contains:
- severely mutated sequences - sequences with a higher mutation rate
- completely random sequences - created by randomly combining bases
These are created as "negative controls", reads that can not be ambigously parsed.

The length of the sequences are sampled from a normal distribution to resemble the length of real observed HYP1 reads.
For the block-based and random motif-based sequences, this length is obtained by using the length of unique real obsereved HYP reads

The user can provide files containing:
- real observed HYP1 reads
- motifs
- short secitons of conserved regions, tose will be flanking the HVDs


Additionaly, a file will be created containing information about the synthetic data set - what category the reads belong to, and the motifs used to create the reads, as well as the number of mutations in the reads. 


```bash
hype-tools synth --n-real 100 --n-hybrid 100 --n-severe 100 --n-random-motif 100 --n-block 100 --n-full-random 100 --real-input real.fasta --motifs motifs.json --output output.fasta
```

or

```bash
hype-tools synth --n 600 --real-input real.fasta --motifs motifs.json --output output.fasta
```


### HYPe Parsing

This tool processes FASTA files by first detecting Hypervariable Domains (HVDs) and then finding the motifs in the HVDs. The selection of possible motifs and borders need to be provided by the user. This tool will output a table for each read containing the most likely sequence of motifs on a dna and protein level, their positions in the read and the quality of the parsing. If two or more motifs fit equally well, the tool will output all of them for one position.

Quality measures: 
- Excluded bases: Percentage of the read that is covered by the motifs
- Per Motif Alignment Score: Normalized semiglobal alignment score of the motif in this position, 1 is a perfect match
- Per Motif Quality Score: Alignment score of the best matching motif in this position, divided by the alignment score of the second best matching motif in this position. The quality score is between 1 and 2, 1 means no certainty, both the best and the second best matching motifs align equally well, 2 is high certainty. 
- Per Read Alignment Score: Average alignment score of the motifs in the read


```bash
 hypetools replace-parser /path/to/folder/or/fasta/file.fasta --hvds-file /path/to/hvd/markers.fasta --motifs-file /path/to/motifs.json --start-index 3 --end-index 6 
```

The input can be a single fasta file or a directory containing multiple fasta files. 


### Report Generation

With this tool, the user will be able to generate a report about about a parser output. The report will contain information about the HVDs, the motifs, and the quality of the parsing.


### Simplify Parsed Reads 

With this tool, the user is be able to generate a compacted version of the parsed reads. The simplified version only contains the sequence header and the motifs, no quality information.


### Filter Parsed Reads

With this tool, the user is able to filter the parsed reads based on the quality of the parsing. The user can filter based on the minimum alignment score, the excluded percentage, the quality score and the minimum average score.







## Future Tools 

### De-Novo Motif Detection

With this tool, the user will be able to scan a fasta file containing HYPe reads for new, unknown motifs. 





## Example Data

Includes 
Synthetically generated G. pallida HYP1 data 
G. pallida HY1 HVD markers
G. pallida HYP1 Motifs
G. pallida HYP1 Germline Sequences

