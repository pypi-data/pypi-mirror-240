import itertools
import logging
from path import Path

import mdtraj
import numpy
import parmed
import pydash as py_
from parmed.amber import AmberMask

from .fs import load_yaml
from .struct import get_mdtraj_from_parmed

logger = logging.getLogger(__name__)
data_dir = Path(__file__).parent / "data"
resnames_by_keyword = load_yaml(data_dir / "select.yaml")


def select_mask(pmd, mask, is_fail_on_empty=True):
    """
    Selects atom based on a selection string which is based on a combination
    atom selection langauge.There are several different types of selection
    modes strings, where the first word is often used a mode selector.

    - keywords
        - accepts (in any order): 'ligand', 'protein', 'water', 'lipid', 'salt',
          'solvent', 'lipid', 'nucleic'
        - If more than one keyword is specified, it is assumed they are joined with "or"
          operation (i.e. 'ligand protein' will return both ligand and protein atom indices).
        - The keyword 'ligand' will find the residue 'LIG', 'UNL', 'UNK', or
          whatever is in 'ligand' in the file 'easytrajh5/data/select.yaml'
        - The keyword 'pocket' will find the closest 6 residues to the 'ligand' group.
        - The keyword 'near' will require a following resname, with an optional integer, e.g.:
            'near ATP'
            'near ATP 5'
        - The keyword 'resname' identifies a single residue type (usually a ligand):
            'resname LEU'
    - residue 0-indexed selections
        "resi 0 10-13" - selects atoms in the first and 11th, 12th and 13th residues
    - atom 0-indexed selections
        "atom 0 55 43 101-105" - selects the first, 56th, 44th, 101 to 105th atom
    - AMBER-style atom selection https://parmed.github.io/ParmEd/html/amber.html#amber-mask-syntax
        "amber :ALA,LYS" - selects all alanine and lysine residues
    - MDTraj-style atom selection - https://mdtraj.org/1.9.4/atom_selection.html
        "mdtraj protein and water" - selects protein and water
    - furthermore, selections can be combined with set operators ("not", "intersect", "merge", "diff"),
        "intersect {not {amber :ALA}} {protein}"
        "diff {protein} {not {amber :ALA}}"
        "not {resname LEU}"
        "merge {near BSM 8} {amber :ALA}"
    - some useful masks:
        - no solvent "not {solvent}"
        - just the protein "protein"
        - heavy protein atoms "diff {protein} {amber @/H}"
        - no hydrogens "not {amber @/H}"
        - pocket and ligand "pocket ligand"
        - specified ligand with 10 closest neighbours "resname UNL near UNL 10"

    :parmam parmed_structure: parmed.Structure
    :param mask: Union[str, List[int]]

    :return: [int] - list of atom indices to pmd
    """

    def get_i_atoms_of_ast(ast):
        has_list = py_.some(ast, lambda node: isinstance(node, list))
        if not has_list:
            expr = " ".join(ast)
            value = process_expr(pmd, expr)
            return value

        operator = ast[0]

        if operator == "not":
            if len(ast) != 2:
                raise ValueError("not: must have only 1 following expr in {}")
            i_atoms1 = get_i_atoms_of_ast(ast[1])
            i_all_atoms = [a.idx for a in pmd.atoms]
            return diff_list(i_all_atoms, i_atoms1)

        elif operator == "merge":
            result = []
            for node in ast[1:]:
                result.extend(get_i_atoms_of_ast(node))
            return list(set(result))

        elif operator == "intersect":
            result = set(get_i_atoms_of_ast(ast[1]))
            for node in ast[2:]:
                i_atom_set = set(get_i_atoms_of_ast(node))
                result = result.intersection(i_atom_set)
            return list(result)

        elif operator == "diff":
            if len(ast) != 3:
                raise ValueError("diff: must have 2 expr in {}")
            i_atoms1 = get_i_atoms_of_ast(ast[1])
            i_atoms2 = get_i_atoms_of_ast(ast[2])
            return diff_list(i_atoms1, i_atoms2)

        else:
            raise ValueError(f"Operator {operator} not in [not diff merge intersect]")

    if isinstance(mask, str):
        i_atoms = get_i_atoms_of_ast(parse_ast(mask))
    elif is_integer_list(mask):
        i_atoms = mask
    else:
        raise ValueError(f"Can't parse atom mask {mask}")

    if is_fail_on_empty and not len(i_atoms):
        raise ValueError("Selection produced no atoms")

    i_atoms = py_.uniq(i_atoms)

    res_indices = py_.uniq([pmd.atoms[i].residue.idx for i in i_atoms])
    logger.info(
        f'select_mask "{mask}" -> {len(i_atoms)} atoms, {len(res_indices)} residues'
    )

    return i_atoms


