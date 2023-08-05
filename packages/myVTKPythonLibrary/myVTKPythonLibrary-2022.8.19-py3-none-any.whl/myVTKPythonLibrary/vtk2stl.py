#!python3
#coding=utf8

########################################################################
###                                                                  ###
### Created by Martin Genet, 2012-2022                               ###
###                                                                  ###
### University of California at San Francisco (UCSF), USA            ###
### Swiss Federal Institute of Technology (ETH), Zurich, Switzerland ###
### École Polytechnique, Palaiseau, France                           ###
###                                                                  ###
########################################################################

import argparse

import myPythonLibrary    as mypy
import myVTKPythonLibrary as myvtk

########################################################################

if (__name__ == "__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("vtk_filename", type=str)
    args = parser.parse_args()

    mesh = myvtk.readPData(
        filename=args.vtk_filename)
    myvtk.writeSTL(
        pdata=mesh,
        filename=args.vtk_filename.replace(".vtk", ".stl").replace(".vtp", ".stl"))
