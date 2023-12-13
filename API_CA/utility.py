# Importing liabraries
import pickle as pk
import numpy as np
import config
import json
import sklearn

class CreditApproval():
    # Parameter setting for user input
    def __init__(self, sav_acc_bal, mon_h_exp, acc_ref,lia_ref,twb,bnk_ac,othe_in,mtwe,curr_job,curr_occ,mari_st,h_st,mtad,age,gender):
        self.sav_acc_bal=sav_acc_bal
        self.mon_h_exp=mon_h_exp
        self.acc_ref=acc_ref
        self.lia_ref=lia_ref
        self.twb=twb
        self.bnk_ac=bnk_ac
        self.othe_in=othe_in
        self.mtwe=mtwe
        self.curr_job=curr_job
        self.curr_occ=curr_occ
        self.mari_st=mari_st
        self.h_st=h_st
        self.mtad=mtad
        self.age=age
        self.gender=gender
    def loadmodel(self):
        # Loading the trained model for computation from user input
        with open (config.lg_model_path,"rb") as file:
            self.model=pk.load(file)
        # Loading JSON file to facilitate user input as per trained pickle file requirements
        with open (config.json_file_path,"r") as file:
            self.json=json.load(file)
    def get_cr_app(self):
        # Writing function for getting the prediction of approval of credit
        self.loadmodel() # Trained model is loaded in the function

        dt_array=np.zeros(len(self.json["columns"]))
        dt_array[0]=self.sav_acc_bal
        dt_array[1]=self.mon_h_exp
        acc_index=self.json["columns"].index(self.acc_ref)
        dt_array[acc_index]=1
        dt_array[5]=self.json["lia_ref"][self.lia_ref]
        dt_array[6]=self.twb
        dt_array[7]=self.json["bnk_ac"][self.bnk_ac]
        dt_array[8]=self.json["othe_in"][self.othe_in]
        dt_array[9]=self.mtwe
        job_index=self.json["columns"].index(self.curr_job)
        dt_array[job_index]=1
        curr_occ_index=self.json["columns"].index(self.curr_occ)
        dt_array[curr_occ_index]=1
        dt_array[33]=self.json["mari_st"][self.mari_st]
        h_st_index=self.json["columns"].index(self.h_st)
        dt_array[h_st_index]=1
        dt_array[37]=self.mtad
        dt_array[38]=self.age
        dt_array[39]=self.json["gender"][self.gender]

        cr_appr=self.model.predict([dt_array])

        return cr_appr