def is_integer_list(o):
    if not isinstance(o, (list, numpy.ndarray)):
        return False
    for x in o:
        if not isinstance(x, (int, numpy.integer)):
            return False
    return True


def process_expr(pmd, expr):
    expr_lower = expr.lower()
    if expr_lower.startswith("amber "):
        amber_mask = AmberMask(pmd, expr[6:])
        i_atoms = [i_atom for i_atom, mask in enumerate(amber_mask.Selection()) if mask]
    elif expr_lower.startswith("mdtraj "):
        mdtraj_top = mdtraj.Topology.from_openmm(pmd.topology)
        return mdtraj_top.select(expr[6:]).tolist()
    elif expr_lower.startswith("atom "):
        i_atoms = parse_number_list(expr[5:])
    elif expr_lower.startswith("resi "):
        i_atoms = select_resi(pmd, expr[5:])
    else:
        i_atoms = select_keywords(pmd, expr)
    return i_atoms


def parse_ast(mask):
    """
    Parses an expression bounded by curly brackets into an abstract syntax tree
    e.g. 'a {{b c} {d}} e}' -> ['a', [[['b', 'c'], ['d'], 'e']]
    """

    def push(obj, a_list, depth):
        while depth:
            a_list = a_list[-1]
            depth -= 1
        a_list.append(obj)

    def parse_parentheses(tokens):
        groups = []
        depth = 0

        try:
            for token in tokens:
                if token == "{":
                    push([], groups, depth)
                    depth += 1
                elif token == "}":
                    depth -= 1
                else:
                    push(token, groups, depth)
        except IndexError:
            raise ValueError("Parentheses mismatch")

        if depth > 0:
            raise ValueError("Parentheses mismatch")
        else:
            return groups

    mask = mask.replace("{", " { ").replace("}", " } ")
    tokens = py_.filter_(mask.split(" "))
    return parse_parentheses(tokens)


def parse_number_list(num_str_or_list):
    """
    Turns a string "1,2,3-4,5, 7 9-11 8-33" into a list of numbers
    """
    if isinstance(num_str_or_list, str):
        result = []
        parse_s = num_str_or_list.replace("-", " - ").replace(",", " ")
        tokens = parse_s.split()
        n = len(tokens)
        start = None
        for i in range(n):
            if tokens[i] == "-":
                continue
            num = int(tokens[i])
            if i < n - 1 and tokens[i + 1] == "-":
                start = num
                continue
            if start is not None:
                for i in range(start, num + 1):
                    result.append(i)
                start = None
            else:
                result.append(num)
        return result
    elif is_integer_list(num_str_or_list):
        return num_str_or_list
    else:
        raise ValueError(f"Can't process {num_str_or_list}")


def select_resi(pmd, expr):
    i_residues = parse_number_list(expr)
    result = []
    for i, residue in enumerate(pmd.topology.residues()):
        if i in i_residues:
            for a in residue.atoms():
                result.append(a.index)
    return result


def traj_calc_residue_contacts(
    traj, i_residues1, i_residues2, cutoff_nm=None, max_n_residue=None
) -> [int]:
    """
    :return: [int] - indices of closest residues to ligand
    """
    # Generate pairs of residue indices [[i_lig1, i_res1], [i_lig1, i_res2]....]
    pairs = list(itertools.product(i_residues1, i_residues2))

    # Calculate distances as nx1 numpy.array and pairs is nx2 numpy.array
    # periodic=False turns off period cell correction
    distances, pairs = mdtraj.compute_contacts(
        traj, contacts=pairs, scheme="closest-heavy", periodic=False
    )

    # Get sorted top_entries list of contact residues
    top_entries = [(d, pair[1]) for d, pair in zip(distances[0], pairs)]
    top_entries = py_.sort_by(top_entries, lambda e: e[0])
    if max_n_residue:
        top_entries = top_entries[:max_n_residue]
    if cutoff_nm:
        top_entries = py_.filter_(top_entries, lambda e: e[0] <= cutoff_nm)

    return [e[1] for e in top_entries]


