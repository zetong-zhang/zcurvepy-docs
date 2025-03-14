# Commandline
In order to meet the needs of more users, especially those who are not good at Python, we also equipped ZCurvePy with a series of command line programs that are basically consistent with APIs and Web Server functionality. In some ways, command line programs are more powerful than API interfaces, such as convenient visual interfaces and easy-to-write setting files as JSON. 
## Contents
- [Z-curve Plotter](#z_curve_plotter)
- [Z-curve Encoder](#z_curve_encoder)
- [Z-curve Segmenter](#z_curve_segmenter)
## Z-curve Plotter <a id="z_curve_plotter"></a>
This is the executable command line version of ZCurvePlotter, which integrates sequence download, cropping, complementary sequence transformation, multi-curve visualization, and more.  

**Usage:**  
2D-mode :
```bash
zcurve-plotter [-h] [-f FASTA] [-g GENBANK] [-a ACCESSION] -s SETTINGS [-o OUTPUT]  [-p PNG] [-v SHOW]
```
3D-mode :
```bash
zcurve-plotter-3d [-h] [-f FASTA] [-g GENBANK] [-a ACCESSION] -s SETTINGS [-o OUTPUT]  [-p PNG] [-v SHOW]
```
**Args:**  
|Short Arg|Long Arg   |Discription                                               |Example             |
|:-------:|:----------|:---------------------------------------------------------|:-------------------|
|-h       |--help     |show this help message and exit                           |-h                  |
|-f       |--fasta    |input genome files as FASTA format (*.fa; *.fasta; *.fna) |-f genome.fa        |
|-g       |--genbank  |input genome files as GenBank format (*.gb; *.gbk; *.gbff)|-g genome.gb        |
|-a       |--accession|input as NCBI accession number (comma-splited; *.txt)     |-a NC_000854.2      |
|-s       |--settings |external setting file as JSON format (*.json)             |-s settings.json    |
|-o       |--output   |output data file of all curves as JSON (*.json)           |-o curves.json      |
|-p       |--png      |output graphic file as PNG picture (*.png)                |-p picture.png      |
|-v       |--show     |show graphic user interface or not (default: False)       |-v True             |

**JSON:**  
```json
{
    /* 
     * All of ZCurvePy's command line programs can share a single settings.json,
     * so the application should be specifed as "plotter" at first.
     */
    "plotter": [
        /* Specify parameters for each drawing task in turn through a list. */
        { // The first nucleic sequence to plot
            "start": 114514,
            "stop": 
        }
    ]
}
```

**Examples:**
## Z-curve Encoder <a id="z_curve_encoder"></a>