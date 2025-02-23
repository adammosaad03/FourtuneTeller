from django.shortcuts import render
import random
# Create your views here.
  
def fortune(request):
  fortune = random.choice(fortuneList)
  return render(request, "randomfortune/fortune.html", context)
fortuneList = [
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
  "You will be successfull",
]  
context = {
  "fortune": fortune
}
