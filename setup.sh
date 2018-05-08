#!/bin/bash

echo "Cloning fastText..."
git init
git remote add -t \* -f origin https://github.com/facebookresearch/fastText.git
git checkout master

echo "Init virtual env..."
virtualenv .

echo "Installing python dependencies..."
pip install NumPy SciPy pybind11 pandas
pip install .

echo "Downloading pre-trained english wiki model..."
curl -O https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.en.zip
unzip wiki.en.zip -d wikimodel