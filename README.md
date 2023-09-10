## Overview
<div style="text-align: center;">
  <img src="overview_CellDialog.png" alt="Alt Text">
</div>

## Data
Data is available at [uniprot](https://www.uniprot.org/), [GEO](https://www.ncbi.nlm.nih.gov/geo/).

## Package Environment
Install python3 for running this code. And these packages should be satisfied:
* tensorflow == 2.5.0
* keras == 2.7.0
* pandas == 1.1.4
* numpy == 1.19.5
* scikit-learn == 1.0.1
* matplotlib == 0.1.5
* xgboost == 1.6.2
* lightgbm == 3.3.0
* KTBoost == 0.2.2
* gpboost == 0.7.10


## Feature Acquisition
[iFeature](https://github.com/Superzchen/iFeature)

## CCC analysis tools
[cellphonedb](https://github.com/Teichlab/cellphonedb),
[NATMI](https://github.com/asrhou/NATMI),
[iTALK](https://github.com/Coolgenome/iTALK),
[CellChat](https://github.com/sqjin/CellChat)
## Usage
1. First, run the model, the default 5 fold cross-validation, get LRI pairs. Or the user can user-specified LRI database directly, skip this step to the second step.
```
python code/CellDialog.py

```
2. The second step, Run the three-point estimation method, including [(cell expression)(expression product)(expression thresholding)]. (Note: the user-specified database only needs to replace the LRI.csv file and the corresponding format in the file.)
- Ligand-Receptor Interactions ：The interaction data should be represented as a two-column table, with the **first column** containing **ligands** and the **second column** containing **receptors** (as in the following example). 

|Ligand|Receptor|
|-:|:-|
|LIGAND1|RECEPTOR1|
|LIGAND2|RECEPTOR2|
|LIGAND3|RECEPTOR2|
|LIGAND4|RECEPTOR3|
|LIGAND4|RECEPTOR4|
|...|...|...|

- scRNA-seq data ：Each column is a normalised gene/protein expression profile of a cell type or an individual cell. An example snapshot of the abundance matrix is shown below.

||cell_type1|cell_type2|cell_type3|...|
|-:|:-:|:-:|:-:|:-|
|**Gene1**|0.58|3.86|0.55|...|
|**Gene2**|1.23|6.2|8.52|...|
|**Gene3**|0|82.01|66.6|...|
|...|...|...|...|...|
```
python example/The three-point estimation method.py

```
3. Finally, output the strength of cell-cell communication.

## Hardware Environment
This code was run on a computer with the following specifications:
* CPU: AMD EPYC 7302
* Memory: 256GB DDR4
* GPU: GeForce RTX 2080 Ti

However, the minimal requirements for running this protocol are:
* CPU: Intel Core i7-11800H
* Memory: 16GB DDR4
* GPU: NVIDIA GeForce RTX 3050Ti
* Storage: At least 10GB available


