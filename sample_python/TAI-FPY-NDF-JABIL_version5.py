


import os , shutil , glob
import re
import pandas as pd
import numpy as np
import sys
import datetime
import pyodbc
import xlwt
import xlrd


from datetime import datetime, timedelta
last10days = datetime.now()+ timedelta(days=-10)
last10days=last10days.strftime('%Y-%m-%d')


def total(row):
    if row['Process Loop']==1 and row['Test Loop']==1:
        return 1
    else:
        return 0


def first_fail(row):
    if row['Test Status']!='Pass' and row['Process Loop']==1 and row['Test Loop']==1:
        return 1
    else:
        return 0
    
def total_pass(row):
    if row['Test Status']=='Pass':
        return 1
    else:
        return 0
    
def total_ndf2(row):
    if row['Defect Text']=='NDF_DEBUG':
        return 1
    else:
        return 0


############read file excel sheet StationDefect#####################

#datalist = r"C://Users//2868690//Desktop//FPY//Data//StationDefect.xlsx"
datalist = r"C://Tai//Excel//StationDefect.xlsx"
rawdata = pd.read_excel(datalist , 'Station Defect')
rawdata = rawdata.rename(columns = {'Assembly No.' : 'Assembly No' })

tpulist = rawdata['Assembly No'].unique() # list of TPU owner, list out TEN tat ca cac PCBA

rawdata['Start Date Time org']=rawdata['Start Date Time'] # Tao them mot cot voi noi dung giong nhu COT Start Date Time
rawdata['Start Date Time']=rawdata['Start Date Time'].dt.strftime('%Y-%m-%d') # add columns DateMonthYear extract from columns TIMESTAMP, it will understood as string
rawdata=rawdata[rawdata['Start Date Time']>=last10days ]
rawdata['first_fail']=rawdata.apply(first_fail, axis=1) # call function fpy

rawdata['total_pass']=rawdata.apply(total_pass, axis=1) # call function fpy
rawdata['total_test']=rawdata.apply(total, axis=1) # call function fpy

rawdata['total_df2']=rawdata.apply(total_ndf2, axis=1) # call function fpy


# In[268]:


###################tinh Total test###################################
df_total_test_raw=rawdata
df_total_test= df_total_test_raw.groupby(['Family','Assembly No' ,'Start Date Time'])['total_test'].sum().reset_index(name = 'TOTAL_TEST') # group theo 'Family','Assembly No' ,'Start Date Time', sau do tinh TONG cot Total

################### End Total test###################################

########################tinh first fail#############################
df_first_fail_raw=rawdata
df_first_fail= df_first_fail_raw.groupby(['Family','Assembly No' ,'Start Date Time'])['first_fail'].sum().reset_index(name = 'FIRST_FAIL')

#######################  End first fail###############################

#####tinh First Pass ######################################
df_first_pass=pd.merge(df_total_test,df_first_fail, on=['Family','Assembly No' ,'Start Date Time'], how='left') #ghep 2 cai bang lai voi nhau
df_first_pass['FIRST_PASS']=df_first_pass['TOTAL_TEST']-df_first_pass['FIRST_FAIL']

#######################  End first_pass###############################

############tinh Total pass cuoi cung#################################
df_total_pass_raw=rawdata
df_total_pass=df_total_pass_raw[df_total_pass_raw['total_pass']==1]
df_total_pass=df_total_pass.sort_values(by=['Start Date Time org'])
df_total_pass = df_total_pass.drop_duplicates('Serial Number' , keep='last')
df_total_last_pass= df_total_pass.groupby(['Family','Assembly No' ,'Start Date Time'])['total_pass'].sum().reset_index(name = 'TOTAL_PASS')
#df_total_last_pass.to_excel( r'C:\Users\2868690\Desktop\FPY\Data\FPY JABIL.xlsx',sheet_name= 'total last_pass')

###################Tinh FPY    ###################
#df_first_pass['FPY']=round(df_first_pass['FIRST_PASS']/df_first_pass['TOTAL_TEST']*100,2)
#df_first_pass['FPY'] = df_total_ndf['FPY'].replace(np.nan, 0)# chuyen doi NaN thanh 0

##############################################

## Tinh NDF####
########Loc ra nhung serial co so 1######

df_first_fail_abort_SN_raw=df_first_fail_raw[df_first_fail_raw['first_fail']==1]
df_total_last_pass_SN_raw=df_total_pass[df_total_pass['total_pass']==1]

