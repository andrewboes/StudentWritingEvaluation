import pandas as pd
import os
import sys
from termcolor import colored

def color_text(text_id, train_df, color_scheme = None):
    if not color_scheme:
        color_scheme = {
        'Lead': 'green',
        'Position': 'red',
        'Claim': 'blue',
        'Counterclaim': 'magenta',
        'Rebuttal': 'yellow',
        'Evidence': 'cyan',
        'Concluding Statement': 'grey'
    } 
    with open(f'train/{text_id}.txt') as f:
        lines = f.readlines()
    text = ''.join(lines)
    
    annot_df = train_df[train_df.id == text_id]
    blocks = [(int(row['discourse_start']),int(row['discourse_end']), color_scheme[row['discourse_type']]) for k, row in annot_df.iterrows()]
    blocks.sort()
    i = 0
    last_symbol = -1
    while i < len(blocks):
        if blocks[i][0] > last_symbol + 1:
            blocks.insert(i, (last_symbol+1, blocks[i][0] - 1, None))
        last_symbol = blocks[i][1]
        i += 1
    if last_symbol < len(text):
        blocks.append((last_symbol+1, len(text) - 1, None))

    colored_text = ''.join([colored(text[x[0]:x[1]+1], x[2]) for x in blocks])
    return colored_text

def print_text(text_id):
    with open(f'train/{text_id}.txt') as f:
        lines = f.readlines()
    print(''.join(lines))

def main():
  textFiles = os.listdir('train/')
  print(len(textFiles))
  trainFile = pd.read_csv('train.csv')
  print(trainFile.info())
  print(trainFile.describe())
  print(trainFile.head(15))
  print_text('423A1CA112E2')
  #pip install termcolor
  print(color_text('423A1CA112E2', trainFile))
  print(color_text('6B4F7A0165B9', trainFile))
  print(color_text('A8445CABFECE', trainFile))

if __name__ == "__main__":
    main()
