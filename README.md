# Automated per-LS anomaly detection tool

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



## Utilities

The `utils` directory stores all the files necessary to load, preprocess and process data in histograms of certain monitor elements.

## Scripts

The scripts used for the anomaly detection of time-series of histograms are in the `scripts` folder.

* `lumisaver_mme.py` is the main script, allowing multi-monitor element analysis. An example of usage is

	```
	python ./scripts/lumisaver_mme.py -a run_315488.csv -b 0  -c run_315488.csv -d 0 -f 40 -g 750 -k 99.99
	```

* `lumisaver.py` is a simpler version of the script, allowing to test only on one monitor element, which is therefore required

	```
	python ./scripts/lumisaver.py -a run_315488.csv -b 0  -c run_315488.csv -d 0 -e METSig -f 40 -g 750
	```


## Requirements
