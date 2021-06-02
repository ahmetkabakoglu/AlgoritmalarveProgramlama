import classes

# Processors
islemci = {}
islemci[1] = classes.Processor("INTEL", "Core i9", "10940X", "3,3", 9093, 1)
islemci[2] = classes.Processor("INTEL", "Core i7", "10700K", "3.8", 4167, 2)
islemci[3] = classes.Processor("INTEL", "Core i5", "10600K", "4.10", 2854, 3)
islemci[4] = classes.Processor("INTEL", "Core i9", "10850K", "3.60", 4493, 4)
islemci[5] = classes.Processor("AMD", "RYZEN 9", "5950X", "3.4", 9047, 5)
islemci[6] = classes.Processor("AMD", "RYZEN 7", "5800X", "3.8", 4884, 6)
islemci[7] = classes.Processor("AMD", "RYZEN 9", "3950X", "3.5", 8076, 7)
islemci[8] = classes.Processor("AMD", "RYZEN 7", "3700X", "3.6", 3156, 8)

islemciler = []

for key in islemci:
    islemciler.append(islemci[key])

# Motherboards
anakart ={}
anakart[1] = classes.Motherboard("GIGABYTE", "B450 AORUS", "Elite V2", "3200", "DDR4", 1024, 1)
anakart[2] = classes.Motherboard("ASUS ROG", "MAXIMUS XIII", "EXTREME Z590", "5333", "DDR4", 9829, 2)
anakart[3] = classes.Motherboard("MSI", "TRX40", "PRO 10G", "4666", "DDR4", 6067, 3)
anakart[4] = classes.Motherboard("ASUS PRIME", "TRX40", "PRO S", "4666", "DDR4", 5185, 4)
anakart[5] = classes.Motherboard("GIGABYTE", "Z490 AORUS", "XTREME", "5000", "DDR4", 8393, 5)
anakart[6] = classes.Motherboard("GIGABYTE", "X570 AORUS", "ULTRA", "4400", "DDR4", 3209, 6)
anakart[7] = classes.Motherboard("ASUS ROG", "STRIX", "B550-E GAMING", "4600", "DDR4", 2663, 7)
anakart[8] = classes.Motherboard("MSI", "MPG X570", "GAMING", "4400", "DDR4", 2198, 8)

anakartlar = []

for key in anakart:
    anakartlar.append(anakart[key])

# Memories
ram ={}
ram[1] = classes.Memory("GSKILL", "Ripjaws V", "3200", "256", "DDR4", 15524, 1)
ram[2] = classes.Memory("CORSAIR", "Dominator Platinum", "4000", "16", "DDR4", 3778, 2)
ram[3] = classes.Memory("SILICON POWER", "XPOWER Turbine", "3200", "32", "DDR4", 2271, 3)
ram[4] = classes.Memory("HYPERX", "Predator", "3000", "32", "DDR4", 2086, 4)
ram[5] = classes.Memory("PATRIOT", "Viper Steel", "3200", "32", "DDR4", 1861, 5)
ram[6] = classes.Memory("THERMALTAKE", "TOUGHRAM", "3600", "16", "DDR4", 1225, 6)
ram[7] = classes.Memory("CORSAIR", "Vengeance LPX", "4000", "16", "DDR4", 1994, 7)
ram[8] = classes.Memory("HYPERX", "Predator", "3200", "16", "DDR4", 1113, 8)

rams = []

for key in ram:
    rams.append(ram[key])

# Computer Cases
kasa = {}
kasa[1] = classes.ComputerCase("RAMPAGE", "REDSKY", "700", 1093, 1)
kasa[2] = classes.ComputerCase("COOLER MASTER", "MasterCase H500", "750", 1831, 2)
kasa[3] = classes.ComputerCase("POWERBOOST", "X58RGB", "650", 975, 3)
kasa[4] = classes.ComputerCase("GAMEBOOSTER", "GB-PE05B", "600", 794, 4)
kasa[5] = classes.ComputerCase("THERMALTAKE", "Versa T25", "650", 1119, 5)
kasa[6] = classes.ComputerCase("POWER BOOST", "VK-P1900B", "500", 627, 6)
kasa[7] = classes.ComputerCase("THERMALTAKE", "H330", "650", 1015, 7)
kasa[8] = classes.ComputerCase("GAMEBOOSTER", "GB-G5180B", "600", 760, 8)

kasalar = []

for key in kasa:
    kasalar.append(kasa[key])

