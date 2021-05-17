import classes

# Processors

islemci1 = classes.Processor("INTEL", "Core i9", "10940X", "3,3", 9093, 1)
islemci2 = classes.Processor("INTEL", "Core i7", "10700K", "3.8", 4167, 2)
islemci3 = classes.Processor("INTEL", "Core i5", "10600K", "4.10", 2854, 3)
islemci4 = classes.Processor("INTEL", "Core i9", "10850K", "3.60", 4493, 4)
islemci5 = classes.Processor("AMD", "RYZEN 9", "5950X", "3.4", 9047, 5)
islemci6 = classes.Processor("AMD", "RYZEN 7", "5800X", "3.8", 4884, 6)
islemci7 = classes.Processor("AMD", "RYZEN 9", "3950X", "3.5", 8076, 7)
islemci8 = classes.Processor("AMD", "RYZEN 7", "3700X", "3.6", 3156, 8)

# Motherboards

anakart1 = classes.Motherboard("GIGABYTE", "B450 AORUS", "Elite V2", "3200", "DDR4", 1024, 1)
anakart2 = classes.Motherboard("ASUS ROG", "MAXIMUS XIII", "EXTREME Z590", "5333", "DDR4", 9829, 2)
anakart3 = classes.Motherboard("MSI", "TRX40", "PRO 10G", "4666", "DDR4", 6067, 3)
anakart4 = classes.Motherboard("ASUS PRIME", "TRX40", "PRO S", "4666", "DDR4", 5185, 4)
anakart5 = classes.Motherboard("GIGABYTE", "Z490 AORUS", "XTREME", "5000", "DDR4", 8393, 5)
anakart6 = classes.Motherboard("GIGABYTE", "X570 AORUS", "ULTRA", "4400", "DDR4", 3209, 6)
anakart7 = classes.Motherboard("ASUS ROG", "STRIX", "B550-E GAMING", "4600", "DDR4", 2663, 7)
anakart8 = classes.Motherboard("MSI", "MPG X570", "GAMING", "4400", "DDR4", 2198, 8)

# Memories

ram1 = classes.Memory("GSKILL", "Ripjaws V", "3200", "256", "DDR4", 15524, 1)
ram2 = classes.Memory("CORSAIR", "Dominator Platinum", "4000", "16", "DDR4", 3778, 2)
ram3 = classes.Memory("SILICON POWER", "XPOWER Turbine", "3200", "32", "DDR4", 2271, 3)
ram4 = classes.Memory("HYPERX", "Predator", "3000", "32", "DDR4", 2086, 4)
ram5 = classes.Memory("PATRIOT", "Viper Steel", "3200", "32", "DDR4", 1861, 5)
ram6 = classes.Memory("THERMALTAKE", "TOUGHRAM", "3600", "16", "DDR4", 1225, 6)
ram7 = classes.Memory("CORSAIR", "Vengeance LPX", "4000", "16", "DDR4", 1994, 7)
ram8 = classes.Memory("HYPERX", "Predator", "3200", "16", "DDR4", 1113, 8)

#Computer Cases

kasa1 = classes.ComputerCase("RAMPAGE", "REDSKY", "700", 1093, 1)
kasa2 = classes.ComputerCase("COOLER MASTER", "MasterCase H500", "750", 1831, 2)
kasa3 = classes.ComputerCase("POWERBOOST", "X58RGB", "650", 975, 3)
kasa4 = classes.ComputerCase("GAMEBOOSTER", "GB-PE05B", "600", 794, 4)
kasa5 = classes.ComputerCase("THERMALTAKE", "Versa T25", "650", 1119, 5)
kasa6 = classes.ComputerCase("POWER BOOST", "VK-P1900B", "500", 627, 6)
kasa7 = classes.ComputerCase("THERMALTAKE", "H330", "650", 1015, 7)
kasa8 = classes.ComputerCase("GAMEBOOSTER", "GB-G5180B", "600", 760, 8)

#Graphic Cards

ekrankarti1 = classes.GraphicCard("SAPPHIRE", "RX 550", "4", "GDDR5", "128", 2106, 1)
ekrankarti2 = classes.GraphicCard("MSI GeForce", "GT 1030", "2", "GDDR5", "64", 1014, 2)
ekrankarti3 = classes.GraphicCard("MSI GeForce", "N730-4GD3V2", "4", "GDDR3", "128", 858, 3)
ekrankarti4 = classes.GraphicCard("MSI GeForce", "N730-2GD3V2", "2", "DDR3", "128", 762, 4)
ekrankarti5 = classes.GraphicCard("MSI GeForce", "GT 710 2GD3H", "2", "DDR3", "64", 607, 5)
ekrankarti6 = classes.GraphicCard("SAPPHIRE", "RX 560", "4", "GDDR5", "128", 2499, 6)
ekrankarti7 = classes.GraphicCard("MSI GEFORCE", "RTX 2060", "6", "GDDR6", "192", 6978, 7)
ekrankarti8 = classes.GraphicCard("ASUS GeForce", "RTX 3060", "12", "GDDR6", "192", 9704, 8)

