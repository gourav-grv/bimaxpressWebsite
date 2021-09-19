from django.http import HttpResponse
from django.shortcuts import redirect, render
import os
import time
from fireo.fields import datetime_field
import pyrebase
from .models import *
from .settings import BASE_DIR
from datetime import date
import pandas as pd
from datetime import timedelta
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate(
    os.path.join(BASE_DIR, "websitebackend-a31b0-firebase-adminsdk-95534-51ba194316.json"))
firebase_admin.initialize_app(cred)
db = firestore.client()

firebaseConfig = {

 "apiKey": "AIzaSyCnA7YwYCbM73DbShucsEp6sVMRCr7Kl20",
  "authDomain": "bimaxpressgrv.firebaseapp.com",
  "databaseURL": "https://bimaxpressgrv-default-rtdb.firebaseio.com",
  "projectId": "bimaxpressgrv",
  "storageBucket": "bimaxpressgrv.appspot.com",
  "messagingSenderId": "725727864773",
  "appId": "1:725727864773:web:10111916009851ceebcdac",
  "measurementId": "G-BT8ZJ4PPQJ"
}
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()

def home(request):
    context={}
    datablog={}
    doc_ref = db.collection(u'blogs').document(u'Website_Blogs')
    doc = doc_ref.get()
    if doc.exists:
        datablog = doc.to_dict()
    else:
        print(u'No such document!')
    
    print(datablog) 
    context["datablog"] = datablog
    return render(request , 'home.html', context)

def pricing(request):
    context = {}
    data = subscription_plan.collection.fetch()
    plan_details = {}
    for obj in data:
        plan_details[obj.id] = obj.price
    print(plan_details)

    context['plan'] = plan_details
    return render(request, 'pricing.html',context)

def blogredirect(request):
    context = {}
    blognumber = request.GET.get('data')
    print(request.GET.get('data'))
    if request.GET.get('data') == "":
        blognumber = "firstblog"
    
    doc_ref = db.collection(u'blogs').document(u'Website_Blogs')
    doc = doc_ref.get()
    if doc.exists:
        datablog = doc.to_dict()[blognumber]
    else:
        print(u'No such document!')
    
    print(datablog)
    
    context['blogdata'] = datablog
    
    return render(request, 'blogcontent.html',context)


def planDetails(request):
    return render(request, 'planDetails.html')

def covid(request):
    return render(request, 'covid.html')

def claimReimbursement(request):
    return render(request, 'claimReimbursement.html')

def cashlessClaim(request):
    return render(request, 'cashlessClaim.html')

def afterPricehospitalDetail(request):
    context={}
    data = subscription_plan.collection.fetch()
    plan_details = {}
    for obj in data:
        plan_details[obj.id] = obj.price
    print(plan_details)
    context['plan'] = plan_details
    return render(request, 'afterPricehospitalDetail.html',context)




def enc(request):
    return HttpResponse("EXECUTED")


