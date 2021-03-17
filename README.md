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

* [sepsis_clinical_phenotypes.csv](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/data/sepsis_clinical_phenotypes.csv) contains data regarding the number of times a particular clinical phenotype has been reported on each - the publication and the public repository. The total number of times the clinical phenotype was reported is a sum of the individual platforms. This is further expressed as a percentage. 

* [sepsis_comparison.csv](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/data/sepsis_comparison.csv) reports the number of clinical phenotypes that have been reported on each of the platforms for each of the cohorts. There were a total of nine clinical phenotypes that were considered. The total number of clinical phenotypes has been expressed as a percentage of the total (all nine clinical phenotypes being reported corresponds to 100%).

* [sepsis_completeness.csv](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/data/sepsis_completeness.csv) was used to observe which of the cohorts were most and least complete. The number of clinical phenotypes reported for each cohort on the publication and the public repository was counted, summed and the total was expressed as a percentage.

* [sepsis_individual_phenonotypes](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/data/sepsis_individual_phenotypes.csv) contains data to calculate the most and least discrepancy between the individual phenotypes reported on both platforms.


# Reproducing results

We have prepared Jupyter Notebooks that utilize the data described above to visualize and reproduce the results presented in our editorial. 

* [Completeness of metadata results](https://github.com/Mangul-Lab-USC/Completeness-of-Metadata-Accompanying-Omics-Studies/blob/main/notebooks/sepsis_metadata_results.ipynb)


# Contact

Please do not hesitate to contact us (smangul@usc.edu, anushkar@usc.edu) if you have any comments, suggestions, or clarification requests regarding the study or if you would like to contribute to the extended analysis involving more disease conditions.
