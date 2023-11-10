from quantumsymmetry.core import *
from openfermion import QubitOperator, FermionOperator, jordan_wigner, utils, linalg
from qiskit import opflow, quantum_info
from qiskit_nature.operators.second_quantization import FermionicOp
from qiskit_nature.converters.second_quantization import QubitConverter
from qiskit.circuit.quantumcircuit import QuantumCircuit
from pyscf import gto, scf, symm, ao2mo
from itertools import combinations
from qiskit_nature.operators.second_quantization import FermionicOp

def make_CAS_encoding(atom, basis, charge = 0, spin = 0, irrep = None, CAS = None, natural_orbitals = False, active_mo = None):
    """Makes an array that stores information about that encoding and which can be passed on to other functions

    Args:
        atom (str): molecular geometry (for example the hydrogen molecule in the optimized configuration is 'H 0 0 0; H 0.7414 0 0').
        basis (str): molecular chemistry basis (for example the minimal basis is 'sto-3g').
        charge (int, optional): total charge of the molecule. Defaults to 0.
        spin (int, optional): number of unpaired electrons 2S (the difference between the number of alpha and beta electrons). Defaults to 0.
        irrep (str, optional): irreducible representation of interest. Defaults to the irreducible representation of the molecular ground state (as long as charge and spin have been set correctly).

    Returns:
        tuple: the encoding object
    """
    mol = gto.Mole()
    mol.atom = atom
    mol.symmetry = True
    mol.basis = basis
    mol.charge = charge
    mol.spin = spin
    mol.verbose = 0
    mol.build()
    if mol.groupname == 'Dooh' or mol.groupname == 'SO3':
        mol.symmetry = 'D2h'
        mol.build()
    if mol.groupname == 'Coov':
        mol.symmetry = 'C2v'
        mol.build()
    mf = scf.RHF(mol)
    mf.kernel()

    if natural_orbitals == True:
        mymp = mp.UMP2(mf).run(verbose = 0)
        noons, natorbs = mcscf.addons.make_natural_orbitals(mymp)
        mf.mo_coeff = natorbs

    label_orb_symm = symm.label_orb_symm(mol, mol.irrep_name, mol.symm_orb, mf.mo_coeff)
    character_table, conj_labels, irrep_labels, conj_descriptions = get_character_table(mol.groupname)
    if irrep == None:
        irrep =  find_ground_state_irrep(label_orb_symm, mf.mo_occ, character_table, irrep_labels)

    if CAS != None:
        number_of_MO = len(label_orb_symm)
        if active_mo == None:
            frozen_core_qubits = list(range(mol.nelectron - CAS[0]))
            active_space_qubits = list(range(mol.nelectron - CAS[0], mol.nelectron - CAS[0] + 2*CAS[1]))
            virtual_qubits = list(range(len(frozen_core_qubits) + len(active_space_qubits), 2*number_of_MO))      

        else:
            frozen_core_qubits = []
            active_space_qubits = []
            virtual_qubits = []
            for mo in active_mo:
                active_space_qubits.append(2*mo - 2)
                active_space_qubits.append(2*mo - 1)
            count = 0
            for mo in range(2*number_of_MO):
                if mo not in active_space_qubits:
                    if count != mol.nelectron - CAS[0]:
                        frozen_core_qubits.append(mo)
                        count += 1
                    else:
                        virtual_qubits.append(mo)
        CAS_qubits = [frozen_core_qubits, active_space_qubits, virtual_qubits]
    else:
        CAS_qubits = None
    
    symmetry_generator_labels, symmetry_generators_strings, target_qubits, symmetry_generators, signs, descriptions = find_symmetry_generators(mol, irrep, label_orb_symm, CAS_qubits)
    tableau, tableau_signs = make_clifford_tableau(symmetry_generators, signs, target_qubits)    

    if CAS != None:
        for x in target_qubits[::-1]:
            for y in range(len(frozen_core_qubits)):
                if x < frozen_core_qubits[y]:
                    frozen_core_qubits[y] -= 1
            for y in range(len(virtual_qubits)):
                if x < virtual_qubits[y]:
                    virtual_qubits[y] -= 1

        CAS_target_qubits = frozen_core_qubits + virtual_qubits
        number_of_qubits = len(frozen_core_qubits + active_space_qubits + virtual_qubits)
        CAS_tableau = (np.ones([2*number_of_qubits, 2*number_of_qubits], dtype= int) - 2*np.identity(2*number_of_qubits, dtype= int)).tolist()
        CAS_tableau_signs = [1]*2*number_of_qubits
        for x in frozen_core_qubits:
            CAS_tableau_signs[x] = -1

        encoding = (tableau, tableau_signs, target_qubits)    
        CAS_encoding = (CAS_tableau, CAS_tableau_signs, CAS_target_qubits)    
        return encoding, CAS_encoding

