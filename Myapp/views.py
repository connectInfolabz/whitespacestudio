from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse

# Create your views here.
def indexpage(request):
    catdata = CATEGORY.objects.all()
    productdata = PRODUCT.objects.all()
    feaddata = feedback.objects.all()
    context = {
        "cat": catdata,
        "prodata": productdata,
        "fiddata": feaddata
    }
    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        productdata = PRODUCT.objects.all()
        feaddata = feedback.objects.all()
        context = {
            "pdata": checkdp,
            "cat": catdata,
            "prodata": productdata,
            "fiddata": feaddata
        }
        return render(request, 'index.html',context)
    except:
        pass
    return render(request,'index.html',context)


def profile(request):
    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        context = {
            "pdata": checkdp,
            "cat" :catdata
        }
        return render(request, 'profile.html', context)
    except:
        pass

    catdata = CATEGORY.objects.all()
    return render(request, "profile.html", {"cat" : catdata})


def signupapge(request):
    return render(request,'signup.html')




def registerdata(request):
    username = request.POST.get("cname")
    useremail = request.POST.get("cemail")
    userphone = request.POST.get("cphone")
    userpass = request.POST.get("cpsw")
    userdp = request.FILES["cdp"]

    try:
        checkemail = LOGIN.objects.get(NAME=username,EMAIL=useremail)
    except:
        checkemail = None
    if checkemail is None:
        storedata = LOGIN(NAME=username,EMAIL=useremail,PHONE=userphone,PASSWORD=userpass,dp=userdp)
        storedata.save()
        messages.success(request,"Registed Successfully!")
    else:
        messages.error(request,"already registed")


    return render(request,"signup.html")

def logindata(request):
    useremail = request.POST.get("uemail")
    userpass = request.POST.get("upassword")
    try:
        checkdata = LOGIN.objects.get(EMAIL=useremail, PASSWORD=userpass)
        request.session["logid"] = checkdata.id
        request.session["logname"] = checkdata.NAME
        request.session.save()
    except:
        checkdata = None
    if checkdata is not None:
        return redirect('/')
    else:
        # messages.error(request,"invalid pass or email")
        try:
            checkdata = LOGIN.objects.get(PHONE=useremail, PASSWORD=userpass)
            request.session["logid"] = checkdata.id
            request.session["logname"] = checkdata.NAME
            request.session.save()
        except:
            checkdata = None
        if checkdata is not None:
            return redirect('/')
        else:
            messages.error(request, "invalid pass or email")
    return redirect('/login')

def logout(request):
    try:
        del request.session["logid"]
        del request.session["logname"]
    except:
        pass
    return redirect('/')

def contactuspage(request):
    catdata = CATEGORY.objects.all()
    context = {
        "cat": catdata
    }
    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        context = {
            "pdata": checkdp,
            "cat": catdata
        }
        return render(request, 'contact.html',context)
    except:
        pass
    return render(request,'contact.html',context)

def aboutuspage(request):
    catdata = CATEGORY.objects.all()
    context = {
        "cat": catdata
    }
    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        context = {
            "pdata": checkdp,
            "cat": catdata,
        }
        return render(request, 'about.html',context)
    except:
        pass
    return render(request,'about.html',context)

def contactdata(request):
    uname = request.POST.get("username")
    uemail = request.POST.get("email")
    uphone = request.POST.get("phone")
    umsg = request.POST.get("message")

    storedata = CONTACT(NAME=uname,EMAIL=uemail,PHONE=uphone,MESSAGE=umsg)
    storedata.save()

    return redirect('/')

def servicespage(request):
    catdata = CATEGORY.objects.all()
    catprodata = PRODUCT.objects.all()
    paginator = Paginator(catprodata, 6)  # Show 6 products per page

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)

    context = {
        "cat": catdata,
        "cdata": products
    }
    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        context["pdata"] = checkdp
        return render(request, 'shop.html', context)
    except:
        pass
    return render(request, 'shop.html', context)

def addproductpage(request):
    catdta = CATEGORY.objects.all()
    context = {
        "catd": catdta
    }
    return render(request,'addproduct.html',context)

def addproductdata(request):
    cat = request.POST.get("pcat")
    name = request.POST.get("pname")
    type = request.POST.get("materialtype")
    color = request.POST.get("pcolor")
    price = request.POST.get("pprice")
    decs = request.POST.get("pdesc")
    quantity = request.POST.get("pquantity")
    img = request.FILES["pimage"]

    storedata = PRODUCT(CATID=CATEGORY(id=cat),NAME=name,MATERIAL_TYPE=type,COLOR=color,PRICE=price,DESCRIPTION=decs,QUANTITY=quantity,IMAGE=img)
    storedata.save()

    return redirect('/')