# Graphic Cards
ekrankarti = {}
ekrankarti[1] = classes.GraphicCard("SAPPHIRE", "RX 550", "4", "GDDR5", "128", 2106, 1)
ekrankarti[2] = classes.GraphicCard("MSI GeForce", "GT 1030", "2", "GDDR5", "64", 1014, 2)
ekrankarti[3] = classes.GraphicCard("MSI GeForce", "N730-4GD3V2", "4", "GDDR3", "128", 858, 3)
ekrankarti[4] = classes.GraphicCard("MSI GeForce", "N730-2GD3V2", "2", "DDR3", "128", 762, 4)
ekrankarti[5] = classes.GraphicCard("MSI GeForce", "GT 710 2GD3H", "2", "DDR3", "64", 607, 5)
ekrankarti[6] = classes.GraphicCard("SAPPHIRE", "RX 560", "4", "GDDR5", "128", 2499, 6)
ekrankarti[7] = classes.GraphicCard("MSI GEFORCE", "RTX 2060", "6", "GDDR6", "192", 6978, 7)
ekrankarti[8] = classes.GraphicCard("ASUS GeForce", "RTX 3060", "12", "GDDR6", "192", 9704, 8)

ekrankartlari = []

for key in ekrankarti:
    ekrankartlari.append(ekrankarti[key])

# Hard Disk Drives
HDD = {}
HDD[1] = classes.HDD("WD", "Blue", "1", "64", "7200", "3.5", 410, 1)
HDD[2] = classes.HDD("SEAGATE", "Barracuda", "1", "64", "7200", "3.5", 420, 2)
HDD[3] = classes.HDD("SEAGATE", "Skyhawk", "1", "64", "5900", "3.5", 566, 3)
HDD[4] = classes.HDD("WD", "Purple", "1", "64MB", "5400", "3.5", 574, 4)
HDD[5] = classes.HDD("SEAGATE", "Barracuda", "1", "256", "7200", "3.5", 585, 5)
HDD[6] = classes.HDD("SEAGATE", "Ironwolf", "1", "64", "5900", "3.5", 688, 6)
HDD[7] = classes.HDD("WD", "Ultrastar", "6", "256", "7200", "3.5", 3032, 7)
HDD[8] = classes.HDD("SEAGATE", "Ironwolf", "8", "256", "7200", "3.5", 3643, 8)

HDDs = []

for key in HDD:
    HDDs.append(HDD[key])

# Solid State Drives
SSD = {}
SSD[1] = classes.SSD("KINGSTON", "UV500", "120", "520", "320", "M.2", 245, 1)
SSD[2] = classes.SSD("PATRIOT", "P210", "256", "500", "400", "2.5", 320, 2)
SSD[3] = classes.SSD("SANDISK", "Ultra", "250", "2400", "950", "M.2", 367, 3)
SSD[4] = classes.SSD("SEAGATE", "Barracuda", "250", "560", "540", "2.5", 400, 4)
SSD[5] = classes.SSD("SAMSUNG", "EVO Plus", "250", "3500", "2300", "M.2", 635, 5)
SSD[6] = classes.SSD("SILICON POWER", "P34A60", "516", "2200", "1600", "M.2", 705, 6)
SSD[7] = classes.SSD("SAMSUNG", "PRO", "512", "3500", "2300", "M.2", 1838, 7)
SSD[8] = classes.SSD("CORSAIR", "MP510", "960", "3480", "3000", "M.2", 1870, 8)

SSDs = []

for key in SSD:
    SSDs.append(SSD[key])

# Monitors
monitor = {}
monitor[1] = classes.Monitor("PowerBoost", "M2390VH", "23.8", "75", "1", "FHD", 850, 1)
monitor[2] = classes.Monitor("PHILIPS", "241E1SCA-01", "24", "75", "4", "FHD", 1250, 2)
monitor[3] = classes.Monitor("MSI", "PRO MP271", "27", "75", "5", "FHD", 1545, 3)
monitor[4] = classes.Monitor("AOC", "C24G1", "24", "144", "1", "FHD", 1781, 4)
monitor[5] = classes.Monitor("ASUS", "VX279HG", "27", "75", "1", "FHD", 2077, 5)
monitor[6] = classes.Monitor("LG", "27GN750-B", "27", "240", "1", "FHD", 2660, 6)
monitor[7] = classes.Monitor("LG", "32UN880-B", "31.5", "60", "5", "UHD", 6894, 7)
monitor[8] = classes.Monitor("Gigabyte", "AORUS FI27Q-X", "27", "240", "0,3", "QHD", 8282, 8)

monitors = []

for key in monitor:
    monitors.append(monitor[key])

# Keyboards
keyboard = {}

