from django.shortcuts import render
from member.models import Member
from member.forms import Ajoutmember, Updatemember


# AFFICHAGE DE LA LISTE DES MEMBRES
def list_members(request):
    members = Member.objects.all()
    return render(request, 'member/list_members.html',
                  {'members': members})


# CREATION D'UN NOUVEAU MEMBRE
def ajout_member(request):
    if request.method == 'POST':
        ajoutmember = Ajoutmember(request.POST)
        if ajoutmember.is_valid():
            member = Member()
            member.first_name = ajoutmember.cleaned_data['first_name']
            member.last_name = ajoutmember.cleaned_data['last_name']
            member.email = ajoutmember.cleaned_data['email']
            member.save()
            members = Member.objects.all()
            return render(request,'member/list_members.html',
                        {'members': members})
    else:
        ajoutmember = Ajoutmember()
        return render(request,'member/ajout_member.html',
                    {'ajoutmembre': ajoutmember})
    

# MISE A JOUR D'UN MEMBRE   
def update_member(request, id):
    if request.method == 'POST':
        member = Member.objects.get(pk=id)
        updatemember = Updatemember(request.POST)
        if updatemember.is_valid():
            member.first_name = updatemember.cleaned_data['first_name']
            member.last_name = updatemember.cleaned_data['last_name']
            member.email = updatemember.cleaned_data['email']
            member.save()
            members = Member.objects.all()
            return render(request,'member/list_members.html',
                        {'members': members})
    else:
        updatemember = Updatemember()
        return render(request,'member/update_member.html',
                    {'updatemember': updatemember})

        


