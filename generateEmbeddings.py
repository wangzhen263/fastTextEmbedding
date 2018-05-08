import pandas as pd
import fastText
import argparse

parser = argparse.ArgumentParser(description='fastText embeddings generator.')
parser.add_argument('output', help='A path to the output file')
parser.add_argument('-m', help='Required a fastText trained model', required=True)
parser.add_argument('-f', help='an input dataset', required=True)
parser.add_argument('-ic', nargs='+', help='input columns inside the dataset', required=True)
parser.add_argument('-oc', nargs='+', help='output columns in the output', required=True)
args = parser.parse_args()

PREFIX = 'vector'
try:
    print "Loading fastText model..."
    model = fastText.load_model(args.m)

    print "Reading csv input..."
    df_nodes = pd.read_csv(args.f, encoding='utf-8')
    df_output = pd.DataFrame(columns=args.oc)

    print "Generating embeddings..."
    for c in args.ic:
        if c in df_nodes.columns:
            df_nodes[PREFIX+c] = [model.get_word_vector(n) for n in df_nodes[c]]

    for o in args.oc:
        if PREFIX+o in df_nodes.columns:
            df_output[o] = df_nodes[PREFIX+o]
        elif o in df_nodes.columns:
            df_output[o] = df_nodes[o]

    print "Writing to output file..."
    df_output.to_csv(args.output, index=False)
except Exception as e:
    print e
