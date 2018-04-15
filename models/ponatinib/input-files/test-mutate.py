import os
import re

from pdbfixer.pdbfixer import PDBFixer
from simtk.openmm import app

aa3_to_1 = {
    'ALA': 'A', 'ARG': 'R', 'ASP': 'D', 'ASN': 'N', 'CYS': 'C', 'GLU': 'E',
    'GLN': 'Q', 'GLY': 'G', 'HIS': 'H', 'ILE': 'I', 'LEU': 'L', 'LYS': 'K',
    'MET': 'M', 'PHE': 'F', 'PRO': 'P', 'SER': 'S', 'THR': 'T', 'TRP': 'W',
    'TYR': 'Y', 'VAL': 'V', 
}

aa1_to_3 = {one: three for three, one in aa3_to_1.items()}

re_aa1_mut = re.compile("([A-Z])([0-9]+)([A-Z])")

def convert_mutation_list(mutations):

    pdbfix_mutations = []

    for mutation in mutations:

        match = re_aa1_mut.match(mutation.upper())

        if match:
            elements = match.groups()
            orig = aa1_to_3[elements[0]]
            resno = elements[1]
            final = aa1_to_3[elements[2]]
            pdbfix_mutation = '{:s}-{:s}-{:s}'.format(orig, resno, final)
            pdbfix_mutations.append(pdbfix_mutation)

    return pdbfix_mutations

input_pdbfile = 'cAbl.pdb'
chain = "A"
sequences = [['m244v'], ['l248r'], ['l248v'], ['g250e'],
             ['y253f'], ['e255k'], ['e255v'], ['v299l'],
             ['t315a'], ['t315i'], ['f317c'], ['f317i'],
             ['f317l'], ['f317v'], ['m351t'], ['e355a'],
             ['f359c'], ['f359i'], ['f359v'], ['h396r'],
             ['e459k'],
            ]


for mutations in sequences:

    mutation_list = convert_mutation_list(mutations)

    fixer = PDBFixer(filename=input_pdbfile)
    fixer.applyMutations(mutation_list, chain)

    prefix = os.path.splitext(input_pdbfile)[0]

    out_filename = "{:s}_{:s}.pdb".format(prefix, '-'.join(mutations))
    outfile = open(out_filename, 'w')
    app.PDBFile.writeFile(fixer.topology, fixer.positions, outfile)
    outfile.close()
