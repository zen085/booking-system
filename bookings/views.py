from django.http  import JsonResponse
from .services import check_available_slots
from datetime import datetime,date
from django.shortcuts import render,redirect,get_object_or_404
from .forms import BookingOrdersForm
from home_page.models import Service
from .models import Order 
from django.contrib.auth.decorators import login_required
import json
from notifications.services import create_order,cancel_order,confirmed_order

@login_required
def api(request):
    date_str = request.GET.get('date')
    if not date_str:
        return JsonResponse({"error":"No date was provided"},status=400)
    try:
        selected_date =  datetime.strptime(date_str, "%Y-%m-%d").date()
    except Exception as e:
        return JsonResponse({f"error":str(e)})
    
    today = date.today()
    if selected_date < today:
        return JsonResponse({"error":"past dates are not allowed"},status=400)
    
    if selected_date > today.replace(year=today.year + 1):
        return JsonResponse({"error": "Cannot book more than 1 year ahead"}, status=400)

    slots = check_available_slots(selected_date)
    return JsonResponse({
        "slots":[slot.strftime("%H:%M")for slot in slots]
        })


@login_required
def booking(request,service_id):
    request.session["service_id"] = service_id
    return redirect("bookings:time_slots")


@login_required
def save_slot(request):

    if request.method != "POST":
        return JsonResponse({"success":False})
    else:
        data = json.loads(request.body)
        request.session["service_id"] = data.get("service_id")
        request.session["booking_date"] = data.get("date")
        request.session["booking_time"] = data.get("time")
        return JsonResponse({"success":True})
    

@login_required
def auto_form(request):

    print("SESSION DEBUG:",
          request.session.get('service_id'),
          request.session.get('booking_date'),
          request.session.get('booking_time'))

    service_id = request.session.get('service_id')
    session_date = request.session.get('booking_date')
    session_time = request.session.get('booking_time')

    context = {
        "service_id": service_id,
        "session_date": session_date,
        "session_time": session_time,
    }

    return render(request, "booking.html", context)

@login_required
def time_slots(request):
    service_id = request.session.get("service_id")
    context = {"service_id":service_id}
    return render(request,'get_slots.html',context)

@login_required
def book_form(request):
    service_id = request.session.get('service_id')
    session_date = request.session.get('booking_date')
    session_time = request.session.get('booking_time')

    if not service_id:
        return redirect("home_page:home")
    
    service = Service.objects.get(id=service_id)

    if request.method != "POST":
        form = BookingOrdersForm(initial={
            'date':session_date,
            'time':session_time
        })
        
    else:
        form = BookingOrdersForm(request.POST)
        if form.is_valid():
            create_order(
                user=request.user,
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                phone=form.cleaned_data["phone"],
                service=service,
                date=session_date,
                time=session_time,
                notes=form.cleaned_data["notes"]
                

            )
            return redirect('bookings:my_bookings')
    
    context = {
        "form":form,
        "service":service,
        "session_date":session_date,
        "session_time":session_time
    }

    return render(request,"booking.html",context)
    
      

@login_required
def my_bookings(request):
    status = request.GET.get("status")
    bookings = Order.objects.filter(user=request.user)

    if status:
        bookings = bookings.filter(status=status)
    
    bookings = bookings.order_by('-date') 
    
    context = {"bookings":bookings,"status":status}
    return render(request,'my_bookings.html',context)

@login_required
def completed_order(request,booking_id):
    booking = Order.objects.get(id=booking_id)    
    confirmed_order(booking)
    return render(request,'my_bookings.html')


   
        

@login_required
def cancel_booking(request,booking_id):
    booking = get_object_or_404(Order,id=booking_id,user=request.user)
    cancel_order(booking)
    return redirect('bookings:my_bookings')







