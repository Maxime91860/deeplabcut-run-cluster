#!/bin/bash
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --mem=16G
#SBATCH --time=2-00:00:00
#SBATCH --job-name="DeepLabCut Demo"
#SBATCH --workdir=.
#SBATCH --error=logs/deeplabcut_%j.txt
#SBATCH --output=logs/deeplabcut_%j.txt

module load CUDA
module load DeepLabCut
python scripts/deeplabcut_demo_cluster.py
