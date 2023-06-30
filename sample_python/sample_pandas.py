import pandas as pd

wip_df = pd.read_excel('eDashboardPlus_MESAgingReport_c27.xlsx',
                       sheet_name='MESAgingReport', engine='openpyxl')
wip_df = wip_df[(wip_df['Step Aging'] == 0) & (
    wip_df['Result'] != 'Fail') & (wip_df['Result'] != 'Abort')]
wip_df['Assembly'] = wip_df['AssemblyNumber']+' / '+wip_df['Revision']
wip_df = wip_df.drop(columns=['Wip_ID', 'Built Time', 'Step Aging', 'Birth Aging',
                     'Birth DateTime', 'Current Step DateTime', 'AssemblyNumber', 'Revision'])


def fair_type(df_row):
    if 'BOXBUILD' in df_row['Route']:
        return 'BOXBUILD'
    else:
        return 'PCBA'


def fair_name(df_row):
    if len(df_row['SerialNumber']) <= 5:
        return 'NA'
    else:
        return hcm_solaredge_fair_name(df_row)


def hcm_solaredge_fair_name(df_row):
    assNum = df_row['Assembly']
    if df_row['FAIR_Type'] == 'BOXBUILD':
        if assNum[0] == 'P':
            modeP = assNum.split('-')[-1][:2]
            if modeP == "NA":
                if df_row['Step'] in 'Birth PCA_FNI BoxBuild PLV Screw1_AAC Screw2_AAC Screw QC HIPOT AAC':
                    return 'AAC OPT'
                elif df_row['Step'] in 'LABELLINK BoxBuild FNI SE_OBA BoxBuild QC':
                    return 'PACKING OPT'
                else:
                    return 'NA'
            elif modeP == "NM" and df_row['Step'] in 'LABELLINK FINALLINK BoxBuild FNI PACKOUT OBA':
                return 'PACKING OPT'
            else:
                return 'NA'
        elif assNum[0] == 'S':
            if '-FAN-' in assNum:
                return 'NA'
            else:
                return 'PACKING INV'
        elif assNum[0] == 'A':
            if assNum[1] == 'U' and df_row['Step'] in 'BB INV PLV03 Board Link PCAVerify2 EOL-TEST SI':
                return 'Unify Inverter'
            elif assNum[1] == 'S':
                if assNum[2] == '9':
                    if df_row['Step'] in 'PCA_FNI BoxBuild PLV LINK_ASSY Auto Screw QC_Assy1 HIPOT PPT 1ST Weighing':
                        return 'Casing OPT Mn'
                    elif df_row['Step'] in 'Potting_Link potting check EOL-TEST POTTING 2nd Weighing':
                        return 'Potting OPT Mn'
                    else:
                        return 'NA'
                else:
                    if assNum.split('-')[1][0] == 'D':
                        if df_row['Step'] in 'Birth BB DCD PLV01 Link DCD_QC_Rework FNI PACKOUT':
                            return 'DCD'
                    elif '-RG' in assNum:
                        return 'NA'
                    else:
                        if df_row['Step'] in 'Birth BB INV PLV01 Link HS Screw 1 Rework HS Screw 2 Rework BB INV PLV02 PCAVerify':
                            return 'Pre-Asy INV'
                        elif df_row['Step'] in 'Lock MB Mainboard Screw Base Locking Holder Choke Locking Cable Assy 1 Cable Assy 2 Lock PB PCBA Link PCAVerify1 TLA QC Rework DC Cables':
                            return 'Casing INV'
                        else:
                            return 'NA'
            else:
                return 'NA'
        else:
            return 'NA'
    elif df_row['FAIR_Type'] == 'PCBA':
        if df_row['Step'] in 'Birth SMT_TOP SMT_BOT SCR_TOP SCR_BOT AOI_TSI AOI_BSI Washing-SMT HIPOT SPI1 SPI2':
            return 'SMT'
        elif df_row['Step'] in 'DepanelM02 LINK_WASHING_IN Wash_Inspection LINK_WAVEPALLET SOED_XRAY SOED_MI01 SOED_MI02':
            return 'MI'
        elif df_row['Step'] in 'ICT program test Manual Insert Final Test SOED_Glue01 SOED_Glue02':
            return 'TEST'
        elif df_row['Step'] in 'Coating Inspection QC_COATING_T COAT_T_REWORK Manual Soldering PCA_FNI':
            return 'COATING'
        else:
            return 'NA'
    else:
        return 'NA'


wip_df['FAIR_Type'] = wip_df.apply(fair_type, axis=1)
wip_df['FAIR_Name'] = wip_df.apply(fair_name, axis=1)
wip_df = wip_df[wip_df['FAIR_Name'] != 'NA']

# def final_group(df_row):
#   return '|'.join([df_row['FAIR_Type'], df_row['FAIR_Name'], df_row['BatchID'], df_row['Assembly']])
# wip_df['Group']=wip_df.apply(final_group, axis=1)
group_wip_df = wip_df.groupby(
    by=['FAIR_Type', 'FAIR_Name', 'BatchID', 'Assembly']).size().reset_index()
# pivot_wip_df = wip_df.pivot(index=['FAIR_Type', 'FAIR_Name', 'BatchID', 'Assembly'], values='SerialNumber')
# print(pivot_wip_df)
with pd.ExcelWriter('res.xlsx', mode='w', engine='openpyxl') as writer:
    group_wip_df.to_excel(writer, sheet_name='Sheet1')

# print(wip_df[(wip_df['FAIR_Name']=='NA') & (wip_df['FAIR_Type']!='PCBA')])

print('Done')
