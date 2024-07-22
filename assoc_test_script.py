import os
import pandas as pd

# Define the number of permutations
num_permutations = 1000

# Path to LDAK executable
ldak_path = "./ldak5.XXX"

# Iterate through each permuted dataset
for i in range(1, num_permutations + 1):
    # Define file names
    pheno_file = f"permuted_{i}.pheno"
    # out_file = f"ldak_results_{i}"
    
    # Run LDAK command
    ldak_cmd = f"{ldak_path} --linear linear --pheno {pheno_file} --bfile data_final_filt"
    # print(f"Running command: {ldak_cmd}")
    os.system(ldak_cmd)
    
    new_name = f"perm_{i}_linear.pvalues"
    # rename the linear.pvalues file
    os.rename("linear.pvalues", new_name)
