# GENERATOR3000
A tool for generating words sequences. Run ```train.py```. It trains on files that are given in test dir add writes model into a file. After this you can run ```generate.py```. It generates a word sequence and writes it into a file or stdout.

### Usage:
```
git clone https://github.com/alexander-deb/generator3000.git
cd generator3000
python3 train.py [command line arguments. info below]
python3 generate.py [command line arguments. info below]

For example:
python3 train.py --input-dir=testdir --model=first_model --lc
python3 generate.py --seed=earth --model=first_model --length=10 --output=out.txt
```

#### Command line arguments:
##### for train.py:
```
usage: train.py [-h] [--input-dir INPUT_DIR] [--model MODEL] [--lc [LC]]

optional arguments:
  -h, --help             show this help message and exit
  --input-dir INPUT_DIR  Directory, with documents for training models
  --model MODEL          Name for trained model file
  --lc [LC]              Makes lowercase text for model
 ```
  #### for generate.py:
```
usage: generate.py [-h] [--seed SEED] [--model MODEL] [--length LENGTH] [--output OUTPUT]

optional arguments:
  -h, --help       show this help message and exit
  --seed SEED      Beginning word
  --model MODEL    Path to the trained model file
  --length LENGTH  Length of generated sequence
  --output OUTPUT  File which will be used to put generated sequence
```
  