# deeplabcut-run-cluster
Run of DeepLabCut on the ICM cluster

To install DeepLabCut:
* https://github.com/AlexEMG/DeepLabCut/blob/master/docs/installation.md

~~~bash
git clone https://github.com/Maxime91860/deeplabcut-run-cluster.git
cd deeplabcut-run-cluster

# To label data on workstation 
python scripts/deeplabcut_demo_workstation.py

# To submit the training from the login node 
sbatch slurm/runDeepLabCut.sh
~~~
