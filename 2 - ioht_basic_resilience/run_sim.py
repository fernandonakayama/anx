"""run_sim.py
"""

# pylint: disable=invalid-name

from anx import model_utils
from anx import utils
from anx import driver
from anx import config

# set model to use and paths
model_name = "ioht_basic"
input_dir = "./input"
output_dir = "./output"

print("\n Working on model '{:s}'\n".format(model_name))

# build the model
print(" Loading model definitions..")
model_edges = model_utils.load_links(model_name, input_dir)
node_types = model_utils.load_node_types(model_name, input_dir)
model_param = model_utils.load_param(model_name, input_dir)

print("\n Creating computational model..")
M = model_utils.make_model(model_edges, node_types, model_param,
                          model_name)

# set the simulation time verbose level
sim_time = 1000
# set verbose level
#   config.VERB_HI - all available info
#   config.VERB_LO - intermediate info
#   config.VERB_NO - minimal info
verbose_level = config.VERB_LO

# run the simulation
print("\n Running simulation on model '{:s}'".format(M.model_name))
driver.run_sim(M, sim_time, output_dir, verbose_level)

print("\n All done.\n")