#### chi lay cot serial cua bang first fail de tin hanh vlookup####
df_first_fail_abort_SN=df_first_fail_abort_SN_raw[['Serial Number']]
df_first_fail_abort_SN['Repeat']=1 #gan repeat=1 cho tat ca serial number of first fail



### Ghep 2 table total last pass voi first fail###########
df_lastpass_firstfail=pd.merge(df_first_fail_abort_SN,df_total_last_pass_SN_raw, on='Serial Number', how='left')
#df_lastpass_firstfail.to_excel( r"C:\Users\2868690\Desktop\FPY\Data\Tai data.xlsx",sheet_name= 'df_total_pass2')

##### Loc nhung thang repeat=1 chung to nhung SN bi trung nhau, tinh NDF1#####
df_NDF1_raw=df_lastpass_firstfail[df_lastpass_firstfail['Repeat']==1]
df_NDF1= df_NDF1_raw.groupby(['Family','Assembly No','Start Date Time'])['Repeat'].sum().reset_index(name = 'NDF1')



df_NDF2_raw=rawdata[rawdata['total_df2']==1]
df_NDF2= df_NDF2_raw.groupby(['Family','Assembly No','Start Date Time'])['total_df2'].sum().reset_index(name = 'NDF2')



df_total_ndf=pd.merge(df_NDF1,df_NDF2, on=['Family','Assembly No','Start Date Time'], how='left')

df_total_ndf['NDF1'] = df_total_ndf['NDF1'].replace(np.nan, 0)# chuyen doi NaN thanh 0
df_total_ndf['NDF2'] = df_total_ndf['NDF2'].replace(np.nan, 0)# chuyen doi NaN thanh 0
df_total_ndf['TOTAL_NDF']=df_total_ndf['NDF1']+df_total_ndf['NDF2']
df_total_ndf

# Xuat bang de lam Report
#df_report=pd.merge(df_first_pass,df_total_ndf, on='Serial Number', how='left')
#df_report


# In[269]:


df_first_pass=pd.merge(df_first_pass,df_total_ndf, on=['Family','Assembly No' ,'Start Date Time'], how='left')
df_first_pass=df_first_pass.fillna(0) # chuyen doi NaN thanh 0
datelist = df_first_pass['Start Date Time'].unique() # list of TPU owner
###FPY#############
tpu_df_first_pass_temp=df_first_pass[df_first_pass['Start Date Time']=="DUCANH"]
for date in datelist: 
    tpu_df_first_pass= df_first_pass[df_first_pass['Start Date Time'] == date].reset_index(drop = True)
    tpu_df_first_pass=tpu_df_first_pass.append(tpu_df_first_pass.sum(numeric_only=True), ignore_index=True)
    tpu_df_first_pass['FPY']=round(tpu_df_first_pass['FIRST_PASS']/tpu_df_first_pass['TOTAL_TEST']*100,2)
    tpu_df_first_pass[['Family','Assembly No']]=tpu_df_first_pass[['Family','Assembly No']].replace(np.nan, "TOTAL") # chuyen doi NaN thanh 0
    #tpu_df_first_pass['Start Date Time']=tpu_df_first_pass['Start Date Time'].replace(np.nan, tpu_df_first_pass["Start Date Time"].shift(1)) # chuyen doi NaN thanh 0
    tpu_df_first_pass['Start Date Time']=tpu_df_first_pass['Start Date Time'].replace(np.nan, date) # chuyen doi NaN thanh 0
    tpu_df_first_pass_temp=pd.concat([tpu_df_first_pass_temp, tpu_df_first_pass]).reset_index(drop = True)
tpu_df_first_pass_temp

# Start Table of Yield Report in 7 days
df_summary=tpu_df_first_pass_temp
                                                                                                 
report = pd.pivot_table(df_summary , index = ['Family','Assembly No'] , values = ['FPY'] , columns = ['Start Date Time']) # pivot the tables and stored in report
report = report.reset_index() # reset the index of report data frame
report.columns = report.columns.droplevel(0) # drop level 0 of dataframe
report.columns.name = None # remove the columns name
cols = report.columns.tolist()
cols = ['Family'] + ['Assembly No']+cols[2:]
report.columns = cols
report.columns
report['GOAL']=97.25 # call function goal to add goal for each TPU
cols=report.columns.tolist() # prepare to swap column orders
cols=cols[0:2] + cols[-1:] + cols[2:-1] # swap column orders
report=report[cols] # save back the table with new column order to report
report1=report[report['Family']!='TOTAL']
report2=report[report['Family']=='TOTAL']
report_yield=pd.concat([report1, report2]).reset_index(drop = True)
report_yield