keyboard[1] = classes.Keyboard("Philips", "SPK8401B", "Mekanik", "Cyan", "Türkçe", 205, 1)
keyboard[2] = classes.Keyboard("GameBooster", "G9 Blade", "RGB Mekanik", "Blue", "Türkçe", 367, 2)
keyboard[3] = classes.Keyboard("Rampage", "KB-R97", "RGB Mekanik", "Blue", "Türkçe", 500, 3)
keyboard[4] = classes.Keyboard("AOC", "GK500", "RGB Mekanik", "Red", "Türkçe", 520, 4)
keyboard[5] = classes.Keyboard("Cooler Master", "CK530", "RGB Mekanik", "Red", "Türkçe", 620, 5)
keyboard[6] = classes.Keyboard("Razer", "BlackWidow", "RGB Mekanik", "Green Switch", "Türkçe", 817, 6)
keyboard[7] = classes.Keyboard("ASUS ROG", "Strix Scope", "RGB Mekanik", "Red", "Türkçe", 920, 7)
keyboard[8] = classes.Keyboard("Razer", "Huntsman", "RGB", "Purple", "İngilizce", 978, 8)

keyboards = []

for key in keyboard:
    keyboards.append(keyboard[key])

# Mouses
mouse = {}
mouse[1] = classes.Mouse("Lenovo", "Legion M200", "RGB", 80, 1)
mouse[2] = classes.Mouse("GameBooster", "M626", "RGB", 121, 2)
mouse[3] = classes.Mouse("AOC", "GM200DREE", "RGB", 142, 3)
mouse[4] = classes.Mouse("Thermaltake", "Neros", "RGB", 179, 4)
mouse[5] = classes.Mouse("Logitech", "G300S", "RGB", 193, 5)
mouse[6] = classes.Mouse("Corsair", "Ironclaw", "RGB Kablosuz", 439, 6)
mouse[7] = classes.Mouse("HyperX", "Pulsefire Surge", "RGB", 569, 7)
mouse[8] = classes.Mouse("Logitech", "G603", "Kablosuz", 771, 8)

mouses = []
for key in mouse:
    mouses.append(mouse[key])

# Notebooks

notebook = {}
notebook[1] = classes.Notebook("MONSTER", "Abra A5", "V16.6.5", "Intel Comet Lake Core i5-10200H",
                       "Nvidia GTX1650TI 4GB GDDR6", "15.6", "FHD", "120Hz", "8GB (1x8GB) DDR4 2933MHz",
                       "250GB M.2 SSD Sata 3", "Free-Dos", 7699, 1)
notebook[2] = classes.Notebook("MONSTER", "Abra A5", "V15.8", "Intel i7-10750H", "Nvidia GTX1650TI 4GB GDDR6", "15.6", "FHD",
                       "120Hz", "8GB (1x8GB) DDR4 2933MHz", "250GB WD BLUE SN550 M.2 SSD", "Free-Dos", 8899, 2)
notebook[3] = classes.Notebook("MONSTER", "Tulpar T5", "V20.2", "Intel i7-10870H", "Nvidia RTX3060 Max-Performance 6GB GDDR6",
                       "15.6", "QHD", "165Hz", "16GB (2x8GB) DDR4 2933MHz", "500GB CRUCIAL P2 PCIe M.2", "Free-Dos",
                       14599, 3)
notebook[4] = classes.Notebook("MONSTER", "Abra A7", "V12.4.3", "Intel i5-10200H", "Nvidia GTX1650TI 4GB GDDR6", "17,3", "FHD",
                       "144Hz", "8GB (1x8GB) DDR4 2933MHz", "500GB CRUCIAL P2 PCIe M.2", "Windows 10 Home SL", 9399, 4)

notebook[5] = classes.Notebook("MONSTER", "Tulpar T7", "V22.1", "Intel i7-10870H", "Nvidia RTX3060 Max-Performance 6GB GDDR6",
                       "17,3", "QHD", "165Hz", "16GB (2x8GB) DDR4 2933MHz", "500GB CRUCIAL P2 PCIe M.2", "Free-Dos",
                       15199, 5)
notebook[6] = classes.Notebook("MONSTER", "Tulpar T7", "V21.4", "Intel i7-10875H", "Nvidia RTX2080 SUPER Max-Q 8GB GDDR6",
                       "17.3", "FHD", "240Hz", "16GB (2x8GB) DDR4 2933MHz", "500GB CRUCIAL P2 PCIe M.2",
                       "Windows 10 Home SL", 21599, 6)
notebook[7] = classes.Notebook("MONSTER", "Markut M7", "V4.1", "Intel i9-10980HK", "Nvidia Quadro RTX 3000 6GB GDDR6 192-Bit",
                       "17,3", "FHD", "144Hz", "32GB (2x16GB) DDR4 3200MHz", "1TB Intel 665P M.2 SSD", "Windows 10 Pro",
                       26699, 7)
notebook[8] = classes.Notebook("MONSTER", "Semruk S7", "V7.2", "Intel i7-10700K", "Nvidia RTX2080 SUPER 8GB GDDR6 256 Bit",
                       "17.3", "FHD", "240Hz", "32GB (2x16GB) DDR4 3200MHz", "500GB CRUCIAL P2 PCIe M.2",
                       "Windows 10 Pro", 31699, 8)

notebooks = []


for key in notebook:
    notebooks.append(notebook[key])