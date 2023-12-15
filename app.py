from flask import Flask, request
import pandas as pd
from asana_app.asana_app import Asana
from energy_metering.electrical_energy import ElectricalUsage

app = Flask(__name__)

#
@app.route("/asana_func")
def asana_func():
    asana = Asana()
    return asana.asana_access_token()


@app.route("/electrical_usage_func", methods=['POST'])
def electrical_usage_func():
    electrical = request.get_json()

    # Substation Data
    ss_df = pd.DataFrame(electrical[0])

    # Plants Data
    plant1_df = pd.DataFrame(electrical[1])
    plant2_df = pd.DataFrame(electrical[2])
    plant3_df = pd.DataFrame(electrical[3])
    plant4_df = pd.DataFrame(electrical[4])

    # Pump House
    pmp_hse_df = pd.DataFrame(electrical[5])

    # Quality Assurance
    qa_df = pd.DataFrame(electrical[6])

    # Process Development
    pd_df = pd.DataFrame(electrical[7])

    # Manufacturing
    mfg_df = pd.DataFrame(electrical[8])

    # Administration
    admin_df = pd.DataFrame(electrical[9])

    # Conner
    conner_df = pd.DataFrame(electrical[10])

    # Distribution
    dist_df = pd.DataFrame(electrical[11])

    # Cafeteria
    cafe_old_df = pd.DataFrame(electrical[12])
    cafe_new_df = pd.DataFrame(electrical[13])

    # Aspex
    aspex_df = pd.DataFrame(electrical[14])

    # West Data Center
    wdc_df = pd.DataFrame(electrical[15])

    # Towers
    towerA_df = pd.DataFrame(electrical[16])
    towerB_df = pd.DataFrame(electrical[17])
    towerC_df = pd.DataFrame(electrical[18])

    # Yards and Grounds
    yg_df = pd.DataFrame(electrical[19])

    ss_df = ss_df.reindex(['Month', 'East 12.5kVAC Meter', 'West 12.5kVAC Meter', 'Total Month'], axis=1)
    plant1_df = plant1_df.reindex(
        ['Month', 'Bus A 480VAC Meter', 'Bus B 480VAC Meter', 'Bus C 480VAC Meter', 'Total kWh', 'Total Percent'],
        axis=1)
    plant2_df = plant2_df.reindex(
        ['Month', 'Bus North 480VAC Meter', 'Bus South 480VAC Meter', 'Bus 4160VAC Meter', 'Total kWh',
         'Total Percent'], axis=1)
    plant3_df = plant3_df.reindex(
        ['Month', 'SC East 4160VAC Meter', 'SC West 4160VAC Meter', 'SqD West 480VAC Meter', 'SqD East 480VAC Meter',
         'Total kWh', 'Total Percent'], axis=1)
    plant4_df = plant4_df.reindex(
        ['Month', 'Bus A 480VAC Meter', 'Bus B 480VAC Meter', 'Bus A 4160VAC Meter', 'Bus B 4160VAC Meter', 'Total kWh',
         'Total Percent'], axis=1)
    pmp_hse_df = pmp_hse_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    qa_df = qa_df.reindex(['Month', 'Bus A 208VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    pd_df = pd_df.reindex(['Month', 'Bus A 480VAC Meter', 'Bus B 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    mfg_df = mfg_df.reindex(
        ['Month', 'Courtyard 480VAC Meter', 'Line 20 480VAC Meter', 'Northeast 480VAC Meter', 'Southwest 480VAC Meter',
         'Total kWh', 'Total Percent'], axis=1)
    admin_df = admin_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    conner_df = conner_df.reindex(
        ['Month', 'Conner D 480VAC Meter', 'Conner F 480VAC Meter', 'Conner ABC 480VAC Meter', 'Total kWh',
         'Total Percent'], axis=1)
    dist_df = dist_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    cafe_old_df = cafe_old_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    cafe_new_df = cafe_new_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    aspex_df = aspex_df.reindex(
        ['Month', 'Bus A 480VAC Meter', 'SqD East 480VAC Meter', 'SqD West 480VAC Meter', 'Total kWh', 'Total Percent'],
        axis=1)
    wdc_df = wdc_df.reindex(['Month', 'Bus East 480VAC Meter', 'Bus West 480VAC Meter', 'Total kWh', 'Total Percent'],
                            axis=1)
    towerA_df = towerA_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    towerB_df = towerB_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    towerC_df = towerC_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)
    yg_df = yg_df.reindex(['Month', 'Bus A 480VAC Meter', 'Total kWh', 'Total Percent'], axis=1)

    with pd.ExcelWriter('electrical_usage.xlsx') as writer:
        ss_df.to_excel(writer, sheet_name='Substation', startrow=0, index=False)
        plant1_df.to_excel(writer, sheet_name='Plant 1', startrow=0, index=False)
        plant2_df.to_excel(writer, sheet_name='Plant 2', startrow=0, index=False)
        plant3_df.to_excel(writer, sheet_name='Plant 3', startrow=0, index=False)
        plant4_df.to_excel(writer, sheet_name='Plant 4', startrow=0, index=False)
        pmp_hse_df.to_excel(writer, sheet_name='Pump House', startrow=0, index=False)
        qa_df.to_excel(writer, sheet_name='Quality Assurance', startrow=0, index=False)
        pd_df.to_excel(writer, sheet_name='Process Development', startrow=0, index=False)
        mfg_df.to_excel(writer, sheet_name='Manufacturing', startrow=0, index=False)
        admin_df.to_excel(writer, sheet_name='Administration', startrow=0, index=False)
        conner_df.to_excel(writer, sheet_name='Conner', startrow=0, index=False)
        dist_df.to_excel(writer, sheet_name='Distribution', startrow=0, index=False)
        cafe_old_df.to_excel(writer, sheet_name='Cafeteria Old', startrow=0, index=False)
        cafe_new_df.to_excel(writer, sheet_name='Cafeteria New', startrow=0, index=False)
        aspex_df.to_excel(writer, sheet_name='Aspex', startrow=0, index=False)
        wdc_df.to_excel(writer, sheet_name='West Data Center', startrow=0, index=False)
        towerA_df.to_excel(writer, sheet_name='Tower A', startrow=0, index=False)
        towerB_df.to_excel(writer, sheet_name='Tower B', startrow=0, index=False)
        towerC_df.to_excel(writer, sheet_name='Tower C', startrow=0, index=False)
        yg_df.to_excel(writer, sheet_name='Yards and Grounds', startrow=0, index=False)

    return "Received"


if __name__ == '__main__':
    app.run()
