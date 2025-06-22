#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=100M
#SBATCH --time=00:01:00

# Load recommended modules
module load python/3.8.10 scipy-stack/2023a

# Create and activate a virtual environment
VENV_DIR=$SLURM_TMPDIR/habit_env
virtualenv --no-download $VENV_DIR
source $VENV_DIR/bin/activate

# Install asteval
pip install --no-index --upgrade pip
pip install --no-index asteval

# Run the script
python Project_mparrondo.py

# Resource use report
seff $SLURM_JOBID
