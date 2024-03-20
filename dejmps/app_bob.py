from dejmps import dejmps_protocol_bob
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state
from netqasm.sdk.toolbox.sim_states import qubit_from, to_dm, get_fidelity
import netsquid as ns
from netsquid.qubits import operators

def main(app_config=None):
    
    # Create a socket for classical communication
    socket = Socket("bob", "alice")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("alice")

    # Initialize Bob's NetQASM connection
    bob = NetQASMConnection(app_name=app_config.app_name, epr_sockets=[epr_socket])
    
    # Create Bob's context, initialize EPR pairs inside it and call Bob's DEJMPS method. Finally, print out whether or not Bob successfully created an EPR Pair with Alice.
    with bob:
        epr1, epr2 = epr_socket.recv(number=2)
        success = dejmps_protocol_bob(epr1, epr2, bob, socket)
    	
        # Compute Fidelity
        q1,q2 = ns.qubits.create_qubits(2)
        ns.qubits.operate(q1, operators.H)
        ns.qubits.operate([q1, q2], operators.CNOT)
        dm_exp = get_qubit_state(epr1, reduced_dm=False)
        fidelity = get_fidelity(q1, dm_exp)
        
    if success:
    	print(fidelity)
    return 
        
   

if __name__ == "__main__":
    main()
