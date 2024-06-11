from django.shortcuts import render
from member.models import Member
from member.forms import Ajout_member

# AFFICHAGE DE LA LISTE DES MEMBRES
def list_members(request):
    members = Member.objects.all()
    return render(request, 'member/list_members.html',
                  {'members': members})

# CREATION D'UN NOUVEAU MEMBRE
def ajout_member(request):
    if request.method == 'POST':
        ajoutmember = Ajout_member(request.POST)
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
        ajoutmember = Ajout_member()
        return render(request,'member/ajout_member.html',
                    {'ajoutmembre': ajoutmember})
        


