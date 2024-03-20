from epl import epl_protocol_bob
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


    # Initialize Alice's NetQASM connection
    bob = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
        )
    

    # Create Alice's context, initialize EPR pairs inside it and call Alice's EPL method. Finally, print out whether or not Alice successfully created an EPR Pair with Bob.
    with bob:
    
        #initialize EPR pair
        epr_1, epr_2 = epr_socket.recv(number=2)
        success = epl_protocol_bob(epr_1, epr_2, bob, socket)
        #print("Success: ", success)

        #Compute Fidelity 
        q1, q2 = ns.qubits.create_qubits(2)
        ns.qubits.operate(q1, operators.H)
        ns.qubits.operate([q1, q2], operators.CNOT)
        ns.qubits.operate(q2, operators.X)
        original = q1

        #compute density matrix
        dm_b = get_qubit_state(epr_1, reduced_dm=False)
        dm = original.qstate.dm
        fidelity = get_fidelity(q1, dm_b)
        #print("Fidelity: ", fidelity)
        if success:
        	print(fidelity)
        return 
        


if __name__ == "__main__":
    main()
