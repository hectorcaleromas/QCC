from epl import epl_protocol_alice
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket, get_qubit_state
from numpy import pi



def main(app_config=None):

   

    # Create a socket for classical communication
    socket = Socket("alice", "bob")
    

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("bob")
    

    # Initialize Alice's NetQASM connection
    alice = NetQASMConnection(
        app_name=app_config.app_name,
        epr_sockets=[epr_socket]
        )


    # Create Alice's context, initialize EPR pairs inside it and call Alice's EPL method. Finally, print out whether or not Alice successfully created an EPR Pair with Bob.
    with alice:
        #initialize EPR pair
        epr_1, epr_2 = epr_socket.create(number=2)

        epr_1.X()
        epr_1.rot_Z(angle=pi/4)
        epr_2.X()
        epr_2.rot_Z(angle=pi/4)
        
        success= epl_protocol_alice(epr_1, epr_2, alice, socket)
        #if succ:
           # print("Alice succesfully created entanglement with Bob")

if __name__ == "__main__":
    main()
