from netqasm.sdk import EPRSocket	
from netqasm.sdk.external import NetQASMConnection, Socket

def main(app_config=None):

	# Socket Initialisation
	socket=Socket("bob","alice")
	
	# EPR Socket
	epr_socket= EPRSocket("alice")
	
	# Initialisation
	bob = NetQASMConnection(
	app_name = app_config.app_name,
	epr_sockets =[epr_socket]
	) ##
	
	with bob:
	

		epr= epr_socket.recv()[0]
		m1, m2 = socket.recv_structured().payload
		# Corrections
		if m2==1:
			epr.X()
		if m1==1:
			epr.Z()

	# Check:
		result= epr.measure()
		bob.flush()
	
		print(result)
if __name__=="__main__":
	main()
	
