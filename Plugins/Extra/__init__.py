from . import inQuest, InternetDB, ThreatFox, MalwareBazaar

extra_dict = {
  0: {
    "name": "Exit to Main Menu",
    "run": None
  }, 
  1: {
    "name": "inQuest Search",
    "run": lambda: inQuest.inQuest().run()
  },
  2: {
    "name": 'InternetDB Search',
    "run": lambda: InternetDB.InternetDB().run()
  },
  3: {
    "name": "ThreatFox Search",
    "run": lambda: ThreatFox.ThreatFox().run()
  },
  4: {
    "name": "Malware Bazaar Search",
    "run": lambda: MalwareBazaar.MalwareBazaar().run()
  }
}

def extraMenu():
  print("\n ------------------------------ ")
  print("           E X T R A        ")
  print(" ------------------------------ ")
  print(" What would you like to do? \n")
  for item in extra_dict.keys():
    if item == 0:
      continue
    print(f" OPTION {item}: {extra_dict[item]['name']}")
  print("\n OPTION 0: Exit to Main Menu")
  val = int(input("\n>> "))
  if val not in extra_dict:
    print("Invalid value specified")
    extraMenu()
  elif val == 0:
    return
  else:
    extra_dict[val]['run']()