from bbpssw.bbpssw import bbpssw_protocol_alice, bbpssw_protocol_bob
from dejmps.dejmps import dejmps_protocol_alice, dejmps_protocol_bob
from epl.epl import epl_protocol_alice, epl_protocol_bob
import subprocess

def test():
    subprocess.run(["./script.sh"])


if __name__=="__main__":
    test()
