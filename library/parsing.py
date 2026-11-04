import csv
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


def parse_and_gate_csv(file_path, output_path):
    gates = {}
    with open(file_path, newline='') as csv_file:
        for row in csv.reader(csv_file):
            if not row or row[0].strip() == 'part':
                continue
            if row[0].strip() != 'AND':
                continue

            gate_name = row[1].strip()
            gate = gates.setdefault(gate_name, {
                'name': gate_name,
                'type': 'AND',
            })

            param = row[3].strip() if len(row) > 3 else ''
            value = row[4].strip() if len(row) > 4 else ''

            if param in {'ymax', 'ymin', 'K1', 'K2', 'n'}:
                gate[param] = value
            elif param == 'equation':
                gate['equation'] = value

    ordered_columns = ['name', 'type', 'ymax', 'ymin', 'K1', 'K2', 'n', 'equation']
    result = pd.DataFrame(gates.values(), columns=ordered_columns)
    result.to_csv(output_path, index=False)


def parse_csv(file_path, output_path):
    if file_path.endswith('gates_Eco3C3G3T3.csv'):
        parse_and_gate_csv(file_path, output_path)
        return

    curr = pd.read_csv(file_path)
    curr = curr.drop(columns=["color", "promoter","promoterDNA","ribozyme","ribozymeDNA","rbs","rbsDNA","cds","cdsDNA","terminator","terminatorDNA"], errors='ignore')
    curr.to_csv(output_path, index=False) # index=False prevents writing an unnamed column

# def plot_gate_equation(parsed_csv):
#     # f = pd.read_csv(parsed_csv)
#     # rows = len(f) #how many gates needs to be plotted 

#     # figure, axes = plt.subplots(rows, 1, figsize=(2, 5*rows))


parsed_csv_files = []
#reading first library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1.csv', 'parsed_Eco1C1G1T1.csv')


#reading second library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco1C1G1T1b.csv', 'parsed_Eco1C1G1T1b.csv')

#reading third library file 
curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco2C2G2T2.csv')
curr = curr.drop( columns=["promoter", "promoterDNA","sgRNA","sgRNADNA","terminator","terminatorDNA", ])
curr.to_csv('parsed_Eco2C2G2T2.csv', index_label=False)
# parsed_csv_files.append('parsed_Eco2C2G2T2.csv') the plots are NOT gates? but format is diff

#reading fourth library file - not sure what is going on here yet
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv')

#reading fifth library file - normalize the AND gate rows so each gate is one row, matching the rest of the parsed libraries.
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_Eco3C3G3T3.csv', 'parsed_Eco3C3G3T3.csv')
# parsed_csv_files.append('parsed_Eco3C3G3T3.csv')

#reading sixth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v1.csv', 'parsed_EcoCB1_v1.csv')
parsed_csv_files.append('parsed_EcoCB1_v1.csv')

#reading seventh library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1_v2.csv', 'parsed_EcoCB1_v2.csv')
parsed_csv_files.append('parsed_EcoCB1_v2.csv')

#reading eighth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoCB1.csv', 'parsed_EcoCB1.csv')
parsed_csv_files.append('parsed_EcoCB1.csv')

#reading ninth library file 
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_110215.csv', 'parsed_EcoJS4ib_110215.csv')
parsed_csv_files.append('parsed_EcoJS4ib_110215.csv')

#reading tenth library file
parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib_111015.csv', 'parsed_EcoJS4ib_111015.csv')
parsed_csv_files.append('parsed_EcoJS4ib_111015.csv')
#reading eleventh library file

parse_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/gates_EcoJS4ib.csv', 'parsed_EcoJS4ib.csv')
parsed_csv_files.append('parsed_EcoJS4ib.csv')

#reading twelfth library file - not sure what is going on here yet either 
#curr = pd.read_csv('/home/shrut/bioCircuitProject/testingCello/cello/resources/csv_gate_libraries/parts_LacI_TetR.csv')

#plotting csv files 

# for file in parsed_csv_files:
#     plot_gate_equation(file)