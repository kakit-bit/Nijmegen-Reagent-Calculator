# Class saves Patient Demographics into Profile Object
class Patient():
    def __init__(self, dilutions):
        self.dilutions = dilutions # Integer from 1-13

# User Input Error Check Functions
def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# Function to Check and Limit Samples Run
def get_workload():
    while True:
        workload_string = input("Number of Inhibitors to Run: ")
        # Check if Input is a Valid Number
        if not is_number(workload_string):
            print("Not a valid number")
            continue
        # Check if Input is Within Range
        workload = int(workload_string)
        if workload >= 10:
            print("Workload exceeds suggested limits")
            continue
        return workload

# Function to Obtain Dilutions with Error and Limitation Checking
def get_dilutions():
    while True:
        dilutions_string = input("Number of Dilutions: ")
        # Check if Input is a Valid Number
        if not is_number(dilutions_string):
            print("Not a valid number")
            continue
        # Check if Input is Within Range
        dilutions = int(dilutions_string)
        if dilutions not in range(1,14):
            print("Dilutions not within range")
            continue
        return dilutions

# Function Allows User to Input Patient Demographics
def get_patient():
    dilutions = get_dilutions()
    patient = Patient(dilutions)
    return patient

# Calculate BSA Needed for Each Patient and Controls
def bsa_resource(all_dilutions):
    # Controls Require 2 BSA
    bsa_total = 2 + all_dilutions
    # Convert to Vials Required
    bsa_needed = (bsa_total*200/1500)
    return round(bsa_needed, 2)

# Calculate PNP Needed for Each Patient and Controls
def pnp_resource(all_dilutions,num_samples):
    # Controls Require 4 PNP
    pnp_total = 4 + all_dilutions + num_samples
    # Convert to Vials Required
    pnp_needed = (pnp_total*200/1500)
    return round(pnp_needed, 2)

# Calculate Dilutions to Add or Subtract
def resource_adjustment(resource):
    difference = abs(resource - round(resource))
    adjustment = difference/(200/1500)
    return adjustment

if __name__ == '__main__':

    all_patients = []
    all_dilutions = 0

    # Get Number of Samples to Run
    num_samples = get_workload()
    for x in range(num_samples):
        patient = get_patient()
        all_patients.append(patient)
    # Tally Total Dilutions
    for patient in all_patients:
        all_dilutions += patient.dilutions

    # Tally BSA and PNP Totals
    bsa_required = bsa_resource(all_dilutions)
    pnp_required = pnp_resource(all_dilutions, num_samples)

    print("# of BSA Required: ", bsa_required)
    print("# of PNP Required: ", pnp_required)

    # Adjustments
    adjustment = round(resource_adjustment(pnp_required))
    if pnp_required < round(pnp_required):
        print("You can add", adjustment ,"more dilutions to use up ", round(pnp_required), " vials of PNP")
    elif pnp_required > round(pnp_required):
        print("Remove ", adjustment , "dilutions to thaw ", round(pnp_required), " vials of PNP")

    # Adjustments
    #pnp_adjust = round(resource_adjustment(pnp_required))
    #bsa_adjust = round(resource_adjustment(bsa_required))

    #if pnp_required < round(pnp_required):
    #    if (pnp_adjust > bsa_adjust):
    #        print("You can add", bsa_adjust, "more dilutions to use up ", round(pnp_required), " vials of PNP")
    #    elif (pnp_adjust < bsa_adjust):
    #        print("You can add", pnp_adjust, "more dilutions to use up ", round(pnp_required), " vials of PNP")
    #elif pnp_required > round(pnp_required):
    #    if (pnp_adjust > bsa_adjust):
    #        print("Remove ", bsa_adjust , "dilutions to thaw ", round(pnp_required), " vials of PNP")
    #    elif (pnp_adjust < bsa_adjust):
    #        print("Remove ", pnp_adjust , "dilutions to thaw ", round(pnp_required), " vials of PNP")