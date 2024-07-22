
# clumping
for i in 01 02 03 04 05 06 07;
do
./ldak5.XXX --thin-tops top$i --bfile validation --pvalues pvalues_filt.pvalues --cutoff 1e-$i --window-cm 1 --window-prune 0.1
done


# PRS
for i in 01 02 03 04 05 06 07;
do
./ldak5.XXX --calc-scores scores_clump$i --scorefile scores_filt.txt --bfile validation --power o --pheno validation.pheno --extract top$i.in
done
