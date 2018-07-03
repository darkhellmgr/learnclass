import pyrebase
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import auth
from mainapp.forms import SchoolModelForm

config = {
    'apiKey': "AIzaSyBTCNgjJpStBaazWCTkn9WmOzRD1jHkTEY",
    'authDomain': "learning-management-7b9f2.firebaseapp.com",
    'databaseURL': "https://learning-management-7b9f2.firebaseio.com",
    'projectId': "learning-management-7b9f2",
    'storageBucket': "learning-management-7b9f2.appspot.com",
    'messagingSenderId': "482234388569"
}
firebase = pyrebase.initialize_app(config)


authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()


# User authentication

def sign(request):
    return render(request, "source/login.html")


def postsign(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")

    try:
        user = authe.sign_in_with_email_and_password(email, passw)
        userid = user['localId']
        # print(user['idToken'])
        adminid_list = (list(db.child('Users').child('admin').shallow().get().val()))
        if userid in adminid_list:
            session_id = user['idToken']  # making session for user
            request.session['uid'] = str(session_id)
            return render(request, "source/admin.html")
        else:
            message = "You are not authorized"
            return render(request, "source/login.html", {"messg": message})
    except RuntimeError:
        pass
        # message = "Invalid Credentials"
        # print(message)
        # return render(request, "source/login.html", {"messg": message})


def logout(request):
    auth.logout(request)
    return sign(request)


# For school form

def schoolform(request):
    form = SchoolModelForm()

    if request.method == 'POST':
        request.POST._mutable = True
        r = request.POST
        print(r)
        try:
            if form.is_valid:
                form = SchoolModelForm(request.POST)
                del r['csrfmiddlewaretoken']
                print(r)
                db.child("Schools").push(r)
                return render(request, 'source/admin.html')
            if 'Save_and_add_another' in request.POST:
                return render(request, 'source/form.html', {'form': form})
        except RuntimeError:
            pass

    return render(request, "source/form.html", {'form': form})




