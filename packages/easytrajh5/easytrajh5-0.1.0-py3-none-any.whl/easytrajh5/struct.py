import logging
import pickle
from path import Path

import mdtraj
import parmed
from parmed import unit

from .pdb import remove_model_lines

logger = logging.getLogger(__name__)

__doc__ = """
Useful transforms for parmed.Structure, mdtraj.Trajectory, and OpenMM
"""


def dump_parmed(pmd: parmed.Structure, fname: str):
    with open(fname, "wb") as handle:
        pickle.dump(file=handle, obj=pmd.__getstate__())


def load_parmed(fname: str) -> parmed.Structure:
    with open(fname, "rb") as handle:
        pmd = parmed.structure.Structure()
        pmd.__setstate__(pickle.load(file=handle))
    return pmd


def get_parmed_from_pdb(pdb: str) -> parmed.Structure:
    """
    Reads pdb with some sanity checks for model lines

    :param pdb: str - either .parmed or .pdb
    """
    suffix = Path(pdb).ext
    if not suffix == ".pdb":
        raise ValueError(f"Can't process {pdb} of type {suffix}, only .pdb")
    # Check for issue where mdtraj saves MODEL 0, which throws error in parmed
    remove_model_lines(pdb)
    return parmed.load_file(pdb)


def get_parmed_from_parmed_or_pdb(pdb_or_parmed: str) -> parmed.Structure:
    """
    :param pdb_or_parmed: str - either .parmed or .pdb
    """
    suffix = Path(pdb_or_parmed).ext
    if suffix == ".pdb":
        pmd = get_parmed_from_pdb(pdb_or_parmed)
    elif suffix == ".parmed":
        pmd = load_parmed(pdb_or_parmed)
    else:
        raise ValueError(f"Can't process {pdb_or_parmed} of type {suffix}")
    return pmd


def get_parmed_from_mdtraj(traj: mdtraj.Trajectory, i_frame=0) -> parmed.Structure:
    return parmed.openmm.load_topology(traj.top.to_openmm(), xyz=traj.xyz[i_frame])


def get_parmed_from_openmm(openmm_topology, openmm_positions=None) -> parmed.Structure:
    return parmed.openmm.load_topology(openmm_topology, xyz=openmm_positions)


def get_mdtraj_from_parmed(pmd: parmed.Structure) -> mdtraj.Trajectory:
    return mdtraj.Trajectory(
        xyz=pmd.coordinates / 10, topology=mdtraj.Topology.from_openmm(pmd.topology)
    )


def get_mdtraj_from_openmm(openmm_topology, openmm_positions) -> mdtraj.Trajectory:
    if unit.is_quantity(openmm_positions):
        openmm_positions = openmm_positions.value_in_unit(unit.nanometer)
    mdtraj_topology = mdtraj.Topology.from_openmm(openmm_topology)
    return mdtraj.Trajectory(topology=mdtraj_topology, xyz=openmm_positions)


