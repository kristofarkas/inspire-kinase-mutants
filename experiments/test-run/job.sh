#!/bin/bash

export RADICAL_PILOT_DBURL='mongodb://htbac:htbac@ds251287.mlab.com:51287/htbac-inspire-1'
export SAGA_PTY_SSH_TIMEOUT=2000
export RADICAL_PILOT_PROFILE=True
export RADICAL_ENMD_PROFILE=True
export RADICAL_ENMD_PROFILING=1
export RP_ENABLE_OLD_DEFINES=True

export RADICAL_ENTK_VERBOSE='DEBUG'
export RADICAL_SAGA_VERBOSE='DEBUG'
export RADICAL_PILOT_VERBOSE='DEBUG'

export LD_PRELOAD='/lib64/librt.so.1'

export PATH=/lustre/atlas/scratch/farkaspall/chm126/miniconda2/bin:$PATH
export LD_LIBRARY_PATH=/lustre/atlas/scratch/farkaspall/chm126/miniconda2/lib:$LD_LIBRARY_PATH

python single-mut.py



