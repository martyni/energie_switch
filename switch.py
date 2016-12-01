import json
def ensure_file_exists(name):
   try:
      with open(name,'r') as _file:
         pass
   except:
      with open(name, 'w') as _file:
         _file.write("0")

def switch_on(switch):
   print switch, "on"
   switch_write_state(switch, 1)
   return json.dumps({ switch : True })

def switch_off(switch):
   print switch, "off"
   switch_write_state(switch, 0) 
   return json.dumps({ switch : False })

def switch_current_state(switch):
   switch = str(switch)
   with open(switch, "r") as s:
      return s.read()

def switch_write_state(switch, state):
   with open(switch,"w") as s:
      s.write(str(state))
      return state

def update_switch(switch):
   current_state = switch_current_state(switch)
   if "0" in current_state:
      return switch_on(switch)
   else:
      return switch_off(switch)

def return_switches(switches):
   return json.dumps({ switch : switch_current_state(switch) for switch in range(switches)})