report_yield = report_yield.style.apply(lambda x: ["background-color: #00FF00" if (col >= 3 and (v >= x.iloc[2])) else "background-color: #FF0000" if (col >=3 and (v < x.iloc[2])) else '' for col , v in enumerate(x)] , axis = 1)
report_yield = report_yield.render() # export the table to html format to prepare for sending email
report_yield = report_yield.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A')

#report_yield.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'report_yield')



### End of Yield Report in 7 days#######


# In[11]:


#Start of NDF% Report in 7 days#############
tpu_df_first_pass_temp=df_first_pass[df_first_pass['Start Date Time']=="DUCANH"]
for date in datelist: 
    tpu_df_first_pass= df_first_pass[df_first_pass['Start Date Time'] == date].reset_index(drop = True)
    tpu_df_first_pass=tpu_df_first_pass.append(tpu_df_first_pass.sum(numeric_only=True), ignore_index=True)
    tpu_df_first_pass['NDF%']=round(tpu_df_first_pass['TOTAL_NDF']/tpu_df_first_pass['TOTAL_TEST']*100,2)
    tpu_df_first_pass[['Family','Assembly No']]=tpu_df_first_pass[['Family','Assembly No']].replace(np.nan, "TOTAL") # chuyen doi NaN thanh 0
    #tpu_df_first_pass['Start Date Time']=tpu_df_first_pass['Start Date Time'].replace(np.nan, tpu_df_first_pass["Start Date Time"].shift(1)) # chuyen doi NaN thanh 0
    tpu_df_first_pass['Start Date Time']=tpu_df_first_pass['Start Date Time'].replace(np.nan, date) # chuyen doi NaN thanh 0
    tpu_df_first_pass_temp=pd.concat([tpu_df_first_pass_temp, tpu_df_first_pass]).reset_index(drop = True)


df_summary=tpu_df_first_pass_temp
report_NDF = pd.pivot_table(df_summary , index = ['Family','Assembly No'] , values = ['NDF%'] , columns = ['Start Date Time']) # pivot the tables and stored in report
report_NDF = report_NDF.reset_index() # reset the index of report data frame
report_NDF.columns = report_NDF.columns.droplevel(0) # drop level 0 of dataframe
report_NDF.columns.name = None # remove the columns name
cols = report_NDF.columns.tolist()
cols = ['Family'] + ['Assembly No']+cols[2:]
report_NDF.columns = cols
report_NDF.columns
report_NDF['GOAL']=0.3 # call function goal to add goal for each TPU
cols=report_NDF.columns.tolist() # prepare to swap column orders
cols=cols[0:2] + cols[-1:] + cols[2:-1] # swap column orders
report_NDF=report_NDF[cols] # save back the table with new column order to report
report1_NDF=report_NDF[report_NDF['Family']!='TOTAL']
report2_NDF=report_NDF[report_NDF['Family']=='TOTAL']
report_NDF=pd.concat([report1_NDF, report2_NDF]).reset_index(drop = True)
report_NDF

report_NDF = report_NDF.style.apply(lambda x: ["background-color: #00FF00" if (col >= 3 and (v <= x.iloc[2])) else "background-color: #FF0000" if (col >=3 and (v > x.iloc[2])) else '' for col , v in enumerate(x)] , axis = 1)
report_NDF = report_NDF.render() # export the table to html format to prepare for sending email
report_NDF = report_NDF.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A')

#report_NDF.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'report_NDF')
# End of NDF% Report in 7 days                                                                                                


# In[12]:


# Start find Serial number of Total NDF
df_NDF1_serialnumber= df_NDF1_raw.groupby(['Start Date Time','Serial Number'])['Repeat'].sum().reset_index(name = 'NDF1')
df_NDF2_serialnumber=df_NDF2_raw.groupby(['Start Date Time','Serial Number'])['total_df2'].sum().reset_index(name = 'NDF2')
df_NDF1_NDF2_serialnumber=pd.concat([df_NDF1_serialnumber, df_NDF2_serialnumber]).reset_index(drop = True)# Ghep 2 table voi nhau

