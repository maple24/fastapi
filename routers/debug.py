from utils.CRQM.CRQM import CRQMClient

cRQM = CRQMClient("ets1szh", "estbangbangde4", "Zeekr", "https://rb-alm-20-p.de.bosch.com")
cRQM.login()


cRQM.disconnect()