def productDetails(request):
    pid = request.POST.get("pid")
    catdata = CATEGORY.objects.all()
    singledata = PRODUCT.objects.get(id=pid)
    proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=pid)
    productdata = PRODUCT.objects.all()
    context = {
        "cat": catdata,
        "pidata": proimgdata,
        "sdata": singledata,
        "prodata": productdata
    }
    try:
        if request.method == "POST":
            pid = request.POST.get("pid")
            uid = request.session["logid"]
            checkdp = LOGIN.objects.get(id=uid)
            catdata = CATEGORY.objects.all()
            singledata = PRODUCT.objects.get(id=pid)
            proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=pid)
            productdata = PRODUCT.objects.all()
            context = {
                "pdata": checkdp,
                "cat": catdata,
                "pidata": proimgdata,
                "sdata": singledata,
                "prodata": productdata
            }
            return render(request, 'productDetails.html',context)
    except:
        pass
    return render(request,'productDetails.html',context)



# shop details reference
# def shopdetailsingle(request , id):
#     catdata = CATEGORY.objects.all()
#     singledata = PRODUCT.objects.get(id=id)
#     proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=id)
#     productdata = PRODUCT.objects.all()
#     context = {
#         "sdata": singledata,
#         "pidata": proimgdata,
#         "cat": catdata,
#         "prodata": productdata
#     }
#     try:
#         uid = request.session["logid"]
#         checkdp = LOGIN.objects.get(id=uid)
#         catdata = CATEGORY.objects.all()
#         singledata = PRODUCT.objects.get(id=id)
#         proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=id)
#         productdata = PRODUCT.objects.all()
#         context = {
#             "pdata": checkdp,
#             "cat": catdata,
#             "pidata": proimgdata,
#             "sdata": singledata,
#             "prodata": productdata
#         }
#         return render(request, 'shop-details.html',context)
#     except:
#         pass
#     return render(request,'shop-details.html',context)


def products(request):
    catdata = CATEGORY.objects.all()
    productdata = PRODUCT.objects.all()

    paginator = Paginator(productdata, 3)

    page = request.GET.get('page')
    try:
        prodata = paginator.page(page)
    except PageNotAnInteger:
        prodata = paginator.page(1)
    except EmptyPage:
        prodata = paginator.page(paginator.num_pages)

    feaddata = feedback.objects.all()

    context = {
        "cat": catdata,
        "prodata": prodata,
        "fiddata": feaddata
    }

    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        context["pdata"] = checkdp
    except:
        pass

    return render(request, 'products.html', context)


def catergory(request):
    id = request.POST.get("cateid")

    catdata = CATEGORY.objects.all()
    catprodata = PRODUCT.objects.filter(CATID=id)

    proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=id)
    context = {
        "cdata": catprodata,
        "pidata": proimgdata,
        "cat": catdata
    }

    try:
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        context["pdata"] = checkdp
    except Exception as e:
        pass

    return render(request, 'category.html', context)



#
#
# def shoppage(request, id):
#     catdata = CATEGORY.objects.all()
#     catprodata = PRODUCT.objects.filter(CATID=id)
#     paginator = Paginator(catprodata, 2)  # Display 2 products per page
#
#     page = request.GET.get('page')
#     try:
#         catprodata = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         catprodata = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         catprodata = paginator.page(paginator.num_pages)
#
#     proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=id)
#     context = {
#         "cdata": catprodata,
#         "pidata": proimgdata,
#         "cat": catdata
#     }
#
#     try:
#         uid = request.session["logid"]
#         checkdp = LOGIN.objects.get(id=uid)
#         catdata = CATEGORY.objects.all()
#         catprodata = PRODUCT.objects.filter(CATID=id)
#         paginator = Paginator(catprodata, 4)  # Display 2 products per page
#
#         page = request.GET.get('page')
#         try:
#             catprodata = paginator.page(page)
#         except PageNotAnInteger:
#             # If page is not an integer, deliver first page.
#             catprodata = paginator.page(1)
#         except EmptyPage:
#             # If page is out of range (e.g. 9999), deliver last page of results.
#             catprodata = paginator.page(paginator.num_pages)
#
#         proimgdata = PRODUCTIMAGE.objects.filter(PRODUCTID=id)
#         context = {
#             "pdata": checkdp,
#             "cat": catdata,
#             "cdata": catprodata,
#             "pidata": proimgdata,
#         }
#         return render(request, 'shop.html', context)
#     except Exception as e:
#         pass
#
#     return render(request, 'shop.html', context)

