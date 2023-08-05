# RIBFIND

## Running RIBFIND
To run RIBFIND on just a protein, a pdb file and a DSSP file is required:

```bash
python -m ribfind.cli \
             --model test/data/model/model.pdb \
             --dssp  test/data/model/model.dssp
```

To run RIBFIND on a protein with RNA a RNAML file is required:

```bash
python -m ribfind.cli \
             --model test/data/model/model.pdb \
             --dssp  test/data/model/model.dssp \
             --rnaml test/data/model/model.xml
```

The cutoff distance parameters which are used to calculate clusters can be
adjusted for protein and RNA molecules.

```bash
python -m ribfind.cli \
             --model test/data/model/model.pdb \
             --dssp test/data/model/model.dssp \
             --rnaml test/data/model/model.xml \
             --protein-cutoff-distance 4.2 \
             --rna-cutoff-distance 1.23
```

Example output:

```text
$ python -m ribfind.cli \
         --model test/data/model/model.pdb \
         --dssp test/data/model/model.dssp
Summary of RIBFIND clusters for the range of cutoffs
% cutoff	# clusters	# clustered SSEs	Cluster weight
  0.0000	         2	              12	          2.92
 33.3333	         2	              11	          2.85
 36.3636	         3	              11	          3.85
 37.5000	         1	               3	          1.23
 46.1538	         0	               0	          0.00
Writing summary:
     model/protein/model.summary
Writing clusters:
     model/protein/model.densclust_0
     model/protein/model.densclust_33
     model/protein/model.densclust_36
     model/protein/model.densclust_37
     model/protein/model.densclust_46
Writing ChimeraX scripts:
     model/protein/model.chimerax_0.cxc
     model/protein/model.chimerax_33.cxc
     model/protein/model.chimerax_36.cxc
     model/protein/model.chimerax_37.cxc
     model/protein/model.chimerax_46.cxc
```

### Other parameters
The optional arguments: `--protein-dens-cutoff` and
`--rna-dens-cutoff`, control the minimum size of a cluster to be
considered as a rigid body.  The default size is 3, which means if a
cluster contains two SSEs such as a sheet and a helix it won't be
considered as a rigid body, where as a sheet and two helices will be
considered.  Choosing a value of 1 means all SSEs will be in a
cluster.

## Installing RIBFIND
RIBFIND can be installed on the system by running `pip install .` from the project directory.
The `ribfind` command should now be available.


## Output files
The output of the command will be a set of files.  The `.summary` file shows
all the clusters for different percentage of interacting residues.

The `.densluster_PERC` list the residues in each rigid body at a given `PERC` cutoff.

The `.chimeraX_PERC.cxc` files can be opened in ChimeraX. Each rigid body will
be assigned a color. Unclustered SSEs and loops will be white.

## Other parameters
The `--protein-helix-ratio` flag (default 0.4), allows tuning interaction
between alpha helices. Helices with a residue ratio below this value do not
interact.

The `--protein-minimum-strand-length` flag (default 4), allows tuning how
strands in sheets interact with other SSEs. Strands below this length are not
used in residue interaction calculations.

The `--protein-dens-cutoff` flag (default 3), defines the minimum number of
SSEs which make up a rigid body cluster.

The `--rna-minimum-strand-length` flag (default 4), allows tuning how
strands interact with other SSEs. Strands below this length are not
used in residue interaction calculations.

The `--rna-dens-cutoff` flag (default 3), defines the minimum number of
SSEs which make up a rigid body cluster.

TODO: How do you generate DSSP and RNAML files.


## Algorithms
### Determining protein interaction
Proteins are divided into helices and sheets. A rigid body is a cluster of
helices and sheets that interact. An interaction between `A` and `B` is defined
as the ratio of side-chains in `A` which are with in a cutoff distance of
side-chains in `B`. The interaction is thus asymmetric: `Interaction(A,B) !=
Interaction(B,A)`. Thus the overall interaction is defined as the maximum of the
two: `max(Interaction(A,B), Interaction(B,A))`.

#### More detail
In general, interaction is defined in terms of all residues in helix or sheet,
however two extra rules apply:

1. If the sheet has strands with less than `dna-minimum-strand-length` residues, the residues from those
   strands are not included in calculating the interaction.
2. Two helices with a length ratio less than `helix-ratio` do not interact.


#### Implementation
The above algorithm is implemented in the `ProteinInteraction` class. An
interaction objected is constructed with parameters for interaction:
``minimum_strand_length` and `helix_ratio`. The `get_interaction` method accepts
two SSEs (helix or sheet) and returns the interaction (a floating point). Given
a list of SSEs, the `graph` method returns an interaction graph which can be
used for clustering. Each edge in the graph spans two SSEs (helices or sheets)
and the edge value represents the interaction strength.

### Calculating side chain contact distance.
Interactions are defined in terms of residues with side chains which are with in
a cutoff distance of one another. How is this distance defined? A number of
possibilities exist for determining such a distance, including closest or
furthest atoms between the side chain pairs. In RIBFIND the distance is
determined by calculating a center point for each side chain.

#### More detail
For all residues except glycine, the center of a side chain is the average of
all atomic coordinates in the side chain. For glycine, the center is simply the
position of the C alpha atom.

#### Implementation
A `BioPyResidueCenters` object can be constructed from a BioPython structure. The
center of every side chain is computed upon construction. Given two residues
with residues numbers N1 and N2 belonging to chains C1 and C2, the `in_contact`
will return true if they are with contact of one another

To use other sources of atomic information such as Gemmi atomic models, a new
object should be implemented which supports the `in_contact` method.

### Determining RNA Interactions
#### More detail
#### Implementation

### Calculating Nucleic acid contact distance
#### More detail
#### Implementation

### Interaction graph and clustering

## Authors

