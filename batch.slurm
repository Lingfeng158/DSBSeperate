#!/bin/bash
#SBATCH --mail-user=lingfeng.li@vanderbilt.edu
#SBATCH --mail-type=ALL
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --mem=24G
#SBATCH --time=4:20:00
#SBATCH --output=output.txt

ml Anaconda3
source activate env2.7
python main.py