#Hard Disk Drives

HDD1 = classes.HDD("WD", "Blue", "1", "64", "7200", "3.5", 410, 1)
HDD2 = classes.HDD("SEAGATE", "Barracuda", "1", "64", "7200", "3.5", 420, 2)
HDD3 = classes.HDD("SEAGATE", "Skyhawk", "1", "64", "5900", "3.5", 566, 3)
HDD4 = classes.HDD("WD", "Purple", "1", "64MB", "5400", "3.5", 574, 4)
HDD5 = classes.HDD("SEAGATE", "Barracuda", "1", "256", "7200", "3.5", 585, 5)
HDD6 = classes.HDD("SEAGATE", "Ironwolf", "1", "64", "5900", "3.5", 688, 6)
HDD7 = classes.HDD("WD", "Ultrastar", "6", "256", "7200", "3.5", 3032, 7)
HDD8 = classes.HDD("SEAGATE", "Ironwolf", "8", "256", "7200", "3.5", 3643, 8)

#Solid State Drives

SSD1 = classes.SSD("KINGSTON", "UV500", "120", "520", "320", "M.2", 245, 1)
SSD2 = classes.SSD("PATRIOT", "P210", "256", "500", "400", "2.5", 320, 2)
SSD3 = classes.SSD("SANDISK", "Ultra", "250", "2400", "950", "M.2", 367, 3)
SSD4 = classes.SSD("SEAGATE", "Barracuda", "250", "560", "540", "2.5", 400, 4)
SSD5 = classes.SSD("SAMSUNG", "EVO Plus", "250", "3500", "2300", "M.2", 635, 5)
SSD6 = classes.SSD("SILICON POWER", "P34A60", "516", "2200", "1600", "M.2", 705, 6)
SSD7 = classes.SSD("SAMSUNG", "PRO", "512", "3500", "2300", "M.2", 1838, 7)
SSD8 = classes.SSD("CORSAIR", "MP510", "960", "3480", "3000", "M.2", 1870, 8)

#Monitors

monitor1 = classes.Monitor("PowerBoost", "M2390VH", "23.8", "75", "1", "FHD", 850, 1)
monitor2 = classes.Monitor("PHILIPS", "241E1SCA-01", "24", "75", "4", "FHD", 1250, 2)
monitor3 = classes.Monitor("MSI", "PRO MP271", "27", "75", "5", "FHD", 1545, 3)
monitor4 = classes.Monitor("AOC", "C24G1", "24", "144", "1", "FHD", 1781, 4)
monitor5 = classes.Monitor("ASUS", "VX279HG", "27", "75", "1", "FHD", 2077, 5)
monitor6 = classes.Monitor("LG", "27GN750-B", "27", "240", "1", "FHD", 2660, 6)
monitor7 = classes.Monitor("LG", "32UN880-B", "31.5", "60", "5", "UHD", 6894, 7)
monitor8 = classes.Monitor("Gigabyte", "AORUS FI27Q-X", "27", "240", "0,3", "QHD", 8282, 8)

#Keyboards

klavye1 = classes.Keyboard("Philips", "SPK8401B", "Mekanik", "Cyan", "Türkçe", 205, 1)
klavye2 = classes.Keyboard("GameBooster", "G9 Blade", "RGB Mekanik", "Blue", "Türkçe", 367, 2)
klavye3 = classes.Keyboard("Rampage", "KB-R97", "RGB Mekanik", "Blue", "Türkçe", 500, 3)
klavye4 = classes.Keyboard("AOC", "GK500", "RGB Mekanik", "Red", "Türkçe", 520, 4)
klavye5 = classes.Keyboard("Cooler Master", "CK530", "RGB Mekanik", "Red", "Türkçe", 620, 5)
klavye6 = classes.Keyboard("Razer", "BlackWidow", "RGB Mekanik", "Green Switch", "Türkçe", 817, 6)
klavye7 = classes.Keyboard("ASUS ROG", "Strix Scope", "RGB Mekanik", "Red", "Türkçe", 920, 7)
klavye8 = classes.Keyboard("Razer", "Huntsman", "RGB", "Purple", "İngilizce", 978, 8)

#Mouses

mouse1 = classes.Mouse("Lenovo", "Legion M200", "RGB", 80, 1)
mouse2 = classes.Mouse("GameBooster", "M626", "RGB", 121, 2)
mouse3 = classes.Mouse("AOC", "GM200DREE", "RGB", 142, 3)
mouse4 = classes.Mouse("Thermaltake", "Neros", "RGB", 179, 4)
mouse5 = classes.Mouse("Logitech", "G300S", "RGB", 193, 5)
mouse6 = classes.Mouse("Corsair", "Ironclaw", "RGB Kablosuz", 439, 6)
mouse7 = classes.Mouse("HyperX", "Pulsefire Surge", "RGB", 569, 7)
mouse8 = classes.Mouse("Logitech", "G603", "Kablosuz", 771, 8)