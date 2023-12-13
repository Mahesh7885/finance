from flask import jsonify,request,Flask,render_template
import config
from API_CA.utility import CreditApproval


app=Flask(__name__)
@app.route("/")
def homeapi():
    return render_template("credit_app.html")

@app.route("/Prediction_of_Approval",methods=["POST","GET"])
def get_approval():
    if request.method == 'POST':
        user_data=request.form
        sav_acc_bal=float(user_data["Savings acc balance"])
        mon_h_exp=float(user_data["housing expense"])
        acc_ref=user_data["acc_ref"]
        lia_ref=user_data["liability ref"]
        twb=float(user_data["time with bank"])
        bnk_ac=user_data["bank acc"]
        othe_in=user_data["othe_in"]
        mtwe=float(user_data["mean time with emp"])
        curr_job=user_data["curr_job"]
        if user_data['current occupation']== "ff" or user_data['current occupation']== "j":
            curr_occ=user_data["current occupation"] + ".1"
        else:
            curr_occ=user_data["current occupation"]
        mari_st=user_data["marital status"]
        h_st=user_data["home status"]
        mtad=float(user_data["mean time at address"])
        age=int(user_data["age"])
        gender=user_data["gender"]

    else:
        sav_acc_bal=float(request.args.get("balance"))
        mon_h_exp=float(request.args.get("expense"))
        acc_ref=request.args.get("account")
        lia_ref=request.args.get("liability")
        twb=float(request.args.get("time"))
        bnk_ac=request.args.get("bank")
        othe_in=request.args.get("Othe invest")
        mtwe=float(request.args.get("mean time"))
        curr_job=request.args.get("Current job")
        if request.args.get("current occu")== "ff" or request.args.get("current occu")== "j":
            curr_occ=request.args.get("current occu") + ".1"
        else:
            curr_occ=request.args.get("current occu")
        mari_st=request.args.get("mari status")
        h_st=request.args.get("home")
        mtad=float(request.args.get("mean time"))
        age=int(request.args.get("age"))
        gender=request.args.get("gender")

        approval=CreditApproval(sav_acc_bal,mon_h_exp,acc_ref,lia_ref,twb,bnk_ac,othe_in,mtwe,curr_job,curr_occ,mari_st,h_st,mtad,age,gender)
        status=approval.get_cr_app()
        if status==1:
            result="Approved"
        else:
            result="Not Approved"
        return render_template("credit_app.html",Credit_Status=result)

if __name__=="__main__":
    app.run()