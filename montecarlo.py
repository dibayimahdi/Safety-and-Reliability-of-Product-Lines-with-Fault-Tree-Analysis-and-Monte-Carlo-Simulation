import numpy as np


# Define the failure rate for each basic event (e.g., per year)
human_error = 0.00003
Mechanical_failure = 0.00003
Link_disconnection = 0.000003
Electromagnetic_effet = 0.000001
Controller_failure = 0.000003
Sensor_failure = 0.000003
Actuator_failure = 0.000003
Switch_failure = 0.000003
Operating_system_failure = 0.00001
Installation_failure = 0.000001 
Incompatible_software = 0.000001 
Routing_addressing_failure = 0.000001 
Topology_failure = 0.000001 
Synchronization_failure = 0.000001 
Open_circuit = 0.000002
Short_circuit = 0.000002 
power_supply = 0.000003 # Power supply failure rate




# Define the number of simulations
num_simulations = 10000
top_event_count = 0
mu=0.0000144
sigma=0.000006
s=0
# Run simulations
for _ in range(num_simulations):
    # Simulate UPS failure
    ups_failure = (sigma * np.random.randn() + mu) 
     #print(ups_failure)
    
    
    # Check if the top event (power disruption) occurs
   # system_failure_rate = 0.000086 + (power_supply * ups_failure)
    print(ups_failure)
    s=s+ups_failure
# Probability of top event occurrence
ups_failure = s / num_simulations
print(f"Probability of UPS failure V3: {ups_failure}")
