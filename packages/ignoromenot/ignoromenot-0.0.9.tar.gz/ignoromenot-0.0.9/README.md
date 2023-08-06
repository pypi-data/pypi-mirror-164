# IgnoroMeNot
IgnoroMeNot outputs a list of ignorome genes highly associated with other well-annotated genes. Ignorome genes are genes that have little to no validated experimental Gene Ontology annotations (see __xxx__). Strong associations between ignorome genes and well-annotated genes can help fill the gaps in the protein function space and improve the balance in knowledge between "annotation-rich" and "annotation-poor" genes.

## Installation
IgnoreMeNot is available on [PyPI](https://pypi.org/project/ignoromenot/0.0.5/). IgnoroMeNot can be installed with [conda](https://anaconda.org/anphan0828/ignoromenot).

### Required files:
IgnoroMeNot requires a tab-separated file of a list of genes with any single annotation metric (e.g. GO annotation count, information content, article count). Highest and lowest annotated genes are defined based on this metric. Below is an example of how the rank table should look like:

| Genes  | Metric            |
|--------|-------------------|
| Q46822 | 55.34890734396416 |
| P18843 | 99.78875455312165 |

Additionally, a STRING interaction network and a protein alias file of the organism to be examined are required and can be downloaded from [STRING](string-db.org/cgi/download). Example: E. coli [alias file](https://stringdb-static.org/download/protein.aliases.v11.5/511145.protein.aliases.v11.5.txt.gz) and [interaction network](https://stringdb-static.org/download/protein.links.full.v11.5/511145.protein.links.full.v11.5.txt.gz)

## IgnoroMeNot usage:
```
usage: ignoromenot.py [-h] --ranktable RANKTABLE --idtable IDTABLE --stringppi STRINGPPI
                      [--threshold_top THRESHOLD_TOP | --percentile_top PERCENTILE_TOP]
                      [--threshold_bot THRESHOLD_BOT | --percentile_bot PERCENTILE_BOT]
                      [--threshold_ppi THRESHOLD_PPI | --percentile_ppi PERCENTILE_PPI] 

Optional arguments:
-h, --help                  Show this help message and exit
-ttop, --threshold_top      Set an absolute upper threshold for most annotated genes based on the given metric. 
                            Default to 100
-ptop, --percentile_top     Set a relative upper threshold for most annotated genes at k-th percentile based on the given metric. 
                            Cannot be provided simultaneously with --threshold_top
-tbot, --threshold_bot      Set an absolute lower threshold for least annotated genes based on the given metric. 
                            Default to 5
-pbot, --percentile_bot     Set a relative lower threshold for least annotated genes at k-th percentile based on the given metric. 
                            Cannot be provided simultaneously with --threshold_bot
-tppi, --threshold_ppi      Set an absolute upper threshold for STRING protein-protein interaction score. 
                            Default to 500
-pppi, --percentile_ppi     Set a relative upper threshold for STRING protein-protein interaction score.
                            Cannot be provided simultaneously with --threshold_ppi
                            
Required arguments:
-rank, --ranktable          The path to a tab-separated file of a list of genes with any single annotation metric (see above sample rank table)
-id, --idtable              The path to a STRING protein alias file of the organism being examined. 
                            The filename must start with the organism ID (e.g., 9606 for human, 511145 for E.coli)
-ppi, --stringppi           The path to a STRING interaction network of the organism being examined.
                            The filename must start with the organism ID (e.g., 9606 for human, 511145 for E.coli)
```
### Example usage:
Demo data of E.coli are included in the GitHub repository.

``$ python3 src/ignoromenot/ignoromenot.py --ranktable demodata/WyattClarkIC-perprotein.tsv --idtable demodata/511145.protein.aliases.v11.5.txt --stringppi demodata/511145.protein.links.full.v11.5.txt --percentile_top 90 --percentile_bot 1 --threshold_ppi 850``

This command reads 3 input files, where the genes coming from E.coli (511145) are ranked based on their Wyatt Clark information content (``WyattClarkIC-perprotein.tsv``). ``--percentile_top 90`` indicates that the genes at the top 10% with respect to Wyatt Clark infromation content are taken,
``--percentile_bot 1`` takes the bottom 1% annotated genes based on Wyatt Clark information content (those are the ignorome genes), and ``--threshold_ppi 850`` chooses STRING coexpression score (``511145.protein.links.full.v11.5.txt``) of 850 and above. The protein alias file (``511145.protein.aliases.v11.5.txt``) makes sure that protein names from different databases have their IDs mapped properly to STRING interaction network.

IgnoroMeNot outputs a list of ignorome genes based on these parameters. If IgnoroMeNot is run with internet connection, it also provides users with all STRING interaction partners of these ignorome genes above ``--threshold_ppi`` via STRING API.
