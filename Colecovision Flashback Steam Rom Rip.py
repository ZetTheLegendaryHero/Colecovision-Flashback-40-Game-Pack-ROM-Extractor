#!/usr/bin/env python

# Rips Roms from the Steam release of Colecovision Flashback

ROMS = [{'OFFSETS': [0x01740, 0x0573F]},
		{'OFFSETS': [0x05740, 0x0973F]},
		{'OFFSETS': [0x09740, 0x0D73F]},
		{'OFFSETS': [0x0D740, 0x1373F]},
		{'OFFSETS': [0x13740, 0x1773F]},
		{'OFFSETS': [0x17740, 0x1B73F]},
		{'OFFSETS': [0x1B740, 0x1F73F]},
		{'OFFSETS': [0x1F740, 0x2373F]},
		{'OFFSETS': [0x23740, 0x2773F]},
		{'OFFSETS': [0x27740, 0x2F73F]},
		{'OFFSETS': [0x2F740, 0x3373F]},
		{'OFFSETS': [0x33740, 0x3973F]},
		{'OFFSETS': [0x39740, 0x3D73F]},
		{'OFFSETS': [0x3D740, 0x4173F]},
		{'OFFSETS': [0x41740, 0x4573F]},
		{'OFFSETS': [0x45740, 0x4B73F]},
		{'OFFSETS': [0x4B740, 0x5173F]},
		{'OFFSETS': [0x51740, 0x5573F]},
		{'OFFSETS': [0x55740, 0x5973F]},
		{'OFFSETS': [0x59740, 0x6153F]},
		{'OFFSETS': [0x61540, 0x6553F]},
		{'OFFSETS': [0x65540, 0x6953F]},
		{'OFFSETS': [0x69540, 0x6D53F]},
		{'OFFSETS': [0x6D540, 0x7153F]},
		{'OFFSETS': [0x71540, 0x7553F]},
		{'OFFSETS': [0x75540, 0x7953F]},
		{'OFFSETS': [0x79540, 0x7D53F]},
		{'OFFSETS': [0x7D540, 0x8153F]},
		{'OFFSETS': [0x81540, 0x8753F]},
		{'OFFSETS': [0x87540, 0x8B53F]},
		{'OFFSETS': [0x8B540, 0x8F53F]},
		{'OFFSETS': [0x8F540, 0x9353F]},
		{'OFFSETS': [0x93540, 0x9753F]},
		{'OFFSETS': [0x97540, 0x9D53F]},
		{'OFFSETS': [0x9D540, 0xA153F]},
		{'OFFSETS': [0xA1540, 0xA553F]},
		{'OFFSETS': [0xA5540, 0xA953F]},
		{'OFFSETS': [0xA9540, 0xAF53F]},
		{'OFFSETS': [0xAF540, 0xB353F]},
		{'OFFSETS': [0xB3540, 0xB953F]}]

# Rom filenames
ROMFILE = [{'NAME': [str("AntarcticAdventure.cv")]},
		   {'NAME': [str("Aquattack.cv")]},
		   {'NAME': [str("BrainStrainers.cv")]},
		   {'NAME': [str("BumpnJump.cv")]},
		   {'NAME': [str("Choplifter.cv")]},
		   {'NAME': [str("CosmicAvenger.cv")]},
		   {'NAME': [str("Evolution.cv")]},
		   {'NAME': [str("Fathom.cv")]},
		   {'NAME': [str("FlipperSlipper.cv")]},
		   {'NAME': [str("FortuneBuilder.cv")]},
		   {'NAME': [str("FranticFreddy.cv")]},
		   {'NAME': [str("Frenzy.cv")]},
		   {'NAME': [str("GatewayToApshai.cv")]},
		   {'NAME': [str("GustBuster.cv")]},
		   {'NAME': [str("JumpmanJunior.cv")]},
		   {'NAME': [str("JungleHunt.cv")]},
		   {'NAME': [str("Miner2049er.cv")]},
		   {'NAME': [str("Moonsweeper.cv")]},
		   {'NAME': [str("MountainKing.cv")]},
		   {'NAME': [str("MsSpaceFury.cv")]},
		   {'NAME': [str("NovaBlast.cv")]},
		   {'NAME': [str("OilsWell.cv")]},
		   {'NAME': [str("OmegaRace.cv")]},
		   {'NAME': [str("PepperII.cv")]},
		   {'NAME': [str("QuintanaRoo.cv")]},
		   {'NAME': [str("Rolloverture.cv")]},
		   {'NAME': [str("SammyLightfoot.cv")]},
		   {'NAME': [str("SirLancelot.cv")]},
		   {'NAME': [str("Slurpy.cv")]},
		   {'NAME': [str("SpaceFury.cv")]},
		   {'NAME': [str("SpacePanic.cv")]},
		   {'NAME': [str("SquishemSam.cv")]},
		   {'NAME': [str("SuperCrossForce.cv")]},
		   {'NAME': [str("TheHeist.cv")]},
		   {'NAME': [str("Threshold.cv")]},
		   {'NAME': [str("TournamentTennis.cv")]},
		   {'NAME': [str("Venture.cv")]},
		   {'NAME': [str("WarRoom.cv")]},
		   {'NAME': [str("WingWar.cv")]},
           {'NAME': [str("Zaxxon.cv")]}]
		   
if __name__ == '__main__':
	f = open("AUTO", "rb")
	
	try:
		autofile = f.read()
	finally:
		f.close
	
	for i in range(0, 40):
		for section in ['OFFSETS']:
			if ROMS[i][section]:
				start = f.seek(ROMS[i][section][0], 0)
				end = f.seek(ROMS[i][section][1], 0)
				game = autofile[start:end]
		for section in ['NAME']:
			if ROMFILE[i][section]:
				romfilename = ROMFILE[i][section][0]
				filename = open(romfilename, "wb")
		try:
			filename.write(game)
		finally:
			filename.close()