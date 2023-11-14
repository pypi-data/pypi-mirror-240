"""
CSV NER Tagging Tool

Usage:
------
Run the script with the following command:

arabi_ner2  input.csv --text-columns "TextColumn1" "TextColumn2" --additional-columns "Column3" "Column4" --output-csv output.csv
"""

import argparse
import pandas as pd
from nlptools.utils.sentence_tokenizer import sent_tokenize
from nlptools.morphology.tokenizers_words import simple_word_tokenize
from nlptools.arabiner.bin.infer import ner

def process_csv(input_csv, text_columns, additional_columns, output_csv):
    # Read CSV
    df = pd.read_csv(input_csv)

    # Process each text column
    for col in text_columns:
        # Sentence and word tokenization
        df[col] = df[col].apply(lambda text: [simple_word_tokenize(sent) for sent in sent_tokenize(text)])
        # Apply NER on tokenized sentences
        df[col] = df[col].apply(lambda sentences: [ner(sentence) for sentence in sentences])

    # Retain additional columns and the processed text columns
    output_columns = text_columns + additional_columns
    output_df = df[output_columns]

    # Write to CSV
    output_df.to_csv(output_csv, index=False)

def main():
    parser = argparse.ArgumentParser(description="CSV NER Tagging Tool")
    parser.add_argument("input_csv", help="Path to the input CSV file")
    parser.add_argument("--text-columns", nargs='+', required=True,
                        help="Column names in the CSV file to apply NER tagging")
    parser.add_argument("--additional-columns", nargs='*', default=[],
                        help="Additional column names to retain in the output")
    parser.add_argument("--output-csv", default="output.csv",
                        help="Path to the output CSV file")

    args = parser.parse_args()
    process_csv(args.input_csv, args.text_columns, args.additional_columns, args.output_csv)

if __name__ == "__main__":
    main()

# arabi_ner2  input.csv --text-columns "TextColumn1" "TextColumn2" --additional-columns "Column3" "Column4" --output-csv output.csv
