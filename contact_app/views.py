from django.shortcuts import render, redirect
from django.http import HttpResponse
import csv
from .utils import make_vcard
import re


def HomeView(request):
    number_list = list()
    validator = r'[\+234]\d{13}'
    if request.method == 'POST':
        # numbers = request.POST.get('contacts')
        numbers = (request.POST['contacts'])
        '''get the numbers from the post request '''
        group_name = request.POST['group_name']
        '''get the group name '''
        numbers_list = list(numbers.split(','))
        # split the numbers by ","
        for number in numbers_list:
            # loop through each number
            phone_number = number.replace(' ', '')
            # remove the space between the number
            match = re.search(validator, phone_number)
            # match the number with the validator above to check if it is a phone number or not
            if match:
                # if True, append to the number list
                number_list.append(phone_number)
            else:
                # else, skip it
                continue
        file_name = group_name + "-contact.vcf"     # name of the file
        response = HttpResponse(content_type="text/x-vCard")    # type, vcard
        response["Content-Disposition"] = 'attachment; filename="%s"' % file_name

        vcard_list = list()  # the vcard, i.e list of vcard containing each phone number and name.

        for number in range(len(number_list)):
            # for number in the range of the number list
            vcard = make_vcard(group_name + ' ' + str(number), number_list[number])
            ''' make a vcard for it, and append the current number in the number list we are to it
                so we can have distinct name.
            '''
            # convert the k, v into vcard object
            vcard_list.append(vcard)
            '''append each vcard to the vcard list'''
            # append the vcard obj to a list
        for line in vcard_list:
            ''' for each vcard in the vcard list, write the vcard to the vcf file and move to the next
                line after writing it.'''
            # get the first list
            response.writelines([l + "\n" for l in line])
        return response
        # return the file as response

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
