# Python API
We listed a table here corresponding to that in the **Introduction** to better help readers sort out the logical relationship between the various curve-related apis:  
|Cumulative Curve     |Profile Curve       |Segmentation Method |Order Index S(P)*  |
|:--------------------|:-------------------|:-------------------|:------------------|
|z_curve              |**\*\***            |genome_dS_curve     |genome_order_index |
|RY_disparity         |x_prime_curve       |RY_dS_curve         |RY_order_index     |
|MK_disparity         |y_prime_curve       |MK_dS_curve         |MK_order_index     |
|WS_disparity         |z_prime_curve       |WS_dS_curve         |WS_order_index     |
|AT_disparity         |AT_prime_curve      |AT_dS_curve         |AT_order_index     |
|GC_disparity         |GC_prime_curve      |GC_dS_curve         |GC_order_index     |
|**\*\*\***           |CpG_prime_curve     |CpG_dS_curve        |CpG_order_index    |

**\*** &nbsp;&nbsp;&nbsp; The order index was treated as a feature of the sequence for machine learning in earlier studies, so it is integrated under the ZCurveEncoder. The other apis are integrated under ZCurvePlotter.  
**\*\*** &nbsp;&nbsp;&nbsp;Z-profile curves in 3D form are generally not used for visualization, but their parameters are used for gene starting point prediction, so we only provide it in "profile" mode of BatchZCurvePlotter to batch the dataset. You can use bulk interfaces (x_prime_curve, y_prime_curve, z_prime_curve) to implement it in 3D form as well.  
**\*\*\*** &nbsp;The geometry of the CpG-disparity curve is not obvious, so we do not provide a standard API. Readers may implement and explore its features on their own.

