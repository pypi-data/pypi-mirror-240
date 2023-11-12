import numpy as np
from typing import Dict, Any
import re
from lcapy import Circuit

# command generator functions : 
latex_command_win = lambda filename: f"pdflatex {filename}"
latex_command_unix = lambda filename, logfile: f"pdflatex {filename} > {logfile}"

# variable initialization utilities : 
def init_var(var_def: Dict[str, Any], precision: int=4) -> np.ndarray[np.float64]:

    dim = var_def.get("dim", 1)

    if var_def["dist"] == "uniform":
        val = np.random.rand(dim)*(var_def["max"]-var_def["min"]) + var_def["min"]
    elif var_def["dist"] == "normal": #! Implement with mean and std
        val = np.random.randn(dim)*(var_def["max"]-var_def["min"]) + var_def["min"]
    elif var_def["dist"] == "exact":
        val = np.array([var_def["val"]])

    if "round" in var_def.keys() and var_def["round"]:
        if var_def.get("int", False):
            val = np.round(val, 0)
        else:
            val = np.round(val, precision)
     
    if dim == 1:
        
        val = val[0]

        if var_def.get("int", False):
            val = int(val)

    return val

def init_var_vals(var_defs: Dict[str,Dict[str, int]], precision: int=4) -> Dict[str, float]:
    var_vals = {}
    for var in var_defs.keys():
        
        nelems = var_defs[var].get("nelems", 1)

        if nelems == 1:
            val = init_var(var_defs[var], precision)
            var_vals[var] = val
        else:
            for ind in range(nelems):
                varname = f"{var}{ind+1}"
                val = init_var(var_defs[var], precision)
                var_vals[varname] = val
                
    return var_vals

# netlist util functions : 
def add_voltage_and_current_labels(netlist_str: str) -> str:
    """
    Adds voltage and current arrows and labels to the given 
    netlist and returns this as a string back.

    :param netlist_str: String containing the netlist file content.
    :type netlist_str: str
    :return: Modified netlist string.
    :rtype: str
    """
    net_elems = netlist_str.split('\n')
    net_elems_clean = []
    for elem in net_elems:

        if elem[0] not in ['W', ';']:
            e = elem[:2]
            e = e.replace('V', 'U')

            elem = re.sub(", [i]=I_\{[^}]+\}", '', elem)
            elem = re.sub(", [v]=U_\{[^}]+\}", '', elem)
            elem += ", v=U_{" + e + "}, i=I_{" + e + "}"

        net_elems_clean.append(elem)

    return '\n'.join(net_elems_clean)

def draw_netlist(task, fig_id) -> None:

    network = Circuit(task["netlist"])
    network.draw(task["insert_figpaths"][fig_id], style="european")
    
    netlist = network.netlist()
    netlist = add_voltage_and_current_labels(netlist)

    network_solution = Circuit(netlist)

    if task["draw_current_voltage_solution"]:
        network_solution.draw(task["insert_figpaths_solution"][fig_id], style="european")