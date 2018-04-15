#! /usr/bin/env python

import os
import sys
import glob
import re

mut = re.compile(".*([a-z][0-9]+[a-z]).*")

mol_files = glob.glob('input-files/*.gaff.mol2')
mol_name = re.split('\.|/', mol_files[0])[1]

pdb_files = glob.glob('input-files/cAbl_*.pdb')
pdb_files.append('input-files/cAbl.pdb')

base_dir = os.getcwd()

for pdb_file in pdb_files:

    match = mut.match(pdb_file)

    if match:

        sys_name = match.groups()[0]

    else:

        sys_name = 'wt'

    build_path = os.path.join(sys_name, 'build')
    cons_path = os.path.join(sys_name, 'constraint')
    
    os.makedirs(build_path)
    os.makedirs(cons_path)

    leap_file = open(os.path.join(build_path, 'complex.leap.in'), 'w')

    with open('template.leap.in', 'r') as template:
        for line in template:
            if 'PROTEIN' in line:
                line = line.replace('PROTEIN', pdb_file)
            elif 'DRUG':
                line = line.replace('DRUG', mol_name)

            leap_file.write(line)

    leap_file.close()

    os.chdir(build_path)

    os.system('tleap -f complex.leap.in')

    if os.stat('complex.top').st_size == 0:
        print('FAIL!')
    else:
        print('WIN!')
        os.system('gawk -f ../../input-files/constraint.awk complex.pdb ../../input-files/cAbl.pdb > ../constraint/cons.pdb'.format(pdb_file))

    os.chdir(base_dir)