df_NDF1_NDF2_serialnumber= df_NDF1_NDF2_serialnumber[['Serial Number']]# chi lay cot Serial Number 
df_NDF1_NDF2_serialnumber['Failure mode']=1 #Them Cot repeat=1 cho tat ca serial number 
df_NDF1_NDF2_serialnumber


# In[13]:


rawdata_fail=rawdata[rawdata['first_fail']==1]# Lay rawdata neu first_fail=1
#rawdata_fail.to_excel( r'C:\Tai\excel_name.xlsx',sheet_name= 'your_sheet_name')
df_NDF1_NDF2_defect=pd.merge(rawdata_fail,df_NDF1_NDF2_serialnumber, on='Serial Number', how='left')# Merge 2 Table voi nhau
df_NDF1_NDF2_defect_raw=df_NDF1_NDF2_defect[df_NDF1_NDF2_defect['Failure mode']==1].reset_index(drop = True)# Loc lay nhung serial number nao Failure mode=1


# In[14]:


# Start Tinh Total cac Failure mode tracking by days
df_NDF1_NDF2_defect_sum= df_NDF1_NDF2_defect_raw.groupby(['Data Label' ,'Start Date Time'])['Process Loop'].count().reset_index(name = 'QTY')
report_NDF1_NDF2_defect = pd.pivot_table(df_NDF1_NDF2_defect_sum , index = ['Data Label'] , values = ['QTY'] , columns = ['Start Date Time']) # pivot the tables and stored in report
report_NDF1_NDF2_defect = report_NDF1_NDF2_defect.reset_index() # reset the index of report data frame
report_NDF1_NDF2_defect.columns = report_NDF1_NDF2_defect.columns.droplevel(0) # drop level 0 of dataframe
report_NDF1_NDF2_defect.columns.name = None # remove the columns name
report_defect = report_NDF1_NDF2_defect.rename(columns = {'' : 'Top defect by days'}) # rename the first columns with empty name to TPU
report_defect = report_defect.sort_values(report_defect.columns[2], ascending = False).reset_index(drop = True)# Sap xep giam dan theo column 2
report_defect
#report_defect.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'report_defect')
# End of Failure mode tracking by days


# In[15]:


# Link data voi nhau
report_defect_link= df_NDF1_NDF2_defect_raw[['Assembly No','Serial Number','Start Date Time','Data Label','Fail Message']].reset_index(drop = True)# chi lay cot Serial Number 
report_defect_link
#report_defect_link.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'report_defect_link')


# In[17]:


# Start Tinh Total Top contributor in 7 days
df_NDF1_NDF2_defect_sum_7days= df_NDF1_NDF2_defect_raw.groupby(['Data Label'])['Process Loop'].count().reset_index(name = 'QTY')
df_NDF1_NDF2_defect_sum_7days=df_NDF1_NDF2_defect_sum_7days.sort_values(by = 'QTY',ascending = False).reset_index(drop = True)
df_NDF1_NDF2_defect_sum_7days
#df_NDF1_NDF2_defect_sum_7days.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'df_NDF1_NDF2_defect_sum_7days')
# End of Tinh Total Top contributor in 7 days


# In[18]:


# Link data voi nhau
df_NDF1_NDF2_defect_sum_7days_link= df_NDF1_NDF2_defect_raw[['Assembly No','Serial Number','Data Label','Fail Message']].reset_index(drop = True)
df_NDF1_NDF2_defect_sum_7days_link
#df_NDF1_NDF2_defect_sum_7days_link.to_excel( r'C:\Tai\Daily Report.xlsx',sheet_name= 'df_NDF1_NDF2_defect_sum_7days_link')


# In[ ]:

####df_NDF1_NDF2_defect_sum_7days link với df_NDF1_NDF2_defect_sum_7days_link
df_NDF1_NDF2_defect_sum_7days['Data Label list'] = df_NDF1_NDF2_defect_sum_7days.apply(lambda x: 'OTHER' if x['QTY']<50 else x['Data Label'] , axis = 1)
df_NDF1_NDF2_defect_sum_7days_link=pd.merge(df_NDF1_NDF2_defect_sum_7days_link,df_NDF1_NDF2_defect_sum_7days, on='Data Label', how='left')# Merge 2 Table voi nhau
del df_NDF1_NDF2_defect_sum_7days_link['QTY']
del df_NDF1_NDF2_defect_sum_7days['Data Label']
df_NDF1_NDF2_defect_sum_7days=df_NDF1_NDF2_defect_sum_7days[['Data Label list','QTY']]
df_NDF1_NDF2_defect_sum_7days= df_NDF1_NDF2_defect_sum_7days.groupby(['Data Label list'])['QTY'].sum().reset_index(name = 'QTY')
df_NDF1_NDF2_defect_sum_7days1=df_NDF1_NDF2_defect_sum_7days[df_NDF1_NDF2_defect_sum_7days['Data Label list']!='OTHER']
df_NDF1_NDF2_defect_sum_7days2=df_NDF1_NDF2_defect_sum_7days[df_NDF1_NDF2_defect_sum_7days['Data Label list']=='OTHER']
df_NDF1_NDF2_defect_sum_7days=pd.concat([df_NDF1_NDF2_defect_sum_7days1, df_NDF1_NDF2_defect_sum_7days2]).reset_index(drop = True)



defect_list = df_NDF1_NDF2_defect_sum_7days_link['Data Label list'].unique() # list of TPU owner
for defect in defect_list:
    tpu_link = df_NDF1_NDF2_defect_sum_7days_link[df_NDF1_NDF2_defect_sum_7days_link['Data Label list'] == defect].reset_index(drop = True)
    tpu_link=tpu_link.sort_values(by = 'Data Label',ascending = False).reset_index(drop = True)
    content = '<!DOCTYPE html>' + '<html><body>'
    tpu_link= tpu_link.style
    tpu_link= tpu_link.render()
    tpu_link= tpu_link.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A') # add border Location in table after exporting to html format
    content = content  + tpu_link
    with open('C:\\Tai\\Data\\NDF1_NDF2\\' + str(defect) + '.html' , 'w',errors="ignore") as f:
        f.write(content)




report_df_NDF1_NDF2_defect_sum_7days = df_NDF1_NDF2_defect_sum_7days.style.format({'Data Label list' : lambda x: '<a href="C:\\Tai\\Data\\NDF1_NDF2\\{}.html">{}</a>'.format(x,x)})
report_df_NDF1_NDF2_defect_sum_7days = report_df_NDF1_NDF2_defect_sum_7days.render() # export the table to html format to prepare for sending email
report_df_NDF1_NDF2_defect_sum_7days = report_df_NDF1_NDF2_defect_sum_7days.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A')

        

###report_defect    link voi report_defect_link
import pandas as pd
defect_list = report_defect_link['Data Label'].unique() # list of TPU owner
for defect in defect_list:
    tpu_report_defect_link = report_defect_link[report_defect_link['Data Label'] == defect].reset_index(drop = True)
    content = '<!DOCTYPE html>' + '<html><body>'
    tpu_report_defect_link= tpu_report_defect_link.style
    tpu_report_defect_link= tpu_report_defect_link.render()
    tpu_report_defect_link= tpu_report_defect_link.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A') # add border Location in table after exporting to html format
    content = content  + tpu_report_defect_link
    with open('C:\\Tai\\Data\\Defect\\' + str(defect) + '.html' , 'w',errors="ignore") as f:
        f.write(content)

report_defect1 = report_defect.style.format({'Top defect by days' : lambda x: '<a href="C:\\Tai\\Data\\Defect\\{}.html">{}</a>'.format(x,x)})
report_defect1 = report_defect1.render() # export the table to html format to prepare for sending email
report_defect1 = report_defect1.replace('\n' , '').replace('<table' , '<table border="1"').replace('nan' , 'N/A')
        


###############################################

# some setups for html format in email
# some setups for html format in email
reportcontent = '<!DOCTYPE html>'
reportcontent += '<html>'
reportcontent += '<body>'
reportcontent += """<p>First pass yield (FPY) report in last 10 days</p>"""
reportcontent += report_yield
reportcontent += """<p>False fail (NDF) report in last 10 days</p>"""
reportcontent += report_NDF
reportcontent += """<p>Report_defect  in last 10 days</p>"""
reportcontent += report_defect1
reportcontent += """<p>False fail (NDF) report in last 10 days</p>"""
reportcontent += report_df_NDF1_NDF2_defect_sum_7days
reportcontent += '</html>'
reportcontent += '</body>'

#send email using your outlook account

import win32com.client as win32
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'dhoang@vn.pepperl-fuchs.com'
mail.Subject = 'First pass yield performance last 10 days'
mail.HTMLBody = reportcontent
mail.Send() # and send email



