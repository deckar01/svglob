import argparse
from svglob import glob


parser = argparse.ArgumentParser(description=glob.__doc__)
parser.add_argument('files', nargs='+', help='The SVG files to process.')
parser.add_argument('--suffix', default='.glob', help='Text to add to the end of the file name (default: .glob).')

args = parser.parse_args()
for file in args.files:
    try:
        new_file = glob(file, args.suffix)
        print(file, '->', new_file)
    except Exception as e:
        print('ERROR:', file, e.split('\n')[0])
