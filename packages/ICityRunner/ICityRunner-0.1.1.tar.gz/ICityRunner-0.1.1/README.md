# ICity Runner

- Parameters and Configurations can be modified in  `config.py`

## 1.How to execute `ICity Runner` ? 

Run command `python ICityRunner.py`



## 2.Instruction

All configurations contain in `config.py`, which can be changed by user's requirements.

> [Archaea_RM] is processed in default

More information see  `config.py`



## 3.supplement

Package the following instructions into `ICityRunner.py` 

```
python hash_SeedExtract

python findneighborhood.py

grep -v "===" Vicinity.tsv | cut -f1 | sort -u > VicinityIDs.lst

blastdbcmd -db Database/ProteinsDB -entry_batch VicinityIDs.lst -long_seqids > Vicinity.faa

bash RunClust.sh Vicinity.faa 0.3 VicinityPermissiveClustsLinear.tsv

python MakeProfiles.py -f VicinityPermissiveClustsLinear.tsv -c CLUSTERS/ -d Database/ProteinsDB

python RunPSIBLAST.py -c CLUSTERS/ -d Database/ProteinsDB

python SortBLASTHitsInMemory.ipynb

bash Cal.sh CLUSTERS/Sorted/ Database/ProteinsDB VicinityPermissiveClustsLinear.tsv Relevance.tsv

python SortRelevance.ipynb
```