def savehospitaldetails(request):
    today = date.today()
    todaydate = today.strftime("%d-%m-%Y")
    enddate="default"
    data = subscription_plan.collection.fetch()
    plan_details = {}
    for obj in data:
        plan_details[obj.id] = obj.price
        print(plan_details)
        
    context={}
    try:
        
        if request.method == "POST":
            data = request.POST.dict()
            print(data)
            print(data['plan'])    
            email = data['hospital_email']
            password = data['hospital_password']
            try:
                user = authe.create_user_with_email_and_password(email, password)
                request.session['hospital_email'] = user['email']
                db.collection(u'backend_users').document(user['email']).set({
                'email': user['email'],
                'Role' : "admin",
                })
                doc_ref = db.collection(u'subscription_plan').document(data['plan'])
                doc = doc_ref.get()
                try:
                    if doc.exists:
                        a = doc.to_dict()
                        print("Yes")
                        date1 = time.strptime(a['endDate'], "%d/%m/%Y")
                        date2 = time.strptime(a['startDate'], "%d/%m/%Y") 
                        print(date1,date2)
                        if(date1 >= date2):
                            print("Valid Plan")
                        else:
                            context['plan'] = plan_details
                            context['message'] = "Sorry Expired ☹️" 
                            return render(request, 'afterPricehospitalDetail.html',context)
                        
                        duration = a['duration']
                        enddate = pd.to_datetime(todaydate)+pd.DateOffset(days=duration)
                        enddate = pd.to_datetime(enddate).date()
                             
                except Exception as e:
                    context['plan'] = plan_details
                    context['message'] = "Sorry Expired ☹️" ,e
                    return render(request, 'afterPricehospitalDetail.html',context)
                
                db.collection(u'hospitals').document(user['email']).set({
                    "name" : data.get('hospital_name',""),
                    "email" : data.get("hospital_email",""),
                    "phone" : data.get("phone",""),
                    "rohini" : data.get("rohini_id",""),
                    "state" : data.get("state",""),
                    "city" : data.get("city",""),
                    "pinCode":data.get("pinCode",""),
                    "address":data.get("address",""),
                    "plan":data.get("plan",""),
                    "discount_code":data.get("discountCode",""),
                    "planstartdate":today.strftime("%d/%m/%Y"),
                    "planenddate":enddate.strftime("%d/%m/%Y"),
                    "gst":data.get("GST",""),
                    "pan":data.get("PAN",""),
                    "regno":data.get("regno","")
                })
                
                db.collection(u'counter').document(user['email']).set({
                    "Approved":0,
                    "Discharge_Approved":0,
                    "Enhance":0,
                    "Reject":0,
                    "Settled":0,
                    "Unprocessed":0,
                    "draft":0,
                    "query":0,
                })
                
                return redirect('userDetails')
            
            except Exception as e: 
                data = subscription_plan.collection.fetch()
                plan_details = {}
                for obj in data:
                    plan_details[obj.id] = obj.price
                print(plan_details)

                context['plan'] = plan_details
                context['message'] = "Email Already Exist or Something Went Wrong ☹️"
                return render(request, 'afterPricehospitalDetail.html',context)
        else:
            data = subscription_plan.collection.fetch()
            plan_details = {}
            for obj in data:
                plan_details[obj.id] = obj.price
            print(plan_details)
            context['plan'] = plan_details
            context['message'] = "Email Already Exist or Something Went Wrong ☹️"
            return render(request, 'afterPricehospitalDetail.html',context)
        
    except Exception as e:
        data = subscription_plan.collection.fetch()
        plan_details = {}
        for obj in data:
            plan_details[obj.id] = obj.price
        print(plan_details)
        context['plan'] = plan_details
        context['message'] = "Email Already Exist or Something Went Wrong"
        return render(request, 'afterPricehospitalDetail.html', context)
        
def userDetails(request):
    context={}
    mylist = []
    mylistone = []
    docs = db.collection(u'backend_users').where(u'hospital', u'==', request.session['hospital_email']).stream()

    for doc in docs:
        mylist.append(doc.to_dict())
        context ['claimAnalyst'] = mylist
        
    print("list of analyst",mylist)


    docs = db.collection(u'backend_users').where(u'hospitals', "array_contains", request.session['hospital_email']).stream()
    for doc in docs:
        mylistone.append(doc.to_dict())
        context ['doctor'] = mylistone

    try:
        if request.session['hospital_email'] != None:
            if request.method == "POST":
                data = request.POST.dict()
                print(data)
            
            return render(request, 'userDetails.html',context)
        else:
            return redirect('afterPricehospitalDetail')
    except:
        return redirect('afterPricehospitalDetail')

def privacy_policy(request):
    
    return render(request, 'privacy-policy.html')
    
