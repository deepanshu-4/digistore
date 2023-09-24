from .models import fpPost, fPostpdf
from .models import pPost, Postpdf
from .models import Post, PostImage
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from data.models import Contact, listing
import random
from .encryption_util import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
from datetime import datetime
import webbrowser
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import smtplib
# Create your views here
from django.contrib import messages
from django.shortcuts import get_object_or_404

from data.models import Contact, video
def about(request):
    if request.user.is_anonymous:
        request.session['lv'] = 1
        return redirect('/data/login')
    else:
        x = request.user.email
        y = request.user
        y = str(y)
        if request.method == "POST":

            vid = request.POST.get('vid')

            vi = video(username=y, video=vid)
            vi.save()
        x = str(x)
        im = Contact.objects.all()
        imo = Contact.objects.filter(username=request.user.username)
        for i in imo:
            im = i.name
        print(imo)
        vim = video.objects.all()
        try:
            if (imo.count() == 0):
                im = "admin"
        except:
            im = i.name

        return render(request, 'data/mabout.html', {
            'im': im,
            'x': x,
            "vim": vim,
            "y": y,
            "imo": im
        })


def yvideo(request):
    if request.user.is_anonymous:
        request.session['lv'] = 1

        return redirect('/data/login')
    else:
        x = request.user.email
        y = request.user
        y = str(y)
        if request.method == "POST":

            vid = request.POST.get('vid')

            vi = video(username=y, video=vid)
            vi.save()
        x = str(x)
        im = Contact.objects.all()
        vim = video.objects.all()
        return render(request, 'data/about.html', {
            'im': im,
            'x': x,
            "vim": vim,
            "y": y
        })


def gallery(request):
    if request.user.is_anonymous:
        request.session['lv'] = 1

        return redirect('/data/login')
    else:
        x = request.user.email
        y = request.user
        y = str(y)
        x = str(x)
        im = Contact.objects.all()
        return render(request, 'data/gabout.html', {
            'im': im,
            'x': x,
            "y": y
        })


def fun(c):
    try:

        a = random.randint(25000, 90000)
        s = str(a)
        send_mail(
            'Your OTP',
            s,
            'dk2184814@gmail.com',
            [c],
            fail_silently=False,
        )
        return 1, s
    except Exception as e:

        return 0, -5


def like(request, id):
    lists = listing.objects.get(id=id)
    lists.like = str(int(lists.like)+1)
    lists.save()
    x = lists.like

    return HttpResponse(x)


def dlike(request, id):
    lists = listing.objects.get(id=id)
    lists.dislike = str(int(lists.dislike)+1)
    lists.save()
    x = lists.dislike

    return HttpResponse(x)


@login_required
def addtolist(request, id):
    link = request.POST.get('shnm')
    listing(puser=str(request.user), image=link,
            like=str(0), dislike=str(0)).save()
    return redirect('/data/')


def deletefromlist(request, id):
    lists = listing.objects.filter(id=id)
    lists.delete()
    return redirect('/data/')


def index(request):
    request.session['ym'] = ""
    request.session['lv'] = 0
    if request.user.is_anonymous == False:
        lists = reversed(listing.objects.all())
        request.session['ym'] = str(request.user)
        ym = request.session['ym']

        return render(request, "data/home.html", {
            'ym': ym,
            'lists': lists
        })
    else:
        request.session['ym'] = ""
        return render(request, "data/home.html", {
            'ym': request.session['ym']
        })


def register(request):
    logout(request)
    if "email" and "name" and "phno" not in request.session:
        request.session["name"] = ""
        request.session["email"] = ""
        request.session["phno"] = ""
        request.session["message"] = "hello how are you"
        request.session["otp"] = ""
    return render(request, 'data/index.html')


