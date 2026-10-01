test3="{'Network:0':'Nw_0','MAX.MaxTPS_Data_statistics_total:M':'MaxTps_DNG','MAX.MaxTPS_Pcrf_statistics_total:M':'MaxTps_PCRF','Generic_statistics:G':'GS','Stat_Code:THREAD_ALLOCATION_FAILED':'SC_TAF','Stat_Code:DB_ERRORS':'SC_DB_ERR','Interface_statistics:I':'IS_I','Interface:DATA' : 'I_DATA','Interface:PCRF': 'I_PCRF','Req_Type:GPRS_INITIAL_REQ' : 'REQ_DNG-I','Req_Type:GPRS_UPDATE_REQ' : 'REQ_DNG-U','Req_Type:GPRS_FINAL_REQ' : 'REQ_GPRS-T','Req_Type:PCRF_INITIAL_REQ':'REQ_PCRF_I','Status:RequestsCount':'ReqCnt','Status:SuccessCount':'SucCnt'}"
list1=[]
dict1={}
for i in test3[1:-1].split(","):
    for j in i.rsplit(":",1):
        k=j.strip(" ").strip("'")
        list1.append(k)
test2={list1[i]:list1[i+1] for i in range(0,len(list1),2)}
print(type(test2))
