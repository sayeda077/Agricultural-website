from django.shortcuts import render
from .models import Myhome,Ideainfo,Branch,Loan,ConfirmLoan




def homepage(request):
    item = Myhome.objects.all()

    title = 'Welcome to the Agricultural website'
    desc ='The proposed system is designed to eliminate some problems of farmers and fisherman usually they face. By using this system, the farmers of Bangladesh who typically don’t get the proper price can get it. Sometimes they need the loan which they get from the chairman of the village with high interest. By this, most of the time, they lose their homestead also. For these reasons, we will design a system from which they can quickly get the loan with very low interest'

    context = {'title':title,
               'description':desc,
                'data':item
                }

    return render(request,'index.html', context)

def farmer(request):
    title='Welcome to Farmer page of agricultural site'
    desc= """Farmers are really very important for the agricultural system of a country"""

    context = {
           'title':title,
           'desc': desc,
    }
    return render(request,'farmer.html',context)

def fisherman(request):
    return render(request,'fisherman.html')

def specialist(request):
    return render(request,'specialist.html')

def adminpage(request):
    return render(request,'adminpage.html')

def checkuser(request):
    
    return render(request,'checkuser.html')


def branchinfo(request):

    if request.method == 'POST':

        branch_name = request.POST.get('branch_name')
        branch_address = request.POST.get('branch_address')
        branch_PhoneNumber1 = request.POST.get('branch_PhoneNumber1')
        branch_PhoneNumber2 = request.POST.get('branch_PhoneNumber2')
        branch_specialist_for_farmer = request.POST.get('branch_specialist_for_farmer')
        branch_specialist_for_fisherman = request.POST.get('branch_specialist_for_fisherman')
        branch_seed_amount = request.POST.get('branch_seed_amount')
        branch_fish_amount = request.POST.get('branch_fish_amount')
        branch_training_time = request.POST.get('branch_training_time')

        data = Branch(bname = branch_name,baddress = branch_address,bphn1 = branch_PhoneNumber1,bphn2 = branch_PhoneNumber2, bspecialist1 = branch_specialist_for_farmer,bspecialist2 =  branch_specialist_for_fisherman, bseed = branch_seed_amount,bfish = branch_fish_amount,btrainingtime = branch_training_time)
        data.save()

    return render(request,'branchinfo.html')

def idea(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('comments')
    
        mydata = Ideainfo(iname = name,iemail = email,iquery = query)
        mydata.save()

    return render(request,'idea.html')

def takeloan(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phoneNumber')
        branch = request.POST.get('branch')
        amount = request.POST.get('amount')

         

        loandata = Loan(name = name, email = email, phn = phone, branch = branch,amount = amount)
        loandata.save()

    return render(request,'takeloan.html')

def confirmloan(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        amount = request.POST.get('amount')

         

        cloan = ConfirmLoan(name = name, email = email,amount = amount)
        cloan.save()
    return render(request,'confirmloan.html')


 