from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from django.utils.crypto import get_random_string
from django.contrib import messages
  # the index function is called when root is visited
initial_random = get_random_string(length=15)
def index(request):
    context = { 
        #declare variables
        "products" : {'T-Shirt' : '1001' ,'Sweater' : '1002','Cup' : '1003' ,'Algorithm-Book' : '1004','Potato' : '1005'},
        "price" : { '$19.99':'1001', '$29.99' : '1002', '$4.99' : '1003', '$49.99' : '1004', '$0.001' : '1005'},
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    request.session['context'] = context
    print(request.session['context']['time'])
    return render(request, "django_app\index.html", context)
def result(request):
    return render(request,'django_app\info.html')
def generate(request):
    if 'initial' in request.session:
        request.session['initial'] = False
        print('TOTAL_PURCHASES::', request.session['amount_total_overall'])
    else:
        request.session['initial'] = True
        request.session['form_number'] = 0
        request.session['num_items'] = 0
        request.session['amount_total_overall'] = 0
        request.session['amount_total_this_purchase'] = 0
        print('INITIALIZED')
    if request.method == "POST":
        #form count
        request.session['form_number'] += 1
        #flashes
        message_string = 'you have submitted this form ' + str(request.session['form_number']) + ' times'
        messages.add_message(request, messages.INFO, message_string)
        #logic
        # iterPost = iter(request.POST.items())
        # print('iterate through::',iterPost)
        # next(iterPost)
        for post_key, post_value in request.POST.items(): #items() gives keys and values of the key value pairs
            print('POST_ELEMENT::',post_key,post_value)
            if post_key == 'T-Shirt' or post_key == 'Sweater' or post_key == 'Cup' or post_key == 'Algorithm-Book':
                this_post = int(request.POST[post_key])
                request.session['num_items'] += this_post
                for product_key, product_value in request.session['context']['products'].items():
                    print('PRODUCT_ELEMENT::',product_key,product_value)
                    if post_key == product_key:
                        this_ID = product_key
                        print('MATCHED_ID')
                        for price_key, price_value in request.session['context']['price'].items(): #iterating through each dictionary in context to find the right data
                            print('PRICE_ELEMENT::',price_key,price_value)
                            if price_value == this_ID:
                                print('MATCHED_PRICE')
                                request.session['amount_total_this_purchase'] += int(price_key) #adds up all the purchases in POST
        request.session['amount_total_overall'] += request.session['amount_total_this_purchase']
        return redirect("/result")
    else:
        return redirect("/")



def show(request, number):
    response = "Placeholder to display blog "+str(number)
    return HttpResponse(response)
def edit(request, number):
    response = "placeholder to edit blog "+str(number)
    return HttpResponse(response)
def destroy(request):
    request.session.clear()
    return redirect('/')
# views.py

