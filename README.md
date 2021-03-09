# Completeness-of-Metadata-Accompanying-Omics-Studies
##
### This analysis was performed to assess the completeness of metadata accompanying omics studies. Over the last decade there has been tremendous progress to improve the sharing of genomics data, which allows researchers to easily access the various types of data across a wide range of phenotypes. Some of the most well known public repositories are Gene Expression Omnibus, Sequence Read Archive and ArrayExpress. However, despite the availability of raw data, metadata accompanying the raw data is often unavailable. Incomplete and improperly annotated metadata on repositories proves to be a hindrance to reusing and reproducing existing data, especially for making novel discoveries. Leveraging previously published data for novel biological discoveries is only possible to its maximum extent if the metadata that accompanies raw omics data is complete and present in a standardized format.Through rhis analysis, we try to quantify the gap that exists between raw data and metadata, and suggests ways that transparent data sharing can be achieved.
##
### The preprint to the editorial is available on: https://osf.io/na5j8/
##
### There are four CSV files that support this analysis.
##
### "sepsis_clinical_phenotypes.csv" contains data regarding the number of times a particular clinical phenotype has been reported on each - the publication and the public repository. The total number of times the clinical phenotype was reported is a sum of the individual platforms. This is further expressed as a percentage. 
##
### "sepsis_comparison.csv" reports the number of clinical phenotypes that have been reported on each of the platforms for each of the cohorts. There were a total of nine clinical phenotypes that were considered. The total number of clinical phenotypes has been expressed as a percentage of the total (all nine clinical phenotypes being reported corresponds to 100%).
##
### "sepsis_completeness.csv" was used to observe which of the cohorts were most and least complete. The number of clinical phenotypes reported for each cohort on the publication and the public repository was counted, summed and the total was expressed as a percentage.
##
### "sepsis_individual_phenotypes.csv" contains data to calculate the most and least discrepancy between the individual phenotypes reported on both platforms.
##
### The results of the analysis are available in the editorial as well as below each corresponding figure on the Jupyter Notebook titled "sepsis_metadata_results.ipynb".
