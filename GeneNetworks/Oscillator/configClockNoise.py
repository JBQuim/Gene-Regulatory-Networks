import numpy as np
from GeneClass import *
import random

def event(t, systemState):
    if random.random()>0.9:
        rand = (random.random()-0.5)/10
        systemState[3] += rand
        systemState[2] -= rand
    return systemState


def setup():
    # --------------
    # set up simulation parameters
    # --------------

    # step is the time advanced every timestep
    # endTime is the time at which the simulation is finished
    # save is the folder in which to save output image e.g. "GeneNetworks/NegFFL/NegFFL.png" set to -1 if no saving wanted
    step = 0.1
    endTime = 500
    saveFile = "GeneNetworks/Oscillator/clockNoise.png"
    plotInfo = [[0, 1], [2, 3]]  # plot info is a list of lists. every list contains the species to be graphed on a subplot

    # speciesNames holds the labels of all species
    # concentrations holds the concentrations of all substances at time 0
    speciesNames = np.array(["X", "Y", "X", "Y"])
    concentrations = np.array([6, 5, 6, 5])

    # genes are assigned to species
    # species = loadNetwork("LIFO/LIFO") will load network from file "GeneNetworks/LIFO/LIFO.txt"
    # saveNetwork(species,"LIFO/LIFO") will save any changes done to the network after loading to GeneNetworks/LIFO/LIFO.txt
    species = loadNetwork("Oscillator/clockNoise")

    return step, endTime, saveFile, speciesNames, species, concentrations, plotInfo
