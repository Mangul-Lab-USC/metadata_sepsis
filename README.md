# The completeness of metadata accompanying omics studies

[![Preprint Available](https://img.shields.io/badge/Preprint-online-green.svg)](https://osf.io/na5j8/)

This project contains the links to the datasets and the figures that were used for our study : ["Improving the completeness of public metadata accompanying omics studies"]

**Table of contents**
* [Datasets](#datasets)
  * [Archival stability](#archival-stability)
  * [Description of summary data](#description-of-summary-data)
* [Reproducing results](#reproducing-results)
* [Contact](#contact)


# Datasets

## Archival stability

We carefully examined a total of 3,125 samples across 29 studies. The original publications from journals were manually surveyed to gather information about the nine clinical phenotypes in question. The authors of these publications who own the data were contacted personally to obtain the complete data that was analyzed for that particular study. To extract metadata from the public repository, two Python scripts were used. These scripts are available [here](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/tree/main/scripts). The first script is used to get the files from the repository in the XML format. Further, the second script extracts the information from the XML file into a CSV file. These summary files from the repository as well as the data summarized from the original publication can be found [here](https://drive.google.com/drive/folders/1tnifubMuldAjFUlIKiLln1fLfojDMSMx?usp=sharing).

## Description of summary data

There are four CSV files that were used to produce the results of the analysis.

* [


# Reproducing results

We have prepared Jupyter Notebooks that utilize the data described above to visualize and reproduce the results presented in our editorial. 

* [Completeness of metadata results](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/notebooks/sepsis_metadata_results.ipynb)
