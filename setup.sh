#!/bin/bash

# clone fastText
git init
git remote add -t \* -f origin https://github.com/facebookresearch/fastText.git
git checkout master

# init virtual env
virtualenv .

# install dependencies
pip install NumPy SciPy pybind11 pandas
pip install .

# download model files
curl -O https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.en.zip
unzip wiki.en.zip -d wikimodel