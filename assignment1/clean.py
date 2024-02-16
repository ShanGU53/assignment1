import pandas as pd

def clean(input_file1,input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df = df.drop(columns=['respondent_id'])
    df = df.dropna()
    df = df[~df['job'].str.contains('insurance|Insurance', regex=True, case=False)]
    return  df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='Data file1 (CSV)')
    parser.add_argument('input2', help='Data file2 (CSV)')
    parser.add_argument('output', help='Cleaned data file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)
    cleaned.to_csv(args.output, index=False)