def inquiry(request):
    uid = request.session["logid"]
    catdata = CATEGORY.objects.all()
    pid = request.POST.get("productid")
    inqdata = PRODUCTINQUIRY.objects.filter(USERID=uid)
    prodata = PRODUCT.objects.get(id=pid)
    context = {
        "indata": inqdata,
        "proiddata": prodata,
        "cat": catdata
    }
    if request.method == "POST":
        pid = request.POST.get("productid")
        try:
            uid = request.session["logid"]
            checkdp = LOGIN.objects.get(id=uid)
            catdata = CATEGORY.objects.all()
            inqdata = PRODUCTINQUIRY.objects.filter(USERID=uid)
            prodata = PRODUCT.objects.get(id=pid)
            context = {
                "pdata": checkdp,
                "cat": catdata,
                "indata": inqdata,
                "proiddata": prodata,
            }
            return render(request, 'productinquiry.html',context)
        except:
            pass
        return render(request,'productinquiry.html',context)
    return render(request,'productinquiry.html',context)

def inquirydata(request):
    uid = request.session["logid"]
    uname = request.session["logname"]
    proid = request.POST.get("pid")
    cquantity = request.POST.get("username")
    cbudget = request.POST.get("ubudget")
    cmsg = request.POST.get("message")

    print(proid)
    storedata = PRODUCTINQUIRY(USERID=LOGIN(id=uid),PRODUCTID=PRODUCT(id=proid),QUANTITY=cquantity,BUDGET=cbudget,MESSAGE=cmsg)
    storedata.save()
    email_content = f"Product: {proid}\nQuantity: {cquantity}\nBudget: {cbudget}\nMessage: {cmsg}"
    subject = f"Inquiry from {uname}"
    if request.method == 'POST':
        send_mail(
            subject,  # title
            email_content,
            # message
            'settings.EMAIL_HOST_USER',  # sender if not avalaible considered the
            ['pavitradesai1607@gmail.com'],  # reciver email
            fail_silently=False)
        messages.success(request, "Response Recorded")
        return redirect(indexpage)
    return render(request,'productinquiry.html')

def feadbackdata(request):
    fmessage = request.POST.get("ymessage")
    fname = request.POST.get("yname")
    fproid = request.POST.get("ypid")

    storefeadback = feedback(message=fmessage,name=fname,productid=PRODUCT(id=fproid))
    storefeadback.save()
    return redirect('/shop-details.html')

def searchdata(request):
    searchname = request.POST.get("searchfield")
    storesearchdata = PRODUCT.objects.filter(NAME__contains=searchname)
    catdata = CATEGORY.objects.all()
    context = {
        "cdata": storesearchdata,
        "cat": catdata
    }
    try:
        searchname = request.POST.get("searchfield")
        storesearchdata = PRODUCT.objects.filter(NAME__contains=searchname)
        uid = request.session["logid"]
        checkdp = LOGIN.objects.get(id=uid)
        catdata = CATEGORY.objects.all()
        context = {
            "cdata": storesearchdata,
            "pdata": checkdp,
            "cat": catdata
        }
        return render(request, 'search.html', context)
    except:
        pass
    return render(request,'search.html',context)

def changepasswordpage(request):
    return render(request,'changepassword.html')


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.http import HttpResponse
from .models import LOGIN


def change_password(request):
    if request.method == 'POST':
        old_password = request.POST.get('opsw')
        new_password = request.POST.get('npsw')
        confirm_password = request.POST.get('cpsw')

        # Assuming the user is authenticated and their ID is stored in session
        user_id = request.session["logid"]
        if user_id:
            try:
                user = LOGIN.objects.get(id=user_id)

                print(user)
                print(old_password)
                print(user.PASSWORD)
                print(new_password)
                print(confirm_password)

                # Check if old password matches


                if old_password == user.PASSWORD:
                    # Old password matches, update with new password
                    if new_password == confirm_password:
                        print("hello")
                        user.PASSWORD = new_password
                        user.save()
                        # Redirect to some success page
                        return redirect(logout)
                    else:
                        error_message = "New password and confirm password don't match."
                else:
                    error_message = "Old password entered is incorrect."

            except LOGIN.DoesNotExist:
                pass  # Handle user not found error
        else:
            pass  # Handle user not authenticated error

        # If the execution reaches here, it means there was an error, so render the form again with error message
        return render(request, 'changepassword.html', {'error_message': error_message})

    else:
        # GET request, render the form
        return render(request, 'changepassword.html')


def forgotpassword(request):
    return render(request,"forgotpwd.html")


def forgotpwd(request):
    if request.method == 'POST':
        username = request.POST.get('uemail')

        try:
            user = LOGIN.objects.get(EMAIL=username)

        except LOGIN.DoesNotExist:
            user = None

        if user is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'rahulinfolabz@gmail.com',
                [username],
                fail_silently=False,
            )

            #now update the password in model
            cuser = LOGIN.objects.get(EMAIL=username)
            cuser.PASSWORD = password
            cuser.save(update_fields=['PASSWORD'])

            messages.info(request, 'mail is sent successfully to your registered email')
            return redirect(indexpage)
        else:
            messages.info(request, 'This account does not exist')
    return redirect(indexpage)



