# fastText word embedding
This is simple python application based on [fastText](https://github.com/facebookresearch/fastText) fastText to generate word embeddings on your dataset.

## Getting Started
- Make sure that you have installed python and [virtualenv](https://virtualenv.pypa.io/en/stable/).
- just install dependencies:

```bash
$ bash setup.py
```

## NOTE
**python generateEmbeddings.py** must run in the **virtual environment**. just do:

```bash
$ source bin/activate
```

## Script help command

```bash
$ python generateEmbeddings.py -h

usage: generateEmbeddings.py [-h] -m M -f F -ic IC [IC ...] -oc OC [OC ...]
                             output

fastText embeddings generator.

positional arguments:
  output           A path to the output file

optional arguments:
  -h, --help       show this help message and exit
  -m M             Required a fastText trained model
  -f F             an input dataset
  -ic IC [IC ...]  input columns inside the dataset
  -oc OC [OC ...]  output columns in the output
  ```

## How to generate embeddings

```bash
python generateEmbeddings.py -m fasttext_trained_model_bin_file -f your_dataset_csv_file -ic columns_to_generate_embeddings -oc columns_in_the_output_embedding_file -- output_file
```

## Other fastText projects

- https://github.com/GINK03/fasttext-vs-word2vec-on-twitter-data
- https://github.com/vinzeebreak/fasttext-tuning
- https://github.com/Babylonpartners/fastText_multilingual
- https://github.com/chenyuntc/PyTorchText
- https://github.com/giacbrd/ShallowLearn
