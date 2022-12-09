# Automated per-LS anomaly detection

This repository contains the code necessary to perform a per-LS automated anomaly detection via Autoencoders.

**Authors**: [Alkis Papanastassiou](mailto:alkis.papanastassiou@cern.ch), [Roberto Seidita](mailto:roberto.seidita@cern.ch)


---

<h2 align=center>Autoencoders in a nutshell</h2>

---

<p align=center>
  <a href=" ">
    <img src="./_.png" alt="Logo"/>
  </a>
</p>

---

## Directory structure

The directory is structured as follows:

```
.
├── utils
│   ├── __init__.py
│   ├── loaddataframe.py
│   ├── preprocessing.py
│   ├── threshold.py
│   └── training.py
└── scripts
    ├── lumisaver_mme.py
    └── lumisaver.py

```


## Datasets

All the datasets used in the experiment, except CER-E, are open and can be downloaded from this [link](https://mega.nz/folder/qwwG3Qba#c6qFTeT7apmZKKyEunCzSg). The CER-E dataset can be obtained free of charge for research purposes following the instructions at this [link](https://www.ucd.ie/issda/data/commissionforenergyregulationcer/). We recommend storing the downloaded datasets in a folder named `datasets` inside this directory.

## Utilities

The `utils` directory stores all the files necessary to load, preprocess and process data in histograms of certain monitor elements.

## Scripts

The scripts used for the experiment in the paper are in the `scripts` folder.

* `lumisaver_mme.py` is the main script, allowing multi-monitor element analysis. An example of usage is

	```
	python ./scripts/lumisaver_mme.py -a runs/run_315488.csv -b 0 -c runs/run360950.csv -d 1 -f 40 -g 750 -k 99.9
	```

* `lumisaver.py` is a simpler version of the script, allowing to test only on one monitor element, which is therefor required

	```
	python ./scripts/lumisaver_mme.py -a runs/run_315488.csv -b 0 -c runs/run360950.csv -d 1 -e METSig -f 40 -g 750 -k 99.9
	```


## Requirements