## Package Structure
- [ZCurvePy](#ZCurvePy)  
    - <details>
        <summary><a href="#ZCurvePlotter">ZCurvePlotter</a></summary>
        <ul>
          <li><a href="#ZCurvePlotter__init__">__init__</a></li>
          <li><a href="#ZCurvePlotter_z_curve">z_curve</a></li>
          <li><a href="#ZCurvePlotter_RY_disparity">RY_disparity</a></li>
          <li><a href="#ZCurvePlotter_MK_disparity">MK_disparity</a></li>
          <li><a href="#ZCurvePlotter_WS_disparity">WS_disparity</a></li>
          <li><a href="#ZCurvePlotter_AT_disparity">AT_disparity</a></li>
          <li><a href="#ZCurvePlotter_GC_disparity">GC_disparity</a></li>
          <li><a href="#ZCurvePlotter_x_prime_curve">x_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_y_prime_curve">y_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_z_prime_curve">z_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_AT_prime_curve">AT_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_GC_prime_curve">GC_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_CpG_prime_curve">CpG_prime_curve</a></li>
          <li><a href="#ZCurvePlotter_genome_dS_curve">genome_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_RY_dS_curve">RY_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_MK_dS_curve">MK_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_WS_dS_curve">WS_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_AT_dS_curve">AT_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_GC_dS_curve">GC_dS_curve</a></li>
          <li><a href="#ZCurvePlotter_CpG_dS_curve">CpG_dS_curve</a></li>
        </ul>
      </details>
    - <details>
        <summary><a href="#BatchZCurvePlotter">BatchZCurvePlotter</a></summary>
        <ul>
          <li><a href="#BatchZCurvePlotter__init__">__init__</a></li>
          <li><a href="#BatchZCurvePlotter__call__">__call__</a></li>
        </ul>
      </details>
    - <details>
        <summary><a href="#ZCurveEncoder">ZCurveEncoder</a></summary>
        <ul>
          <li>__init__</li>
          <li>genome_order_index</li>
          <li>RY_order_index</li>
          <li>MK_order_index</li>
          <li>WS_order_index</li>
          <li>AT_order_index</li>
          <li>GC_order_index</li>
          <li>mononucl_transform</li>
          <li>dinucl_transform</li>
          <li>trinucl_transform</li>
          <li>mononucl_phase_transform</li>
          <li>dinucl_phase_transform</li>
          <li>trinucl_phase_transform</li>
          <li>k_nucl_phase_transform</li>
        </ul>
      </details>
    - <details>
        <summary><a href="#BatchZCurveEncoder">BatchZCurveEncoder</a></summary>
        <ul>
          <li>__init__</li>
          <li>__call__</li>
          <li>dump</li>
        </ul>
      </details>
    - <details>
        <summary><a href="#ZCurveSegmenter">ZCurveSegmenter</a></summary>
        <ul>
          <li>__init__</li>
          <li>run</li>
          <li>reset</li>
        </ul>
      </details>
    - <details>
        <summary><a href="#ZCurveBuilder">ZCurveBuilder</a></summary>
        <ul>
          <li>__init__</li>
          <li>fit</li>
          <li>predict</li>
        </ul>
      </details>
    - [decode](#Decode)
    - [shuffle](#shuffle)
- _ZCurvePy
- ZCurvePy.RunnableScriptsUtil
  - extract_CDS
  - download_acc

## ZCurvePy
This is the Python package `__init__` module of released ZCurvePy package. All the C/C++ apis can be called through this module. If you don't want to import additional third-party modules (e.g. modules from scikit-learn) or APIs written in pure Python provided by ZCurvePy (e.g. [ZCurveBuilder](#ZCurveBuilder)), use `import _ZCurvePy` instead of `import ZCurvePy`.

### ZCurvePlotter
A simple API for plotting a nucleotide sequence to Z-curve or do segmentation based on order index. Multi-thread is not supported by this API. If you want to plot Z-curve for a large dataset using multi-thread, use [BatchZCurvePlotter](#BatchZCurvePlotter) instead. This API only returns coordinate information and provides no graphical operations. If you want visual curves, use commandline tools or program it by yourself using visualization library like [Matplotlib](https://matplotlib.org/) and [Plotly](https://plotly.com/python/).

#### `ZCurvePlotter.__init__` 
`__init__` method  of _ZCurvePy.ZCurvePlotter  
**Args:**  
- seq_or_record:   
Object that stores information of nucleic sequence. str, Bio.Seq.Seq, Bio.SeqRecord.SeqRecord and many other types are supported.

**Returns:**
- plotter (object):  
  _ZCurvePy.ZCurvePlotter

#### `ZCurvePlotter.z_curve` <a id="ZCurvePlotter_z_curve"></a>
Convert a DNA sequence or RNA sequence to Z-curve.  

**Background**  
Z-curve theory is a geometrical approach to genome analysis. The Z-curve is a three-dimensional curve that represents a DNA sequence in the sense that each can be uniquely reconstructed
given the other.The Z-curve, therefore, contains all the information that the corresponding DNA sequence carries.

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$x_n = (A_n + G_n) - (C_n + T_n)$  
$y_n = (A_n + C_n) - (G_n + T_n), n=1,2,3 ...,N$  
$z_n = (A_n + T_n) - (G_n + C_n)$  

The $x_n$, $y_n$, $z_n$ can be drawn in a three-dimensional rectangular coordinate system, or take the length of the sequence as the horizontal axis and be drawn in three plane coordinate systems.
In this process, both global and local features of the sequence are well visualized.

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization; Replication origins prediction; Machine learning  

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
x, y, z = plotter.z_curve(window=10000, return_n=False)
# n, x, y, z = plotter.z_curve(window=10000)

fig = plt.figure(figsize=(10, 10))
ax3d = fig.add_subplot(projection='3d')
ax3d.plot(x, y, z)
ax3d.set_xlabel("X", labelpad=10)
ax3d.set_ylabel("Y", labelpad=10)
ax3d.set_zlabel("Z", labelpad=10)
plt.show()
```
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - x (list):  
  The x values of the Z-curve.
  - y (list):  
  The y values of the Z-curve.
  - z (list):  
  The z values of the Z-curve

![Z-curve of Escherichia coli](./images/e_coli_z_curve.jpg)

#### `ZCurvePlotter.RY_disparity` <a id="ZCurvePlotter_RY_disparity"></a>
Returns the x values of the Z-curve (RY-disparity).

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$x_n = (A_n + G_n) - (C_n + T_n), n=1,2,3 ...,N$  

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization; Replication origins prediction; Machine learning

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, x = plotter.RY_disparity(window=100)
# x = plotter.RY_disparity(window=100, return_n=False)
plt.plot(n, x)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel('RY Disparity', labelpad=10)
plt.show()
```
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - x (list):  
  The x values of the Z-curve.

![Disparity curves of Escherichia coli](./images/e_coli_disparity.png)
#### `ZCurvePlotter.MK_disparity` <a id="ZCurvePlotter_MK_disparity"></a>
Returns the y values of the Z-curve (MK-disparity).

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$y_n = (A_n + C_n) - (G_n + T_n), n=1,2,3 ...,N$  

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization; Replication origins prediction; Machine learning

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, y = plotter.MK_disparity(window=100)
# y = plotter.MK_disparity(window=100, return_n=False)
plt.plot(n, y)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel('MK Disparity', labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.RY_disparity*  
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - y (list):  
  The y values axis of the Z-curve.

#### `ZCurvePlotter.WS_disparity` <a id="ZCurvePlotter_WS_disparity"></a>
Returns the z values of the Z-curve (WS-disparity).

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$z_n = (A_n + T_n) - (G_n + C_n), n=1,2,3 ...,N$  

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization; Replication origins prediction; Machine learning

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, z = plotter.WS_disparity(window=100)
# z = plotter.WS_disparity(window=100, return_n=False)
plt.plot(n, z)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel('WS Disparity', labelpad=10)
plt.show()
```
*The local geometry of WS-display is not significant in the vast majority of species. (due to stable GC content)*  
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - z (list):  
  The z values axis of the Z-curve.

#### `ZCurvePlotter.AT_disparity` <a id="ZCurvePlotter_AT_disparity"></a>
Returns AT-disparity (equivalent to AT-skew in some cases).

**Definition**  
Let $A_n$ and $T_n$ be the count of A and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$d_{\rm AT}(n) = A_n - T_n, n=1,2,3 ...,N$  

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, d = plotter.AT_disparity(window=100)
# d = plotter.AT_disparity(window=100, return_n=False)
plt.plot(n, d)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel('AT Disparity', labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.RY_disparity*  
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - d (list):  
  The AT-disparity values.

#### `ZCurvePlotter.GC_disparity` <a id="ZCurvePlotter_GC_disparity"></a>

Returns GC-disparity (equivalent to GC-skew in some cases).

**Definition**  
Let $G_n$ and $C_n$ be the count of A and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$d_{\rm GC}(n) = G_n - C_n, n=1,2,3 ...,N$  

This curve could be smoothed using mean-smoothing method.

**Application Scene**  
Genome visualization

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, f = plotter.GC_disparity(window=100)
# f = plotter.GC_disparity(window=100, return_n=False)
plt.plot(n, f)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel('GC Disparity', labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.RY_disparity*  
**Args:**  
  - window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
  - return_n (bool):  
  Return the sequence length axis or not. (Default: True)

**Returns:**  
  - n (list):  
  The sequence length axis.
  - f (list):  
  The GC-disparity values.

#### `ZCurvePlotter.x_prime_curve` <a id="ZCurvePlotter_x_prime_curve"></a>

Calculate x' values and the slope k.

**Background**  
The different patterns of the species-specific, conserved nucleotide distribution are helpful to extract some recognition variables to identify gene starts. In prokaryotic genomes, a major jump in xn occurs in the region of −14 to −7 for the true start codons, but not for the non-coding ORFs. It is likely caused by purine-rich SD sequence.Therefore the features of mononucleotide frequencies near the true start codons are notably different from those of the upstream and downstream false starts.

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$x_n = (A_n + G_n) - (C_n + T_n), n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$x'_n = x_n - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization; Gene start sites prediction

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, xp, k = plotter.x_prime_curve(window=100)
# xp, k = plotter.x_prime_curve(window=100, return_n=False)
plt.plot(n, xp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("x'", labelpad=10)
plt.show()
```

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- xp (list):  
  The x' values.
- k (float):  
  The slope value 'k'.

![L lactis Gene Start](./images/l_lactis_gene_start.png)  
#### `ZCurvePlotter.y_prime_curve` <a id="ZCurvePlotter_y_prime_curve"></a>

Calculate y' values and the slope 'k'.

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$y_n = (A_n + C_n) - (G_n + T_n), n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$y'_n = y_n - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization; Gene start sites prediction

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, yp, k = plotter.y_prime_curve(window=100)
# yp, k = plotter.y_prime_curve(window=100, return_n=False)
plt.plot(n, yp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("y'", labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.x_prime_curve*  

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- yp (list):  
  The y' values.
- k (float):  
  The slope value 'k'.

#### `ZCurvePlotter.z_prime_curve` <a id="ZCurvePlotter_z_prime_curve"></a>

Calculate z' values and the slope 'k'.

**Background**  
The GC profile is a windowless technique to calculate the G+C content of genomic DNA sequences as well as visualize isolate structures, which is rich of G+C. By this method, the G content can be calculated at different 'resolution'.In an extreme case, the G content may be computed at a specific point, rather than in a window of finite size. This is particularly useful to analyze the fine variation of base composition along genomic sequences.

**Definition**  
Let $A_n$, $G_n$, $C_n$ and $T_n$ be the count of A, G, C and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$z_n = (A_n + T_n) - (G_n + C_n), n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$z'_n = z_n - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization; Gene start sites prediction

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, zp, k = plotter.z_prime_curve(window=100)
# zp, k = plotter.z_prime_curve(window=100, return_n=False)
plt.plot(n, zp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("z'", labelpad=10)
plt.show()
```

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- zp (list):  
  The z' values.
- k (float):  
  The slope value 'k'.  

![z' curve of human chr15](./images/human_zp.png)
#### `ZCurvePlotter.AT_prime_curve` <a id="ZCurvePlotter_AT_prime_curve"></a>

Calculate d'AT values for AT-disparity.

**Definition**  
Let $A_n$ and $T_n$ be the count of A and T of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$d_{\rm AT}(n) = A_n - T_n, n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$d'_{\rm AT}(n) = d_{\rm AT}(n) - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, dp, k = plotter.AT_prime_curve(window=100)
# dp, k = plotter.AT_prime_curve(window=100, return_n=False)
plt.plot(n, dp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("d'AT", labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.x_prime_curve*  

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- dp (list):  
  The d'AT values.
- k (float):  
  The slope value 'k'.

#### `ZCurvePlotter.GC_prime_curve` <a id="ZCurvePlotter_GC_prime_curve"></a>

Calculate d'GC values for GC-disparity.

**Definition**  
Let $G_n$ and $C_n$ be the count of G and C of a subsequence consisting of the first n nucleotides of a DNA, s.t.

$d_{\rm GC}(n) = G_n - C_n, n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$d'_{\rm GC}(n) = d_{\rm GC}(n) - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, fp, k = plotter.GC_prime_curve(window=100)
# fp, k = plotter.GC_prime_curve(window=100, return_n=False)
plt.plot(n, fp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("d'GC", labelpad=10)
plt.show()
```
*For the visual displaying example, please see ZCurvePlotter.x_prime_curve*  

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- fp (list):  
  The d'GC values.
- k (float):  
  The slope value 'k'.

#### `ZCurvePlotter.CpG_prime_curve` <a id="ZCurvePlotter_CpG_prime_curve"></a>

Calculate z' values for CpG-profile.

**Definition**  
Let $CpG_n$ be the count of CpG dinucleotide units in a DNA sequence, s.t.

$z_n = 2CpG_n - n, n=1,2,3 ...,N$

apply a linear fit to the curve based on least square method, then a slope 'k' is obtained, s.t.

$z'_n = z_n - kn, n=1,2,3 ...,N$

**Application Scene**  
Genome visualization

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, zp, k = plotter.CpG_prime_curve(window=100)
# zp, k = plotter.CpG_prime_curve(window=100, return_n=False)
plt.plot(n, zp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("CpG-profile", labelpad=10)
plt.show()
```  
*For the visual displaying example, please see ZCurvePlotter.z_prime_curve*  
**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  

**Returns:**  
- n (list):  
  The sequence length axis.
- zp (list):  
  The CpG-profile values.
- k (float):  
  The slope value 'k'.  

![CpG profile of human chr15](./images/human_cpg_island.png)
#### `ZCurvePlotter.genome_dS_curve` <a id="ZCurvePlotter_genome_dS_curve"></a>
Return dS(P) curve and its max point and max value. Segmentation algorithm for DNA sequences.  

**Background**  
Based on the quadratic divergence,the segmentation algorithm to partition a given genome or DNA sequence into compositionally distinct domains is put forward. The algorithm has been applied to segment human chromosome sequences, and the boundaries of isochores for each chromosome were obtained. Compared with the results obtained by using the entropic segmentation algorithm based on the Jensen-Shannon divergence, both algorithms resulted in all identical coordinates of segmentation points. An explanation of the equivalence of the two segmentation algorithms is presented. The new algorithm has a number of advantages. Particularly, it is much simpler and faster than the entropy-based method. Therefore, the new algorithm is more suitable for analyzing long genome sequences, such as human and other newly sequenced eukaryotic genome sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = a_n^2 + t_n^2 + c_n^2 + g_n^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.genome_dS_curve(window=10)
# sp, mp, mv = plotter.genome_dS_curve(return_n=False)
# mp, mv = plotter.genome_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).  

![Segmentation of Z-curve](./images/e_coli_segment.png)
#### `ZCurvePlotter.RY_dS_curve` <a id="ZCurvePlotter_RY_dS_curve"></a>
Return dS(P) curve for RY disparity and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = (a_n + g_n)^2 + (c_n + t_n)^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.RY_dS_curve(window=10)
# sp, mp, mv = plotter.RY_dS_curve(return_n=False)
# mp, mv = plotter.RY_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).

![RY profile of human mtDNA](./images/human_mt_xp.png)
#### `ZCurvePlotter.MK_dS_curve` <a id="ZCurvePlotter_MK_dS_curve"></a>
Return dS(P) curve for MK disparity and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = (a_n + c_n)^2 + (g_n + t_n)^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.MK_dS_curve(window=10)
# sp, mp, mv = plotter.MK_dS_curve(return_n=False)
# mp, mv = plotter.MK_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```  
*The segmented pattern of bacteria MK disparity is the same as Z-curve, see ZCurvePlotter.genome_order_index*  
**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).

#### `ZCurvePlotter.WS_dS_curve` <a id="ZCurvePlotter_WS_dS_curve"></a>
Return dS(P) curve for WS disparity and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = (a_n + t_n)^2 + (c_n + g_n)^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.WS_dS_curve(window=10)
# sp, mp, mv = plotter.WS_dS_curve(return_n=False)
# mp, mv = plotter.WS_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```

**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).
**
#### `ZCurvePlotter.AT_dS_curve` <a id="ZCurvePlotter_AT_dS_curve"></a>
Return dS(P) curve for AT disparity and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = a_n^2 + t_n^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.AT_dS_curve(window=10)
# sp, mp, mv = plotter.AT_dS_curve(return_n=False)
# mp, mv = plotter.AT_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```  
*The geometric characteristics of the curves AT disparity are not significant.*  
**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).

#### `ZCurvePlotter.GC_dS_curve` <a id="ZCurvePlotter_GC_dS_curve"></a>
Return dS(P) curve for GC disparity and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $a_n$, $g_n$, $c_n$ and $t_n$ be the frequency of A, G, C, T of a subsequence consisting of the first n nucleotides of a DNA, such that  

$S_n({\rm P}) = g_n^2 + c_n^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.GC_dS_curve(window=10)
# sp, mp, mv = plotter.GC_dS_curve(return_n=False)
# mp, mv = plotter.GC_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```
*The segmented pattern of bacteria GC disparity is the same as RY disparity, see ZCurvePlotter.RY_dS_curve*  
**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).

#### `ZCurvePlotter.CpG_dS_curve` <a id="ZCurvePlotter_CpG_dS_curve"></a>
Return dS(P) curve for CpG-profile and its max point and max value. Segmentation algorithm for DNA sequences.

**Definition**  
Let $p_n({\rm CpG})$ be the frequency of CpG dinucleotide units in a DNA sequence, such that the CpG order index could be defined as:

$S_n({\rm P}) = [p_n({\rm CpG})]^2 + [1 - p_n({\rm CpG})]^2, n=1,2,3...,N$

and denote that of the rest of the sequence by $S({\rm Q})$, such that we have

$dS_n({\rm P}) = S_n({\rm P}) + S_n({\rm Q}) - S({\rm P + Q}), n=1,2,3...,N$

the max point of the $dS_n({\rm P})$ is the segment point in a round of the recursive algorithm.

$n_{\rm seg} = {\rm argmax}\{dS_n({\rm P})\}$

**Application Scene**  
Genome segmentation

**Usage Example**
```python
from Bio import SeqIO
from ZCurvePy import ZCurvePlotter
import matplotlib.pyplot as plt

record = SeqIO.read("e_coli.fa", "fasta")
plotter = ZCurvePlotter(record)
n, sp, mp, mv = plotter.CpG_dS_curve(window=10)
# sp, mp, mv = plotter.CpG_dS_curve(return_n=False)
# mp, mv = plotter.CpG_dS_curve(only_m=True)
plt.plot(n, sp)
plt.axvline(n, mp)
plt.xlabel('n (bp)', labelpad=10)
plt.ylabel("dS(P)", labelpad=10)
plt.show()
```
*For visual presentation of segmented points, see ZCurvePlotter.CpG_prime_curve*  
**Args:**  
- window (int):  
  Window size used by mean-smoothing method. If a value <= 0 is given, do nothing and return the original curve data. (Default: 0)
- return_n (bool):  
  return the sequence length axis or not. (Default: True)  
- only_m (bool):  
  only return max point and max value.

**Returns:**  
- n (list):  
  The sequence length axis.
- sp (list):  
  The S(P) values axis.
- mp (float):  
  The max point of S(P).
- mv (float):  
  The max value of S(P).

### BatchZCurvePlotter <a id="BatchZCurvePlotter"></a>
### ZCurveEncoder <a id="ZCurveEncoder"></a>
### BatchZCurveEncoder <a id="BatchZCurveEncoder"></a>
### ZCurveSegmenter <a id="ZCurveSegmenter"></a>
### ZCurveBuilder <a id="ZCurveBuilder"></a>
### decode <a id="Decode"></a>
### shuffle <a id="Shuffle"></a>

## Third-party API
We list all of the third party APIs we call here and won't go into them below.  
|API                |Description                                                      |Python Package|
|:-----------------:|:----------------------------------------------------------------|:------------:|
|`Bio.Seq`          |Provide objects to represent biological sequences with alphabets.|Biopython     |
|`Bio.SeqRecord`    |Represent a Sequence Record, a sequence with annotation.         |Biopython     |
|`Bio.SeqIO`        |The standard Sequence Input/Output interface.                    |Biopython     |
|`Bio.SeqUtils`     |Miscellaneous functions for dealing with sequences.              |Biopython     |
|`matplotlib.pyplot`|State-based interface to matplotlib.                             |Matplotlib    |
