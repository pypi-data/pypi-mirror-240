# LoReMe pipeline

TODO:

- Document setting pore type/chemistry
- Tidy up rough edges in documentation (e.g. cli reference)
- Review handling of ONT bedMethyl format
- Find out why Modkit runs with only one thread
- Rust-ify postprocessing functions
- unit tests for postprocessing functions

LoReMe (Long Read Methylaton) is a Python package facilitating analysis of
DNA methylation signals from [Pacific Biosciences](https://www.pacb.com/technology/hifi-sequencing/)
or [Oxford Nanopore](https://nanoporetech.com/applications/dna-nanopore-sequencing)
long read sequencing data.

It consists of an API and CLI for three distinct applications:

1. Pacific Biosciences data processing. PB reads in SAM/BAM format are aligned
to a reference genome with the special-purpose aligner [pbmm2](https://github.com/PacificBiosciences/pbmm2>),
a modified version of [minimap2](https://lh3.github.io/minimap2/).
Methylation calls are then piled up from the aligned reads with [pb-CpG-tools](https://github.com/PacificBiosciences/pb-CpG-tools).

2. Oxford nanopore basecalling. ONT reads are optionally converted from FAST5
to [POD5](https://github.com/nanoporetech/pod5-file-format) format, then
basecalled and aligned to a reference with [dorado](https://github.com/nanoporetech/dorado>)
(dorado alignment also uses minimap2 under the hood), and finally piled up with
[modkit](https://github.com/nanoporetech/modkit).

3. Postprocessing and QC of methylation calls. Several functions are available
to generate diagnostic statistics and plots.

See also the [full documentation](https://salk-tm.gitlab.io/loreme/index.html).

Other tools of interest: [methylartist](https://github.com/adamewing/methylartist), [modbamtools](https://github.com/rrazaghi/modbamtools)  ([modbamtools docs](https://rrazaghi.github.io/modbamtools/)), [methplotlib](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7214038/)

## Installation

### In a Conda environment

The recommended way to install `loreme` is with a dedicated `conda` environment:

First create an environment including all dependencies:
```sh
conda create -n loreme -c conda-forge -c bioconda samtools pbmm2 \
  urllib3 pybedtools gff2bed seaborn pyfaidx psutil gputil tabulate \
  cython h5py iso8601 more-itertools tqdm
conda activate loreme
```

Then install with `pip`:
```sh
pip install loreme
```

You may also wish to install `nvtop` to monitor GPU usage:
```sh
conda install -c conda-forge nvtop
```

### With pip

```sh
pip install loreme
```


### Check installation

Check that the correct version was installed with `loreme --version`

### Uninstall

To uninstall loreme:

```sh
loreme clean
pip uninstall loreme
```

## Oxford Nanopore reads

### Download example dataset

Use `loreme download-ont-example` to download a *K. azureus* (zebra perch) genome assembly, gene annotations, and a POD5 file containing ONT reads.

> #### Note
> This example analysis involves downloading and processing a 26 GB POD5 file of nanopore reads, which will be time consuming and resource-intensive. For that reason, it is recommended to reproduce it on a remote server (such as Seabiscuit for members of the Michael Lab at Salk).

```
mkdir loreme_example_Kazu/
loreme download-ont-example -d loreme_example_Kazu/
```

Consider going for a coffee break with your colleagues, as this will take a few minutes. Once the download is complete, the example datasets will be present in the desintation directory.

```
cd loreme_example_Kazu/
ls
```
```
Kazu_090722.primary_high_confidence.gff3.gz
Kazu_090722.softmasked.fasta.gz
Kazu_090722_95etoh_22C_6w_SRE1_deep.pod5
```

### Download dorado

Calling methylation from ONT long reads requires the basecaller [dorado](https://github.com/nanoporetech/dorado) . Download it by running

```
loreme download-dorado <platform>
```

This will download dorado and several basecalling models. The platform should be one of: `linux-x64`, `linux-arm64`, `osx-arm64`, `win64`, whichever matches your system. Running `loreme download-dorado --help` will show a hint as to the correct choice.

> #### Note
> For members of [Michael Lab](https://michael.salk.edu/) at Salk running on Seabiscuit, use `loreme download-dorado linux-x64`.

### Modified basecalling

> #### Note
> If you have FAST5 data, convert it to POD5 using `loreme dorado-convert` (see `loreme dorado-convert --help`)

The POD5 file will need to be contained in its own directory on a scratch disk 
to be basecalled, so create a directory and move it there:

> #### Note
> Since basecalling ONT data is disk-read intensive, it will be slow on a spinning disk. The environment variable `$SCRATCH` should be set to a location on a fast SSD or NVMe disk for the following steps. For Michael lab members running on Seabiscuit, use this command: `SCRATCH=/scratch/<username>`.

```
mkdir $SCRATCH/Kazu_090722_pod5/
mv Kazu_090722_95etoh_22C_6w_SRE1_deep.pod5 $SCRATCH/Kazu_090722_pod5/
```

First check that a GPU is available to use:

```sh
loreme check-gpu
```

You can carry out modified basecalling (i.e. DNA methylation) with default parameters by running:

```
loreme dorado-basecall $SCRATCH/Kazu_090722_pod5/ $SCRATCH/Kazu_090722.bam
```

The input argument should be a directory containing one or more POD5 files. The output argument is a BAM file containing MM/ML tags. For other parameter options, see `loreme dorado-basecall --help`

> #### Note
> By default, LoReMe uses the "fast" basecalling model, which is less accurate. In practice you will probably want to use a higher accuracy model by setting the `--accuracy` option, e.g. `loreme dorado-basecall --accuracy sup $SCRATCH/Kazu_090722_pod5/ $SCRATCH/Kazu_090722.bam`

> #### Note
> While basecalling, tools like `htop` or `mutil` may show your memory usage increasing to hundreds of gigabytes. This is a bug in dorado and/or how Linux communicates with the GPU, and does not reflect actual memory usage.

To run dorado with only regular basecalling, use the `--no-mod` option:

```
loreme dorado-basecall --no-mod <pod5s/> <output.bam>
```

### Alignment
The BAM file produced by dorado can be aligned to a reference index (FASTA or MMI file) with `loreme dorado-align`:

```
loreme dorado-align Kazu_090722.softmasked.fasta.gz $SCRATCH/Kazu_090722.bam Kazu_090722_aligned.bam
```

### Download modkit

Piling up methylation calls from BAM data requires [modkit](https://github.com/nanoporetech/modkit) . Download it by running:

```
loreme download-modkit
```

### Check BAM file for MM/ML tags

Before processing with modkit, check that the BAM file contains MM/ML tags.

```sh
loreme check-tags Kazu_090722_aligned.bam
```

### Pileup

The pileup step generates a bedMethyl file from an aligned BAM file.

Before running modkit, you will need to decompress the FASTA file.
```
gunzip Kazu_090722.softmasked.fasta.gz
```

Then you can generate a pileup
```
loreme modkit-pileup Kazu_090722.softmasked.fasta Kazu_090722_aligned.bam Kazu_090722.bed
```
> #### Note
> See `loreme modkit-pileup --help` for additional options. On a HPC system you may want to use additional threads with the `-t` flag.

### Postprocessing

See also the [Pacific Biosciences reads](https://salk-tm.gitlab.io/loreme/pb_reads.html) section for examples of postprocessing analysis that can be applied to bedMethyl files.

**Calculate mean methylation level**

```
loreme mean --total Kazu_090722.bed
```

```
Group        Methylation level (%)
0    79.64114117704054
```

> #### Note
> This and subsequent steps represent postprocessing that can be applied to either Pacific Biosciences or Oxford Nanopore datasets.

**Methylation level of promoters**

To calculate methylation levels of promoter regions:

```sh
loreme promoter Kazu_090722.primary_high_confidence.gff3.gz \
  Kazu_090722.bed --hist Kazu_090722_promoter.svg > Kazu_090722_promoter.bed
head Kazu_090722_promoter.bed
```

```
ctg1	159758	161758	Kazu_090722.ctg1.g000010	86.36	-
ctg1	256072	258072	Kazu_090722.ctg1.g000030	64.29	+
ctg1	321679	323679	Kazu_090722.ctg1.g000050	76.79	-
ctg1	397819	399819	Kazu_090722.ctg1.g000060	45.23	+
ctg1	437295	439295	Kazu_090722.ctg1.g000070	100.00	+
ctg1	444908	446908	Kazu_090722.ctg1.g000080	59.09	-
ctg1	499196	501196	Kazu_090722.ctg1.g000100	97.64	-
ctg1	547954	549954	Kazu_090722.ctg1.g000110	100.00	+
ctg1	577225	579225	Kazu_090722.ctg1.g000120	77.38	-
ctg1	662637	664637	Kazu_090722.ctg1.g000130	100.00	-
```

Histogram of methylation levels of promoter regions:

![promoter methylation](docs/source/_static/Kazu_090722_hist_promoter.svg)

**Methylation level of gene bodies**

To calculate methylation levels of gene bodies:

```sh
loreme gene-body Kazu_090722.primary_high_confidence.gff3.gz \
  Kazu_090722.bed --hist Kazu_090722_gene_body.svg > Kazu_090722_gene_body.bed
head Kazu_090722_gene_body.bed
```

```
ctg1	159267	159758	Kazu_090722.ctg1.g000010	95.00	-
ctg1	237075	241223	Kazu_090722.ctg1.g000020	92.05	-
ctg1	258072	259127	Kazu_090722.ctg1.g000030	100.00	+
ctg1	320906	321679	Kazu_090722.ctg1.g000050	66.67	-
ctg1	399819	411211	Kazu_090722.ctg1.g000060	83.36	+
ctg1	439295	440181	Kazu_090722.ctg1.g000070	77.78	+
ctg1	444411	444908	Kazu_090722.ctg1.g000080	100.00	-
ctg1	456252	477732	Kazu_090722.ctg1.g000090	89.00	+
ctg1	498921	499196	Kazu_090722.ctg1.g000100	100.00	-
ctg1	549954	558103	Kazu_090722.ctg1.g000110	98.23	+
```

Histogram of methylation levels of gene bodies:

![gene body methylation](docs/source/_static/Kazu_090722_hist_gene_body.svg)

**Gene methylation profile**

To plot a profile of methylation across gene bodies:

```sh
loreme plot-genes Kazu_090722.primary_high_confidence.gff3.gz \
  Kazu_090722.bed Kazu_090722_genes.svg
```

Methylation profile across gene bodies:

![gene methylation profile](docs/source/_static/Kazu_090722_genes.svg)