def saveusercreation(request):
    context={}
    mylist = []

    mylistone = []
    docs = db.collection(u'backend_users').where(u'hospitals', "array_contains", request.session['hospital_email']).stream()
    for doc in docs:
        mylistone.append(doc.to_dict())
        context ['doctor'] = mylistone

    docs = db.collection(u'backend_users').where(u'hospital', u'==', request.session['hospital_email']).stream()

    for doc in docs:
        mylist.append(doc.to_dict())
        context ['claimAnalyst'] = mylist
    print("list of analyst",mylist)
    try:
        if request.session['hospital_email'] != None:
            if request.method == "POST":
                data = request.POST.dict()
            print(data)
            email = data.get('email',"")
            password = data.get('pass',"")
            try:
                print("going")
                user = authe.create_user_with_email_and_password(email, password)
                print("insertion taking place")
                db.collection(u'backend_users').document(user['email']).set({
                'email': user['email'],
                'name': data.get('name',""),
                'Role' : "claim_analyst",
                'hospital' : request.session['hospital_email'],
                'phone':data.get('phone',""),
                'employeeId':data.get("empid","")
                })
            except Exception as e: 
                print(e)

                context['message'] = "Email Already Exist",
                return render(request, 'userDetails.html',context)
            return redirect('userDetails')
        else:
            return redirect('afterPricehospitalDetail')
    except:
        return redirect('afterPricehospitalDetail')
            

def savedoctorcreation(request):
    try:
        if request.session['hospital_email'] != None:
            if request.method == "POST":
                data = request.POST.dict()
            print(data)
            email = data.get('doctor_email',"")
            password = data.get('doctor_passwd',"")
            try:
                print("going")
                user = authe.create_user_with_email_and_password(email, password)
                print("insertion taking place")
                
                db.collection(u'backend_users').document(user['email']).set({
                    'email': user['email'],
                    'Role' : "doctor",
                    'name' : data.get('doctor_name',""),
                    'phone' : data.get('doctor_phone',""),
                    'qualification' : data.get('doctor_qualification',""),
                    'speciality' : data.get('doctor_specialization',""),
                    'doctorRegistrationNo' : data.get('doctor_registration',""),
                    'hospitals': firestore.ArrayUnion([request.session['hospital_email']])
                })
                
            except :
                db.collection(u'backend_users').document(f'{email}').update({"hospitals": firestore.ArrayUnion([request.session['hospital_email']])})
                return render(request, 'userDetails.html')
            
            return redirect('userDetails')
        else:
            return redirect('afterPricehospitalDetail')
    except:
        print("nihe wal")
        db.collection(u'backend_users').document(email).update({"hospitals": firestore.ArrayUnion([request.session['hospital_email']])})
        return redirect('afterPricehospitalDetail')
        
def empanelled_companies(request):
    return render(request, 'empanelled_companies.html')
    

def logout(request):
    request.session.flush()
    return redirect("afterPricehospitalDetail")

def valuegot(request):
    context={}
    images={}
    temp = []
    if request.method == "POST":
        data = request.POST.dict()
        print(data)
        temp = data['company_list'].split(',')
        print(temp)
        for i in temp:
            doc_ref = db.collection(u'InsuranceCompany_or_TPA').document(f"{i}")
            doc = doc_ref.get()
            if doc.exists:
                img_value = doc.to_dict()
                images[doc.id]=(img_value['image'])
            else:
                print(u'No such document!')
            
    context['images'] = images
    context['email'] = request.session['hospital_email']
    print(images)
    return render(request, 'discount_exclustion.html',context)

def email(request):
    return render(request, 'email.html')


def emailLogin(request):
    if request.method == 'POST':
        domainName = request.POST.get('imap')
        smtp = request.POST.get('smtp')
        hospitalEmail = request.POST.get('hospital_mail')
        hospitalPassword = request.POST.get('hospital_password')
        ref = db.collection(u'hospitals').document(request.session['hospital_email'])
        print("hospital",request.session['hospital_email'])
        try:
            data = {
                "Emailer": {
                    "imap": domainName,
                    "smtp": smtp,
                    "email": hospitalEmail,
                    "password": hospitalPassword
                }
            }
        except:
            return render(request, 'emailLogin.html')
        ref.set(data,merge=True)
        os.environ['EMAIL_USER'] = hospitalEmail
        os.environ['EMAIL_PASSWORD'] = hospitalPassword
        os.environ['EMAIL_HOST'] = domainName
        return redirect('https://claimdesk.bimaxpress.com')
    else:
        return render(request, 'emailLogin.html')
    