def otp(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        phno = request.POST.get('phno')
        message = request.POST.get('message')
        request.session["uname"] = name
        request.session["email"] = email
        request.session["phno"] = phno
        num_results = Contact.objects.filter(email=email).count()
        num_results2 = User.objects.filter(username=name).count()
        print(num_results2)
        if (num_results >= 1):
            messages.success(request, "email already exist")
            return HttpResponseRedirect(request.path_info)
        if (num_results2 >= 1):
            messages.success(request, "user already exist")
            return HttpResponseRedirect(request.path_info)
        x, y = fun(email)
        request.session["otp"] = y
        request.session['nvar'] = 0
        if (int(y) < 0):
            request.session["otp"] = ""
        if (x != 1):
            messages.success(request, "Wrong credentials")
            return HttpResponseRedirect(request.path_info)
        request.session['var'] = 1
        return redirect('/data/newf')
    else:
        return redirect('/data')
    return redirect('/data')


def newf(request):
    try:

        if request.session['var']:
            request.session['var'] = 0
            return render(request, 'data/otp.html')
        return redirect('/data')
    except:
        return redirect('/data')


def checkotp(request):
    if request.method == "POST":
        name = request.POST.get('name')
        password = request.POST.get('Password')
        request.session['passw'] = password
        # confirmpassword=request.POST.get('conpass')
        otp = request.POST.get('otp')
        username = request.session["uname"]
        if (request.session["otp"] == otp):
            try:

                contact = Contact(username=username, name=name,
                                  email=request.session["email"], phoneno=request.session["phno"], date=datetime.today())
                user = User.objects.create_user(
                    username, request.session["email"], password)
                contact.save()
                messages.success(request, "account verified")
                u = User.objects.get(username=username)
                u.set_password(password)
                u.save()
                del request.session['email']
                request.session['otp'] = "-112s6a"
                return redirect('/data')
            except:
                print("error occured")
                messages.success(request, "user exist")
                request.session['otp'] = "-112s6a"
                return redirect('/data')

        else:
            messages.success(request, "account not  verified")
            # del request.session['otp']
            request.session['otp'] = "-112s6a"
            return redirect('/data')

    else:
        return redirect('/data')


def log_in(request):
    # if user.is_active:
    #     logout(request)
    #     login(request, user)
    if request.user.is_anonymous:

        if (request.method == "POST"):
            username = request.POST.get('logname')
            password = request.POST.get('pasword')
            user = authenticate(request, username=username, password=password)
            if user is not None:

                login(request, user)
                if (request.session['lv'] == 1):
                    request.session['lv'] = 0
                    return redirect('/data/about')
                messages.success(request, "Successfully logged in")
                return redirect('/data')
                # Redirect to a success page.

            else:
                messages.success(request, "not valid user name or password")
                return redirect('/data')

                # Return an 'invalid login' error message.
        return render(request, 'data/login.html')
    else:
        messages.success(request, "logged in")
        return redirect('/data')


def log_out(request):
    logout(request)
    return redirect('/data')


@login_required
def blog_view(request):
    posts = Post.objects.all()
    y = request.user
    y = str(y)
    return render(request, 'data/blog.html', {
        'posts': posts,
        'y': y
    })


@login_required
def detail_view(request, id):
    num = Post.objects.filter(guser=str(request.user))
    request.session['id'] = id
    post = get_object_or_404(num, id=id)
    # print(post)
    yid = request.user
    y = id
    photos = PostImage.objects.filter(post=post)
    # print(photos)
    try:
        photos = PostImage.objects.filter(post=post)
        ln = len(photos)
    except:
        ln = None
    return render(request, 'data/detail.html', {
        'post': post,
        'photos': photos,
        'y': y,
        "yid": str(yid),
        "ln": ln
    })


@login_required
def addimage(request, id):
    fie = request.FILES.get('file')
    print(fie)
    # fie=request.GET.get('file') it is wrong
    y = request.user
    y = str(y)
    post = Post.objects.filter(id=id)
    print(post)
    for p in post:
        image = PostImage(post=p, images=fie)

        image.save()

    return redirect('/data/'+str(request.session['id']))


@login_required
def addfolder(request):
    if (request.method == 'GET'):
        tit = request.GET.get('tile')
        ns = Post.objects.filter(title=tit).count()
        # print(tit)

        # print(ns)
        if (ns == 0):
            pst = Post(title=tit, guser=str(request.user))
            pst.save()
    return redirect('/data/blog')

# delete video and image


def delete(request, id):
    if request.method == "POST":
        video.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/yvideo')


def deleteimage(request, id):
    if request.method == "POST":
        PostImage.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/'+str(request.session['id']))


def deletefolder(request, id):
    if request.method == "POST":
        Post.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/blog')


# for pdf


@login_required
def pblog_view(request):
    posts = pPost.objects.all()
    y = request.user
    y = str(y)
    return render(request, 'data/pblog.html', {
        'posts': posts,
        'y': y
    })


@login_required
def pdetail_view(request, id):
    num = pPost.objects.filter(guser=str(request.user))
    request.session['pid'] = id
    post = get_object_or_404(num, id=id)
    # print(post)
    yid = request.user
    y = id
    photos = Postpdf.objects.filter(post=post)
    try:
        photos = Postpdf.objects.filter(post=post)
        ln = len(photos)
    except:
        ln = None
    # print(photos)
    return render(request, 'data/pdetail.html', {
        'post': post,
        'photos': photos,
        'y': y,
        "yid": str(yid),
        "ln": ln
    })


@login_required
def addpdf(request, id):
    fie = request.FILES.get('file')
    print(fie)
    # fie=request.GET.get('file') it is wrong
    y = request.user
    y = str(y)
    post = pPost.objects.filter(id=id)
    print(post)
    for p in post:
        pdf = Postpdf(post=p, pdf=fie)

        pdf.save()

    return redirect('/data/p/'+str(request.session['pid']))


@login_required
def paddfolder(request):
    tit = request.GET.get('tile')
    ns = pPost.objects.filter(title=tit).count()
    print(ns)
    if (ns == 0):
        pst = pPost(title=tit, guser=str(request.user))
        pst.save()
    return redirect('/data/pblog')


def deletepdf(request, id):
    if request.method == "POST":
        Postpdf.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/p/'+str(request.session['pid']))


def pdeletefolder(request, id):
    if request.method == "POST":
        pPost.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/pblog')


def listen(request, id, id1):
    sng = Postpdf.objects.filter(id=id1)
    for i in sng:
        x = str(i.pdf)
        z = x[-1:-4:-1]
        z = z[::-1]
    if (z != "mp3" and z != "mp4" and z != "wma" and z != "wav"):
        return HttpResponse("not a song ")

    nums = pPost.objects.filter(guser=str(request.user))
    post = get_object_or_404(nums, id=id)
    # print(post)
    yid = request.user
    y = id
    sngl = Postpdf.objects.filter(post=post)
    # print(photos)
    return render(request, 'data/ipad.html', {
        'sng': sng,
        'sngl': sngl
    })


# for files


@login_required
def fpblog_view(request):
    posts = fpPost.objects.all()
    post = fpPost.objects.filter(guser=str(request.user))

    y = request.user
    y = str(y)
    return render(request, 'data/fpblog.html', {
        'posts': posts,
        'y': y,

    })


@login_required
def fpdetail_view(request, id):
    num = fpPost.objects.filter(guser=str(request.user))
    request.session['fpid'] = id
    post = get_object_or_404(num, id=id)
    # print(post)

    yid = request.user
    y = id
    try:
        photos = fPostpdf.objects.filter(post=post)
        ln = len(photos)
    except:
        ln = None
    return render(request, 'data/fpdetail.html', {
        'post': post,
        'photos': photos,
        'y': y,
        "yid": str(yid),
        'ln': ln
    })


@login_required
def faddpdf(request, id):
    fie = request.FILES.get('file')
    print(fie)
    # fie=request.GET.get('file') it is wrong
    y = request.user
    y = str(y)
    post = fpPost.objects.filter(id=id)
    print(post)
    for p in post:
        pdf = fPostpdf(post=p, pdf=fie)

        pdf.save()

    return redirect('/data/fp/'+str(request.session['fpid']))


@login_required
def fpaddfolder(request):
    tit = request.GET.get('tile')
    # pst=fpPost(title=tit,guser=str(request.user))
    ns = fpPost.objects.filter(title=tit).count()
    if (ns == 0):
        pst = fpPost(title=tit, guser=str(request.user))
        pst.save()
    return redirect('/data/fpblog')


def fdeletepdf(request, id):
    if request.method == "POST":
        fPostpdf.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/fp/'+str(request.session['fpid']))


def fpdeletefolder(request, id):
    if request.method == "POST":
        fpPost.objects.filter(id=id).delete()
        return HttpResponseRedirect('/data/fpblog')


@login_required
def resetutil(request):
    if (request.method == "POST"):
        y = str(request.user)
        print(y)
        u = User.objects.get(username=y)
        password = request.POST.get('opas')
        npas = request.POST.get('rpas')
        user = authenticate(request, username=y, password=password)
        if user is not None:
            print(password, npas)
            hashv = encrypt(y)+"/"+encrypt(password)+"/"+encrypt(npas)
            weblink = "http://digistorage.herokuapp.com/data/reset/"+hashv
            print(weblink)
            request.session['email_text'] = weblink
            try:
                a = random.randint(25000, 90000)
                s = str(a)
                send_mail(
                    'Password reset link',
                    request.session['email_text'],
                    'dk2184814@gmail.com',
                    [u.email],
                    fail_silently=False,
                )
            except Exception as e:
                messages.success(request, "Some error occured in sending mail")
                return redirect('/data')
            messages.success(request, "check your mail")
            return redirect('/data')
            # Redirect to a success page.
        else:
            messages.success(request, "not valid password")
            return redirect('/data')
    return render(request, 'data/reset.html')


def reset(request, a, b, c):
    try:
        a = decrypt(a)
        b = decrypt(b)
        c = decrypt(c)
        print("values", a, b, c)
        u = User.objects.get(username=str(request.user))
        user = authenticate(request, username=str(request.user), password=b)
        print(user)
        if user is not None:
            u.set_password(c)
            u.save()
            messages.success(request, "Password change successhul")
            return redirect('/data')
        else:
            messages.success(request, "Not allowed")
            return redirect('/data')
    except:
        messages.success(request, "Not allowed")
        return redirect('/data')


def forget(request):
    if request.method == "POST":
        a = request.POST.get('flogin')
        b = request.POST.get('femail')
        c = request.POST.get('fpass')
        u = User.objects.get(username=a)
        if (u.email == b):
            if True:
                hashv = encrypt(a)+"/"+encrypt(b)+"/"+encrypt(c)
                weblink = "http://digistorage.herokuapp.com/data/changepassword/"+hashv
                print(weblink)

                request.session['slink'] = weblink
                # message = 'Subject: {}\n\n{}'.format(subject,email_text)
                try:

                    a = random.randint(25000, 90000)
                    s = str(a)
                    send_mail(
                        'Change the Password',
                        request.session['slink'],
                        'dk2184814@gmail.com',
                        [u.email],
                        fail_silently=False,
                    )

                    messages.success(request, "Reset request send to mail")
                    return redirect('/data')
                except Exception as e:
                    messages.success(
                        request, "Some error occured in sending mail")
                    return redirect('/data')
                return redirect('/data')
                # Redirect to a success page.

        else:
            messages.success(request, "not registered email")
            return redirect('/data')

    return render(request, 'data/forget.html')


def forgetutil(request, a, b, c):
    try:

        a = decrypt(a)
        b = decrypt(b)
        c = decrypt(c)
        # print("values",a,b,c)
        u = User.objects.get(username=a)
        if True:
            u.set_password(c)
            u.save()
            messages.success(request, "Password change successful")
            return redirect('/data')
        else:
            messages.success(request, "Not allowed")
            return redirect('/data')
    except:
        messages.success(request, "Not allowed")
        return redirect('/data')