def select_residue_contacts(pmd, lig_resnames=["LIG"], max_n_residue=6, cutoff_nm=None):
    """
    Finds the atoms of the residues closest to a ligand residue

    :return: [int]
    """
    logger.info(f"calc_contacts to {lig_resnames}")

    traj = get_mdtraj_from_parmed(pmd)
    residues = list(traj.topology.residues)
    protein_resnames = get_resnames("protein")
    i_ligand_residues = [r.index for r in residues if r.name in lig_resnames]
    i_protein_residues = [r.index for r in residues if r.name in protein_resnames]

    if len(i_ligand_residues) == 0:
        raise ValueError(f"no residue with resname={lig_resname}")

    i_closest_residues = traj_calc_residue_contacts(
        traj,
        i_ligand_residues,
        i_protein_residues,
        cutoff_nm=cutoff_nm,
        max_n_residue=max_n_residue,
    )

    logger.info(f"found {len(i_closest_residues)} residues")

    return select_resi(pmd, i_closest_residues)


def get_resnames(keyword):
    return resnames_by_keyword[keyword]


def select_resnames(pmd, resnames):
    return [a.idx for a in pmd.atoms if a.residue.name in resnames]


def diff_list(list1, list2):
    return list(sorted(set(list1) - set(list2)))


def select_keywords(pmd: parmed.Structure, keyword_selection) -> [int]:
    """
    Select a list of atom  that can be used to slice parmed objects, set restraints, or specify CVs.
    If both keyword and resid selection are applied both are returned (i.e. 'or' combining is assumed).

    :param keyword_selection:
        - accepts (in any order): 'ligand', 'protein', 'water', 'lipid', 'salt', 'solvent', 'lipid', 'nucleic'
          If more than one keyword is specified, it is assumed they are joined with "or"
          operation (i.e. 'ligand protein' will return both ligand and protein atom indices).
        - The keyword 'ligand' will find the residue 'LIG', 'UNL', 'UNK', or
          whatever is in 'ligand_resname'
        - The keyword 'pocket' will find the closest 6 residues to the ligand.
        - The keyword 'near' will require a following resname, with an optional integer, e.g.:
            'near ATP'
            'near ATP 5'
        - The keyword 'resname' will require a resname:
            'resname LEU'
    """
    if keyword_selection is None and resid_selection is None:
        raise ValueError("Must specify either keyword selection or resid_selection")
    result = []
    if keyword_selection:
        tokens = [t for t in keyword_selection.split(" ") if t]
        allowed_keywords = list(resnames_by_keyword.keys()) + [
            "pocket",
            "near",
            "resname",
            "noh",
            "nosolvent",
        ]
        while len(tokens) > 0:
            keyword = tokens.pop(0)
            if keyword not in allowed_keywords:
                raise ValueError(f"Keyword {keyword} not in {allowed_keywords}")
            i_atoms = []
            if keyword in resnames_by_keyword:
                i_atoms = select_resnames(pmd, get_resnames(keyword))
            elif keyword == "pocket":
                i_atoms = select_residue_contacts(pmd, get_resnames("ligand"))
            elif keyword == "near":
                if len(tokens) < 1:
                    raise ValueError("keyword near requires a resname argument")
                lig_resname = tokens.pop(0)
                args = [pmd, [lig_resname]]
                if len(tokens) and tokens[0].isdigit():
                    args.append(int(tokens.pop(0)))
                i_atoms = select_residue_contacts(*args)
            elif keyword == "resname":
                if len(tokens) < 1:
                    raise ValueError("keyword res requires an argument")
                resname = tokens.pop(0)
                i_atoms = select_resnames(pmd, [resname])
                if not len(i_atoms):
                    logger.warning(
                        f"Warning: no atoms were found for resname={resname}"
                    )
            elif keyword == "noh":
                raise ValueError(
                    f"Deprecated 'noh' in '{expr}'; use 'not {{amber @/H}}"
                )
            elif keyword == "nosolvent":
                raise ValueError(
                    f"Deprecated 'nosolvent' in '{expr}'; use 'not {{solvent}}"
                )
            result.extend(i_atoms)
    return py_.uniq(result)
