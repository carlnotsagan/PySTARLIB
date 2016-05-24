# This example extracts all available forward rates.
# 
# Does not include compound rates contained in MESA
# that include '_to_' for reactions of the form
# a_b_c_to_d_e, a_b_c_to_d, a_to_b_c_d, etc.

import py_starlib as ps
import subprocess

# Assumes user has provided a rate list names 'reactions_list.txt',
# see example 'reactions_list' for formatting.
# List of reactions for a given MESA network can be obtained by using
# show_net_reactions_info = .true. in your &star_job options.

# this line unzips the compressed starlib library
subprocess.call(['./open_starlib.sh']) 

# get rates
ps.extract_rates()