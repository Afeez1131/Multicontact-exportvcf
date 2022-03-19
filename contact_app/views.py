from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .utils import make_vcard

# Create your views here.
def HomeView(request):
    number_list = list()
    if request.method == 'POST':
        # numbers = request.POST.get('contacts')
        numbers = (request.POST['contacts'])
        group_name = request.POST['group_name']

        numbers_list = list(numbers.split(','))
        for number in numbers_list:
            number_list.append(number.replace(' ', ''))

        file_name = group_name + "-contact.vcf"
        response = HttpResponse(content_type="text/x-vCard")
        response["Content-Disposition"] = 'attachment; filename="%s"' % file_name

        vcard_list = list()  # the vcard obj dict.
        c = 0

        for number in range(len(number_list)):
            vcard = make_vcard(group_name + ' ' + str(number), number_list[number])
            # convert the k, v into vcard object
            vcard_list.append(vcard)
            # append the vcard obj to a list
            c += 1
        print('VCARD ', vcard_list)
        for line in vcard_list:
            # get the first list
            response.writelines([l + "\n" for l in line])

        return response

    else:
        return render(request, 'home.html', {})




'''def export_all_contact(contacts, group_name):
    file_name = str(group_name) + "-contact.vcf"
    response = HttpResponse(content_type="text/x-vCard")
    response["Content-Disposition"] = 'attachment; filename="%s"' % file_name

    vcard_list = list()  # the vcard obj dict.
    c = 0

    for number in range(len(contacts)):
        vcard = make_vcard(group_name + ' ' + str(number), contacts[number])
        # convert the k, v into vcard object
        vcard_list.append(vcard)
    # append the vcard obj to a list
        c += 1

    for line in vcard_list:
        # get the first list
        response.writelines([l + "\n" for l in line])

    return response'''