def contact(request):
    data = [{'blog7': {'content': "All Health Insurance schemes can be divided broadly between Government and Private players. There are various government schemes, viz: Ayushman Bharat (erstwhile RSBY), CGHS, State Health Insurance Schemes, ESIC. Apart from the government-sponsored plans, there are 31 Insurance companies in India providing Health Insurance products. Another vital entity in the ecosystem is TPAs. They act on behalf of Insurance companies to offer cashless claims services through their network to Insurance Companies' customers.  Notable facts: • Ayushman Bharat is the world’s largest free health insurance scheme. • The private insurers processed a total of 34.25 million claims in FY 2018-19.", 'date ': '16 January 2021', 'img': 'https://image.slidesharecdn.com/healthinsurancepolicy-160411111657/95/types-of-health-insurance-in-india-3-638.jpg?cb=1460713682', 'title': 'Type of Health Insurance and who are the players in the industry?'}, 'blog8': {'title': 'If I have an Insurance cover through my employer, do I need Health Insurance separately?', 'img': 'https://qph.fs.quoracdn.net/main-qimg-f946d0ce7c434b818924c7004cd1ed8a', 'content': 'Health Insurance cover as provided by the insurer may not be sufficient to cover the needs of hospitalization. This is because every company is trying to reduce its expenses in the current scenario. And the cost of insurance for employees is one of such fees. This budget-cutting will result in you having limits in terms of co-pay options, type of rooms covered, several family members covered, etc. You may end up paying an additional premium for your parents, who may not even be covered if they have a pre-existing condition. Also, if you plan to leave the organization, you may lose your cover too. This is especially true for people taking a retirement. All these and many more make it perfect sense to buy an additional Health Insurance plan for you and your family.', 'date': '10 February 2020'}, 'firstblog': {'img': 'data:image/jpeg;base64,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', 'title': 'NODE MCU', 'content': 'new content', 'date': '1st January, 2021'}, 'blog10': {'title': 'In what conditions Can an Insurance Company reject a Health Insurance Claim?', 'date': '10 August 2020', 'content': 'Medical claims can be rejected for a variety "\\n" of reasons. However, you can avoid these rejections by initially disclosing your medical history, including smoking and other risk-attracting habits. If done right, there shouldn\'t be an issue with a claim. Here are some other reasons that could lead to health claim rejections:  1. Policy Renewal: You cannot claim on an expired policy, so make sure your premiums are paid on time. Furthermore, you can also lose out on your no claim bonus by delaying premium payments. 2. Pre-existing Illnesses: Plans usually don\'t cover pre-existing diseases right after purchase. Though, IRDAI has a standardized definition to eliminate the chances of this happening. Usually, pre-existing conditions are covered after a certain waiting period. 3. Permanent Exclusions: Several diseases, treatments, and expenses are permanently not covered under all health policies, and knowing this could help you appropriately filing a claim. 4. Limits on Treatments: Health insurance policies usually have a defined amount that can be spent on treatment costs and room rent. Any amount more than the amount mutually agreed on will not be paid. 5. Incorrectly Filled Claim Form: Make sure to fill your claim form without mistakes, as it is a factor on which rejections take place.', 'img': 'https://www.mymoneysage.in/blog/wp-content/uploads/2017/05/health-insu-claim.png'}, 'blog2': {'content': "Who doesn't like a good discount deal? However, while purchasing health insurance, you should consider not just the cost of it but the following points as well: #1 - Claim Settlement Ratio of the Insurance Company : The claim settlement ratio is the ratio of the number of claims approved to the number of claims received. This ratio/percentage should be upward of 85% for an insurance company. A claim settlement ratio of 85% means that for every 100 claims received by the company, it approves 85 of them.  #2 – Pre-Existing Conditions & Cool Off Period: Suppose you or your family member who will be covered in the insurance plan is already suffering from a disease. Such diseases are called pre-existing conditions. Cool Off period is the time taken by your insurance to kick in. This cool off period can range anywhere between 30 to 180 days. During this period, if you raise a claim against pre-existing conditions, your claim will be denied. Therefore, it is always recommended to go for a policy that has the lowest cool off period.  #3 - The Hospital Network: Each Health Insurance company has a network of hospitals empaneled with them or with their TPA. You should check whether your preferred hospital in your residence/work area is empaneled as a network hospital with the insurance company. Doing this will enable you to get cashless treatment at the preferred hospital.  #4 – Type of Room Covered: This is an important parameter when you are considering a Health Insurance plan. Generally, all the other parameters associated with Health Care expenses are linked to room type. You will get higher coverage of all other features if your policy provides higher category room type coverage. You should also check for the limits available for ICU, which will be required in emergencies. #5 – Medical Conditions Covered: Each policy has a list of Medical Conditions which are not covered under it. For example, maternity is not covered in many plans, so if you are looking to start a family, you should look for maternity coverage plans.", 'img': 'https://images.livemint.com/rf/Image-621x414/LiveMint/Period2/2018/05/19/Photos/Processed/health-kCnE--621x414@LiveMint.jpg', 'title': '5 Points to Consider While buying a Health Insurance Plan!', 'date': '20 october,2021'}, 'blog3': {'img': 'https://s3.ap-south-1.amazonaws.com/healthinsurances3.com/prod/imagegallery/How-Can-I-File-Claim-for-Two-Health-Insurance-Policies.jpg', 'date': '20 October 2021', 'title': 'How can one claim for their treatment?', 'content': "A person can claim for their treatment in two ways, they are: 1. Cashless Claims 2. Claim Reimbursements.  Cashless Claim: A cashless claim means you (as a policyholder) do not have to pay the hospital bill (apart from a nominal amount). This is because your insurance company will settle it with the hospital as part of the claim settlement if it is a network hospital. Within Cashless Process, there are also two types, i.e., Planned and Emergency. In case of planned admission, you have to take upfront approval from the insurance company for cashless treatment. In Emergency cases, you need to inform the Insurance company within 24 to 48 hours of hospitalization. To avail of the cashless process's benefits, you have to provide the insurance company the complete information about your treatment. This information includes the hospital you are going for treatment, the kind and mode of treatment, any existing chronic illness, the estimated cost going to be pay, etc. The Insurance company will review the details and will provide the approval to the hospital. Subsequently, only the hospital will initiate your cashless claims process.  Reimbursement Claim: The Reimbursement Claim for health insurance can be made if the policyholder opts to go to a hospital of his/ her choice, a non-network hospital. Here, you directly go to the hospital and pay for all the expenses; subsequently, the costs are reimbursed from the Insurance Company/TPA. In this case, the cashless claim facility cannot be used as the hospital is a non-network hospital. Therefore, the insured has to pay all his/ her medical bills and other costs involved in hospitalization and treatment and then claim reimbursement. To avail reimbursement, you have to provide the necessary documents, including original documents (Bills, Reports, Discharge Summary), etc., to the insurance provider. The company will then evaluate the claim and assess against the coverages under the policy. It will then accordingly makes a payment to the insured. At BimaXpress, we are committed to improving your Claims Experience whether you are opting for a Claims Reimbursement or Cashless Claims. If you are looking to file for a Claim Reimbursement, please download our app called 'BimaXpress' from Apple or Google App Stores."}, 'blog11': {'title': 'What is the type of expenses covered under Health Insurance for Claims?', 'content': "An Insurance Policy covers you against a wide range of medical expenses, which can vary between policies. Here are some of the most common inclusions of an Insurance Policy:  1. Hospitalization Costs: It includes all medical expenses incurred during the policyholder's hospitalization or the policy's beneficiaries. It covers costs related to diagnostic procedures, OT charges, medicines, blood, x-ray, oxygen, etc. 2. Pre and Post-Hospitalisation Expenses: Medical expenses arising before 30 days of hospitalization and up to 60 days post-discharge are covered under the Insurance Policy. However, you need to check with the insurer if this type of hospitalization is part of the policy. 3. Day-Care Expenses: Medical expenses arising out of advanced medical treatments that do not require the patient to be hospitalized for more than 24 hours are covered. 4. Hospital Room Expenses: Costs towards regular wards or Intensive Care Unit (ICU) are fully reimbursed or through the cashless facility. 5. Doctor’s or Medical Professionals’ Fee: Doctor's consultation fee or medical professionals' charges such as nurses' fee, etc., are covered. Every Insurance Policy has some exclusions and varies from one insurance company to another. Here are some of the standard exclusions in Insurance Policies:  1. Pre-existing illnesses. 2. Dental treatments. 3. Sexually transmitted diseases. 4. Birth control and hormonal therapies. 5. Vaccinations. 6. Plastic surgery. 7. Cosmetic surgery and obesity-related treatments. 8. Maternity expenses if not opted as an Add-on feature. 9. Non-medical expenses such as service charges, administrative charges, toiletries, etc. 10. Ailments and diseases contracted within a set period from the policy purchase date.", 'img': 'https://www.iciciprulife.com/content/dam/icicipru/all/Health-Insurance-cost-of-medical-treatment.jpg', 'date': '15 August 2020'}, 'blog6': {'img': 'https://www.bankbazaar.com/images/india/infographic/Complaint-Against-Health-Insurance-Companies.png', 'date': '15 August 2021', 'title': 'How to get my grievances addressed for Health Insurance Claims?', 'content': "In case you are not satisfied with the Health Insurance company's reason to reject the claim, follow the following process: Give a written complaint at the Insurance Companies branch and get a written acknowledgment. IRDA has stipulated a TAT of 15 days for resolving the complaints against any claim. In case you are not getting a satisfactory response, you can reach out to the Consumer redressal department of IRDA. You can also file a grievance with the Insurance Ombudsman. In case your complaints are still not resolved, you can file a complaint with the Consumer Court. Consumer courts have a different department to handle health insurance claims related grievances. Contact Details for Grievance Redressal Cell of the Consumer Affairs Department of IRDA Toll Free Number: 1800 4254 732/ 155255 Email ID: complaints@irda.gov.in Postal Address: Consumer Affairs Department Insurance Regulatory and Development Authority, 3-5-817/818, 9th Floor, United India Towers, Hyderguda, Basheerbagh Hyderabad – 500 029 Fax: 040-66789768 To get the details of the Ombudsman for your area, please visit https://www.policyholder.gov.in/Addresses_of_Ombudsmen.aspx"}, 'blog5': {'date': '5 August 2020', 'title': 'Process for Claim Reimbursement?', 'img': 'https://general.futuregenerali.in/img/claims/travel-2.png', 'content': 'Step 1. Intimate the TPA/Insurance Company on their Toll-Free number regarding the admission and get the claim number. Step 2. As when you pay the money, keep a copy of the receipts safely. Step 3. At the time of discharge from the hospital, be sure to collect the following: i. Detailed bill for payment made. ii. Final Payment Receipt iii. Discharge Summary: Check the Discharge Summary before leaving. Sometimes, by error, there may be a mention of a pre-existing condition which the patient never suffered. For example, there may be a sentence stating diabetes past ten years when the patient had never suffered from the same. iv. Copy of Investigation Reports- Blood test, Urine test, motion test, X-ray, MRI, CT-Scan, report where the specimen is sent for tests, and any other test reports. Make sure to collect all the test reports mentioned in the discharge summary. v. In case of accidents, collect a Medico-Legal Certificate. vi. In case any implants have been done, ask for the invoice copy of the implant. The invoice may include a plate for fracture, a stent for angioplasty, lenses for cataract surgery, etc. vii. Collect a copy of the Indoor case papers. Still, the same need not be submitted to the TPA/Insurance Company unless specifically asked. Step 4. You need to fill the complete claim form and share it with the Insurance company and all the papers, bills, Discharge Summary, and Reports and submit the same. Step 5. The acceptable amount may be credited to you, or the TPA/Insurance Company may raise a few queries. In case of questions, go to the hospital and get the details from the treating Doctor.  In case you are looking to get your claim reimbursed, please download the BimaXpress App from Google /Apple Appstore and initiate a Claim Reimbursement request.'}, 'blog4': {'content': "Step 1: Give the Health Card to Insurance Department in the Hospital. Step 2: Give an intimation to the Insurance Company on their Toll-free number, get the claim number, and give it to the hospital's insurance department. Step 3: Pre-authorization request to be sent to the Insurance Company/TPA by Hospital. Step 4: Follow up with the hospital to find out whether they received the authorization. Initially, an authorization will be granted only for a partial amount. This acts as evidence that the claim is accepted. When a discharge is advised, follow-up with the hospital to send Discharge Summary, Final Bill, all investigation reports to the Insurance Company/TPA. Only after receiving all the documents will the final approval be given. Then you will be able to receive the final authorization amount in a couple of hours. In case there is a difference between the actual and authorized amount, the difference can be reimbursed if payable. If you are a hospital looking to streamline your Claims Management process, write to us at sales@bimaxpress.com and reach out to you.", 'date': '20 November 2021', 'title': 'What is the process for Cashless Claims?', 'img': 'data:image/png;base64,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'}, 'blog9': {'img': 'data:image/png;base64,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', 'title': 'What should hospitals take care of while filing for Health Insurance Plan?', 'content': "Every Insurance Company/TPA has its procedure for processing claims. When it comes to filing a Health Insurance Claim, Hospitals must follow all the guidelines and disclose all the necessary details and documents to the Insurance Companies/TPA. The Documents required are:  1. The Primary/Insured Details (Health ID card, KYC documents), etc. 2. The Diagnosis Reports. 3. Patient's Medical History. 4. Doctor's Prescriptions. 5. OT Notes. 6. Tests/Investigations. 7. Duty Doctor's/Visiting Doctor's Notes. 8. Estimated Expenses. Once the hospital has filed the claim, it then coordinates with the Insurance Company/TPA to get the claim processed. Suppose any additional details are required, or the Insurance Company/TPA raises a query. In that case, the hospital will resolve them within the timeframe and revert to the company. Get a call back from our sales team to understand the product.", 'date': '19 October 2021'}, 'blog1': {'img': 'https://geospatialmedia.s3.amazonaws.com/wp-content/uploads/2019/07/UAVs-help2.jpg', 'content': 'With the continuously increasing costs of health care in our country and with the ever-rising instances of diseases, insurance these days is a necessity. Insurance provides individuals with the required money backup from time to time of medical emergencies. Health risks and uncertainties don’t come knocking on your door. A person may not be ready emotionally or physically for such difficulties, but they can undoubtedly prepare themselves financially. One of the best ways to do this is by buying a health insurance plan.  Health insurance pays for medical expenses incurred by the insured. Health Insurance can get cashless medical treatment in a network hospital. The insured can get the costs reimbursed through the insurance company if the treatment is through a non-network hospital. However, it would help if you were careful while buying an insurance plan. For a better understanding of the steps to be taken before purchasing health insurance, read our blog, 5 points to consider while buying a Health Insurance Plan!', 'title': 'Why should you buy Health Insurance?', 'date': '21st October,2020'}}]
    
    for i in data:
        db.collection(u'blogs').document(u'Website_Blogs').set(i)

    return render(request, 'contact.html')

def emailGoogle(request):
    context={}
    context['my_host'] = "gmail.com"

    return render(request, 'emailLogin.html',context)

def emailYahoo(request):
    context={}
    context['my_host'] = "yahoo.com"
    return render(request, 'emailLogin.html',context)

def emailAws(request):
    context={}
    context['my_host'] = "awsapps.com"
    return render(request, 'emailLogin.html',context)