def apply_encoding(operator, encoding, output_format = 'openfermion'):
    """Applies the encoding to a fermionic operator object or a qubit operator (in the Jordan Wigner basis) object

    Args:
        operator (Qiskit FermionicOp or OpenFermion QubitOperator or OpenFermion FermionOperator): a fermionic operator object or a qubit operator (in the Jordan Wigner basis) object in OpenFermion
        encoding (tuple): an encoding object

    Returns:
        openfermion.QubitOperator: the corresponding qubit operator in the encoding
    """
    if type(operator) == FermionOperator:
        operator = jordan_wigner(operator)
    if type(operator) == FermionicOp:
        operator = QubitConverter(JordanWignerMapper()).convert(operator)
    if type(operator) == opflow.PauliSumOp:
        operator = PauliSumOp_to_QubitOperator(operator)
    if len(encoding) == 3:
        tableau, tableau_signs, target_qubits = encoding
        CAS_target_qubits = []
    elif len(encoding) == 2:
        tableau, tableau_signs, target_qubits = encoding[0]
        CAS_tableau, CAS_tableau_signs, CAS_target_qubits = encoding[1]
    transformed_operator = apply_Clifford_tableau(operator, tableau, tableau_signs)
    operator = simplify_QubitOperator(project_operator(transformed_operator, target_qubits))
    if len(encoding) == 2:
        operator = apply_Clifford_tableau(operator, CAS_tableau, CAS_tableau_signs)
        operator = simplify_QubitOperator(project_operator(operator, CAS_target_qubits))
    if output_format == 'openfermion':
        return operator
    elif output_format == 'qiskit':
        operator = QubitOperator_to_PauliSumOp(operator, num_qubits= len(tableau)//2 - len(target_qubits) - len(CAS_target_qubits))
        return operator

def apply_encoding_mapper(operator, suppress_none=True):
    apply_encoding(operator = operator, encoding = SymmetryAdaptedEncoding_encoding, output_format = 'qiskit')

def convert_encoding(operators, suppress_none=True, check_commutes=False, num_particles=None, sector_locator=None):
    if type(operators) == FermionicOp:
        operator = operators
        output = 0
        operator = fix_qubit_order_convention(operator)
        encoded_operator = apply_encoding(operator = operator, encoding = SymmetryAdaptedEncoding_encoding, output_format = 'qiskit')
        if type(encoded_operator) != int and type(encoded_operator) != None:
            output = encoded_operator
    elif type(operators) == list:
        output = list()
        for operator in operators:
            operator = fix_qubit_order_convention(operator)
            encoded_operator = apply_encoding(operator = operator, encoding = SymmetryAdaptedEncoding_encoding, output_format = 'qiskit')
            if type(encoded_operator) != int and type(encoded_operator) != None:
                output.append(encoded_operator)
    return output

def transform(driver, operators):
    output1 = driver
    output2 = list()
    if operators == None:
        return output1, None
    for operator in operators:
        operator = fix_qubit_order_convention(operator)
        encoded_operator = apply_encoding(operator = operator, encoding = SymmetryAdaptedEncoding_encoding, output_format = 'qiskit')
        if type(encoded_operator) != int and type(encoded_operator) != None:
            output2.append(encoded_operator)
    return output1, output2

def fix_qubit_order_convention(input):
    output = 0
    input.display_format="dense"
    N = input.register_length
    input_list = input.to_list()
    for x in range(len(input_list)):
        output_label = str()
        input_label = input_list[x][0]
        input_label = input_label[::-1]
        for j in range(N//2):
            output_label += input_label[j]
            output_label += input_label[N//2 + j]
        output += FermionicOp([(output_label[::-1], input_list[x][1])], display_format='dense')
    return output
    
def SymmetryAdaptedEncodingQubitConverter(encoding):
    global SymmetryAdaptedEncoding_encoding
    SymmetryAdaptedEncoding_encoding = encoding
    qubit_transformation = QubitConverter(apply_encoding_mapper)
    qubit_transformation.convert_match = convert_encoding
    qubit_transformation.mapper.map = apply_encoding_mapper
    qubit_transformation.convert = convert_encoding
    return qubit_transformation

def HartreeFockCircuit(encoding, atom, basis, charge = 0, spin = 0, irrep = None, CAS = None, natural_orbitals = False):
    mol = gto.Mole()
    mol.atom = atom
    mol.symmetry = True
    mol.basis = basis
    mol.charge = charge
    mol.spin = spin
    mol.verbose = 0
    mol.build()
    if mol.groupname == 'Dooh' or mol.groupname == 'SO3':
        mol.symmetry = 'D2h'
        mol.build()
    if mol.groupname == 'Coov':
        mol.symmetry = 'C2v'
        mol.build()
    mf = scf.RHF(mol)
    mf.kernel()

    if natural_orbitals == True:
        mymp = mp.UMP2(mf).run(verbose = 0)
        noons, natorbs = mcscf.addons.make_natural_orbitals(mymp)
        mf.mo_coeff = natorbs

    b = HartreeFock_ket(mf.mo_occ)

    if len(encoding) == 2:
        encoding, CAS_encoding = encoding
    else:
        CAS_encoding == None
    
    tableau, tableau_signs, target_qubits = encoding
    tableau = np.array(tableau)
    tableau_signs = np.array(tableau_signs)
    n = len(tableau)//2
    ZZ_block = (-tableau[:n, :n] + 1)//2
    sign_vector = (-tableau_signs[:n]+ 1)//2
    string_b = f'{b:0{n}b}'
    b_list = list(string_b)[::-1]
    for i in range(len(b_list)):
        b_list[i] = int(b_list[i])
    c_list = np.matmul(ZZ_block, b_list + sign_vector)[::-1] % 2
    string_c = ''.join(str(x) for x in c_list)
    target_qubits.sort(reverse = True)
    for qubit in target_qubits:
        l = len(string_c)
        string_c = string_c[:l - qubit - 1] + string_c[l - qubit:]

    if CAS_encoding != None:
        CAS_tableau, CAS_tableau_signs, CAS_target_qubits = CAS_encoding
        print(CAS_target_qubits)
        CAS_target_qubits.sort(reverse = True)
        for qubit in CAS_target_qubits:
            l = len(string_c)
            string_c = string_c[:l - qubit - 1] + string_c[l - qubit:]

    output = QuantumCircuit(len(string_c))
    for i, bit in enumerate(string_c[::-1]):
        if bit == '1':
            output.x(i)
    return output

def swap_plus_and_minuses(input):
    output = str()
    for s in input:
        if s == '+':
            output += '-'
        elif s == '-':
            output += '+'
        else:
            output += s
    return output

def make_fermionic_excitation_ops(reference_state):
    number_of_qubits = len(reference_state)
    occ = []
    unocc = []
    reference_state = list(reference_state)
    reference_state.reverse()

    #get occupations
    for i, x in enumerate(reference_state):
        if x == '0':
            unocc.append(i)
        if x == '1':
            occ.append(i)
    print(unocc)
    print(occ)

    #singles
    operators_s = []
    for perm_plus in list(combinations(occ, 1)):
        for perm_minus in list(combinations(unocc, 1)):
            if len(set(perm_plus).union(set(perm_minus))) == 2:
                operator = ['I']*number_of_qubits
                for i in perm_plus:
                    operator[i] = '+'
                for i in perm_minus:
                    operator[i] = '-'
                operator = ''.join(operator)
                operators_s.append(operator)

    #doubles
    operators_d = []
    for perm_plus in list(combinations(occ, 2)):
        for perm_minus in list(combinations(unocc, 2)):
            operator = ['I']*number_of_qubits
            for i in perm_plus:
                operator[i] = '+'
            for i in perm_minus:
                operator[i] = '-'
            operator = ''.join(operator)
            operators_d.append(operator)
    
    #create fermionic operators
    operators2 = []
    for operator in operators_s:
        excitation = FermionicOp([(operator, 1j), (swap_plus_and_minuses(operator), 1j)], register_length = number_of_qubits, display_format='dense')
        if excitation not in operators2:
            operators2.append(excitation)

    for operator in operators_d:
        excitation = FermionicOp([(operator, 1j), (swap_plus_and_minuses(operator), -1j)], register_length = number_of_qubits, display_format='dense')
        if excitation not in operators2:
            operators2.append(excitation)

    return operators2

def make_excitation_ops(reference_state, encoding):
    operators = []
    excitations = make_fermionic_excitation_ops(reference_state)
    for excitation in excitations:
        op = apply_encoding(encoding = encoding, operator = excitation, output_format = 'qiskit')
        operators.append(op)
    return operators
