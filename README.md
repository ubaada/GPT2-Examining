# GPT2-Examining
Exploring gender bias in language modelling with GPT-2.


Use the split_data.py to split the dataset into test/training sets (80/20) from the brown corpus.
The generated files will be:
- split_80.txt
- split_20.txt

Use the cdo.py (Counterfactual Data Augmentation) script to produce the manipulated text file:
- cdo_80.txt

Retrain the GPT2 model on either split_80.txt or cdo_80.txt and compare.
