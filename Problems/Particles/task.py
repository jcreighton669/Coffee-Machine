spin = input()
electric_charge = input()

if electric_charge == "0":
    if spin == "0":
        print("Higgs boson Boson")
    elif spin == "1":
        print("Photon Boson")
    elif spin == "1/2":
        print("Muon Lepton")

if spin == "1/2":
    if electric_charge == "-1/3":
        print("Strange Quark")
    elif electric_charge == "2/3":
        print("Charm Quark")
    elif electric_charge == "-1":
        print("Electron Lepton")
