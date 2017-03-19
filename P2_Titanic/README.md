# Titanic data analysis

This project's goal is to analyze available data about Titanic passengers to figure 
what factors were responsible for survival or death of passengers during the crash.

Project dependencies are listed in ``environment.yaml`` file.
You can create an environment with these dependencies by executing:
```
conda env create -f environment.yaml
```
To activate the environment use:
```
source activate P2_Titanic
```
To process the data execute:
```
python titanic.py
```
It will generate files in ``report`` directory that can be used 
to generate ``titanic-report.pdf`` file using LaTeX.
To generate final ``titanic-report.pdf`` run:
```
python generate-report.py
```
