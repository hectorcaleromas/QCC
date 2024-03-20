from netqasm.sdk.classical_communication.message import StructuredMessage
import math


def dejmps_protocol_alice(q1, q2, alice, socket):
    """
    Implements Alice's side of the DEJMPS distillation protocol.
    This function should perform the gates and measurements for DEJMPS using
    qubits q1 and q2, then send the measurement outcome to Bob and determine
    if the distillation was successful.
    
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :param alice: Alice's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
    a = dejmps_gates_and_measurement_alice(q1, q2)
    alice.flush()
	
    # Write below the code to send measurement result to Bob, receive measurement result from Bob and check if protocol was successful
    a=int(a)
    socket.send_structured(StructuredMessage("Alice's measurement is: ", (a)))
    b = socket.recv_structured().payload
    
    return a == b


def dejmps_gates_and_measurement_alice(q1, q2):
    """
    Performs the gates and measurements for Alice's side of the DEJMPS protocol
    :param q1: Alice's qubit from the first entangled pair
    :param q2: Alice's qubit from the second entangled pair
    :return: Integer 0/1 indicating Alice's measurement outcome
    """
    q1.rot_X(angle=math.pi/2)
    q2.rot_X(angle=math.pi/2)
    q1.cnot(q2) 
    return q2.measure()


def dejmps_protocol_bob(q1, q2, bob, socket):
    """
    Implements Bob's side of the DEJMPS distillation protocol.
    This function should perform the gates and measurements for DEJMPS using
    qubits q1 and q2, then send the measurement outcome to Alice and determine
    if the distillation was successful.
    
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :param bob: Bob's NetQASMConnection
    :param socket: Alice's classical communication socket to Bob
    :return: True/False indicating if protocol was successful
    """
    b = dejmps_gates_and_measurement_bob(q1, q2)
    bob.flush()

    # Write below the code to send measurement result to Alice, receive measurement result from Alice and check if protocol was successful
    b = int(b)
    socket.send_structured(StructuredMessage("Bob's measurement is:", (b)))
    a = socket.recv_structured().payload
    
    return a == b

def dejmps_gates_and_measurement_bob(q1, q2):
    """
    Performs the gates and measurements for Bob's side of the DEJMPS protocol
    :param q1: Bob's qubit from the first entangled pair
    :param q2: Bob's qubit from the second entangled pair
    :return: Integer 0/1 indicating Bob's measurement outcome
    """
    q1.rot_X(angle=-math.pi/2)
    q2.rot_X(angle=-math.pi/2)
    q1.cnot(q2) 
    return q2.measure()
