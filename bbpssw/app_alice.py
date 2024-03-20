from bbpssw import bbpssw_protocol_alice
from netqasm.sdk import EPRSocket
from netqasm.sdk.external import NetQASMConnection, Socket

def main(app_config=None):

    # Create a socket for classical communication
    socket = Socket("alice", "bob")

    # Create a EPR socket for entanglement generation
    epr_socket = EPRSocket("bob")

    # Initialize Alice's NetQASM connection
    alice = NetQASMConnection(app_name = app_config.app_name, epr_sockets = [epr_socket])
      
    # Create Alice's context, initialize EPR pairs inside it and call Alice's BBPSSW method. Finally, print out whether or not Alice successfully created an EPR Pair with Bob.
    with alice:
        # Initialize EPR pairs
    	epr1, epr2 = epr_socket.create(number=2)

        # Call BBPSSW method
    	success = bbpssw_protocol_alice(epr1, epr2, alice, socket)

    #print("Alice successfully created an EPR pair with Bob:", success)


if __name__ == "__main__":
    main()
