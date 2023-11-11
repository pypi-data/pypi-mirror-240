import argparse
import os
from sage_lib import DFTPartition, SurfaceStatesGenerator, VacuumStatesGenerator  # Importing necessary classes

def generate_xyz_from_outcar(path, verbose=False):
    """
    Generate an XYZ file from a VASP OUTCAR file.

    Parameters:
    - path (str): Path to the VASP OUTCAR file.
    - verbose (bool): If True, prints additional information.
    """
    absolute_path = os.path.abspath(path)  # Convert to absolute path
    DP = DFTPartition(absolute_path)
    DP.readVASPFolder(v=verbose)
    DP.export_configXYZ()
    
def generate_vacancy(path, verbose=False):
    """
    Generate configurations with vacancies.

    Parameters:
    - path (str): Path to the VASP files directory.
    - verbose (bool): If True, prints additional information.
    """
    absolute_path = os.path.abspath(path)  # Convert to absolute path
    DP = DFTPartition(absolute_path)
    DP.readVASPFolder(v=verbose)
    DP.generateDFTVariants('Vacancy', [1])
    DP.exportVaspPartition()

def generate_disassemble_surface(path, steps=5, final_distance=5.0, atoms_to_remove=None, verbose=False):
    """
    Generate configurations for disassembling the surface.

    Parameters:
    - path (str): Path to the VASP files directory.
    - steps (int): Number of steps in the disassembly process.
    - final_distance (float): Final distance between layers or atoms.
    - atoms_to_remove (int or None): Specific number of atoms to remove.
    - verbose (bool): If True, prints additional information.
    """
    absolute_path = os.path.abspath(path)  # Convert to absolute path
    SSG = SurfaceStatesGenerator(absolute_path)
    SSG.readVASPFolder(v=verbose)
    SSG.generate_disassemble_surface(steps=steps, final_distance=final_distance, atoms_to_remove=atoms_to_remove)
    SSG.exportVaspPartition()

def generate_dimers(path=None, labels:list=None, steps:int=10, vacuum:float=18.0, verbose=False):
    """
    Generate configurations for dimer search.

    Parameters:
    - path (str): Path to the VASP files directory (optional if labels are provided).
    - labels (list of str): List of atom labels (optional if path is provided).
    - steps (int): Number of steps in the dimer search.
    - vacuum (int): Specific vacuum distance.
    - verbose (bool): If True, prints additional information.
    """
    
    
    if path is not None: 
        absolute_path = os.path.abspath(path)  # Convert to absolute path
        VSG = VacuumStatesGenerator(path)
        VSG.readVASPFolder(v=False)
    else:
        path='.'
        absolute_path = os.path.abspath(path)  # Convert to absolute path
        VSG = VacuumStatesGenerator(path)


    if labels is not None: 
        VSG.generate_dimers(AtomLabels=labels, steps=steps )
    else: 
        VSG.generate_dimers(steps=steps )
    VSG.export_configXYZ()
    VSG.exportVaspPartition()

def main():
    parser = argparse.ArgumentParser(description='Tool for theoretical calculations in quantum mechanics and molecular dynamics.')
    subparsers = parser.add_subparsers(dest='command', help='Available sub-commands')

    # Sub-command to generate vacancy directory
    parser_vacancy = subparsers.add_parser('vacancy', help='Generate vacancy.')
    parser_vacancy.add_argument('--path', type=str, required=True, help='Path to the VASP files directory')   
    parser_vacancy.add_argument('--verbose', action='store_true', help='Display additional information')
    
    # Sub-command to generate XYZ file from an OUTCAR directory
    parser_xyz = subparsers.add_parser('xyz', help='Generate an XYZ file from an OUTCAR directory.')
    parser_xyz.add_argument('--path', type=str, required=True, help='Path to the OUTCAR directory')
    parser_xyz.add_argument('--verbose', action='store_true', help='Display additional information')
    parser_xyz.add_argument('--subfolders', action='store_true', help='Read all subfolders')

    # Sub-command to generate configurations for disassembling the surface
    parser_disassemble = subparsers.add_parser('disassemble', help='Generate configurations for disassembling the surface.')
    parser_disassemble.add_argument('--path', type=str, required=True, help='Path to the VASP files directory')
    parser_disassemble.add_argument('--steps', type=int, default=5, help='Number of steps in disassembly (default: 5)')
    parser_disassemble.add_argument('--final_distance', type=float, default=5.0, help='Final distance between layers or atoms (default: 5.0)')
    parser_disassemble.add_argument('--atoms_to_remove', type=int, help='Specific number of atoms to remove')
    parser_disassemble.add_argument('--verbose', action='store_true', help='Display additional information')

    # Sub-comando para generar configuraciones para la búsqueda de dimeros
    parser_dimer = subparsers.add_parser('dimer', help='Generate configurations for dimer search.')
    group = parser_dimer.add_mutually_exclusive_group(required=True)
    group.add_argument('--path', type=str, help='Path to the VASP files directory')
    group.add_argument('--labels', nargs='+', help='List of atom labels for dimer search')
    parser_dimer.add_argument('--steps', type=int, default=10, help='Number of steps in the dimer search (default: 10)')
    parser_dimer.add_argument('--vacuum', type=int, default=18, help='Specific vacuum distance (default: 18)')
    parser_dimer.add_argument('--verbose', action='store_true', help='Display additional information')


    args = parser.parse_args()

    # Handle execution based on the specified sub-command
    if   args.command == 'xyz':
        generate_xyz_from_outcar(args.path, verbose=args.verbose)
    elif args.command == 'vacancy':
        generate_vacancy(args.path, verbose=args.verbose)
    elif args.command == 'disassemble':
        generate_disassemble_surface(args.path, steps=args.steps, final_distance=args.final_distance, atoms_to_remove=args.atoms_to_remove, verbose=args.verbose)
    elif args.command == 'dimer':
        generate_dimers(path=args.path, labels=args.labels, steps=args.steps, vacuum=args.vacuum, verbose=args.verbose)

if __name__ == '__main__':
    main()