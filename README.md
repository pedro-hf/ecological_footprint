# Ecological Footprint analysis
The notebook ecological footprint presents a analysis of a Kaggle dataset:
https://www.kaggle.com/footprintnetwork/ecological-footprint with data from the footprint network organization.
I also takes additional data from:
* Human development index:http://hdr.undp.org/en/data
* Humal life indicator:http://www.iiasa.ac.at/web/home/research/researchPrograms/WorldPopulation/Reaging/HLI.html
* Country data:https://www.kaggle.com/fernandol/countries-of-the-world

The medium story https://medium.com/@pedro.hf86/the-uncomfortable-relation-between-ecological-footprint-and-human-development-401d24b69499 uses this analysis as base for discussion.

To run this notebook you will need:
* python 3.6.7
* pandas 0.23.4
* matplotlib 3.0.2
* numpy 1.15.4
* scikit-learn 0.20.2
* geopandas 0.4.0

## Motivation
A current topic of public discussion is ecological attitudes and policies, including conscious consumerism. I would like to back this with data and specifically, determine if current human economic development is the main reason behind our footprint.

## Content
* **ecological_footprint.ipynb**: Notebook containing the analysis
* **CSV files with data**: NFA 2018.csv, HDI.csv, Final_hli.csv, country_data_fixed.csv, countries of the worlds.csv
* **Pictures** used in blog post, result of the analysis.
* **help_function.py**: Help plotting functions used in the notebook.

## Notebook Content
1. **Business understanding: Ecological Footprint**
2. **Data understanding:**
    * 2.1 Ecological footprint
    * 2.2 Human development Index
    * 2.3 Human Life Index
    * 2.4 Country area data

3. **Data preparation:**
    * 3.1 Ecological footprint
    * 3.2 Human development Index
    * 3.3 Human Life Index
    * 3.4 Country area data

4. **Questions to our data:**
    * 4.1 Year in the world: a glipse of how the world looks like:
        * 4.1.1. Evaluation
        * 4.1.2
    * 4.2 HDI and GDP: are they behind ecological footprint?
        * 4.2.1. Modelling
        * 4.2.2. Evaluation
    * 4.3. Can we classify the countries based on their ecological footprint?
        * 4.3.1 Modelling
        * 4.3.2 Evaluation


## Conclusions

* We are currently consuming 70% more than what our world has the capacity to produce.
* Our development is closely tied to our ecological footprint
* Our ecological footprint behavior seems very much tied to our economic and human development.
