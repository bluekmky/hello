from django.shortcuts import render
import random

# Create your views here.
def gamemain(request):
    return render(request, "game/gamemain.html")

def game(request):  
    # inn = 유저가 입력한 수
    inn = request.GET['gamenum']
    ran_num = random.randint(0, 1)
             
    # 게임 진행
    if inn == str(ran_num):
        outnum = ran_num
        message = "이겼"
        return render(request, "game/gameend.html", {'message' : message, 'outnum' : outnum, 'innum' : inn})
    
    else:
        outnum = ran_num
        message = "졌"
        return render(request, "game/gameend.html", {'message' : message, 'outnum' : outnum, 'innum' : inn})