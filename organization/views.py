from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .forms import OrganizationForm, Special_eventForm, UserForm
from .models import Organization, Special_event

# AUDIO_FILE_TYPES = ['wav', 'mp3', 'ogg']


# this is represent which type of image file alow to run progrrame
IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

 # add organization in section work properly
def create_organization(request):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        form = OrganizationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            organization = form.save(commit=False)
            organization.user = request.user
            organization.organization_logo = request.FILES['organization_logo']
            file_type = organization.organization_logo.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'organization': organization,
                    'form': form,
                    'error_message': 'Image file must be PNG, JPG, or JPEG',
                }
                return render(request, 'organization/create_organization.html', context)
            organization.save()
            return render(request, 'organization/detail.html', {'organization': organization})
        context = {
            "form": form,
        }
        return render(request, 'organization/create_organization.html', context)

# this is a section which is active when i want to input information data 
# as organization event update
# which is control by admin pannel .it is off nonal way
def create_special_event(request, organization_id):
    form = special_eventForm(request.POST or None, request.FILES or None)
    organization = get_object_or_404(Organization, pk=organization_id)
    if form.is_valid():
        organizations_special_events = organization.special_event_set.all()
        for s in organizations_special_events :
            if s.topic == form.cleaned_data.get("special_event_topic"):
                context = {
                    'organization': organization,
                    'form': form,
                    'error_message': 'You already added that special_event',
                }
                return render(request, 'organization/create_special_event.html', context)
        special_event = form.save(commit=False)
        special_event.organization = organization
        # special_event.audio_file = request.FILES['audio_file']
        # file_type = special_event.audio_file.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in AUDIO_FILE_TYPES:
        #     context = {
        #         'organization': organization,
        #         'form': form,
        #         'error_message': 'Audio file must be WAV, MP3, or OGG',
        #     }
        #     return render(request, 'organization/create_special_event.html', context)

        special_event.save()
        return render(request, 'organization/detail.html', {'organization': organization})
    context = {
        'organization': organization,
        'form': form,
    }
    return render(request, 'organization/create_special_event.html', context)



# this porsion is show the organization event detail in table click page
# go to a new page and update many different field

def event_detail(request,organization_id):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        user = request.user
        organization = get_object_or_404(Organization, pk=organization_id)
        return render(request, 'organization/event_detail.html', {'organization': organization, 'user': user})

# this thing is work in all organization when i want to 
# remove a particular organization on that area

def delete_organization(request, organization_id):
    organization = Organization.objects.get(pk=organization_id)
    organization.delete()
    organizations = Organization.objects.filter(user=request.user)
    return render(request, 'organization/index.html', {'organizations': organizations})

# this section allow remove event update on that occasion this part is 
# delect option is work their
def delete_special_event(request, organization_id, special_event_id):
    organization = get_object_or_404(organization, pk=organization_id)
    special_event = Special_event.objects.get(pk=special_event_id)
    special_event.delete()
    return render(request, 'organization/detail.html', {'organization': organization})
 # this section is related with the detail update on any organization event 
 # update their

def detail(request, organization_id):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        user = request.user
        organization = get_object_or_404(Organization, pk=organization_id)
        return render(request, 'organization/detail.html', {'organization': organization, 'user': user})

 # this section is represt the important section which is motivate
 # which organization is particularly important on that section is automaticlly 
 # start button
def favorite(request, special_event_id):
    special_event = get_object_or_404(Special_event, pk=special_event_id)
    try:
        if special_event.is_favorite:
            special_event.is_favorite = False
        else:
            special_event.is_favorite = True
        special_event.save()
    except (KeyError, Special_event.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def favorite_organization(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    try:
        if organization.is_favorite:
            organization.is_favorite = False
        else:
            organization.is_favorite = True
        organization.save()
    except (KeyError, Organization.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        organizations = Organization.objects.filter(user=request.user)
        special_event_results = Special_event.objects.all()
        query = request.GET.get("q")
        if query:
            organizations = organizations.filter(
                Q(organization_name__icontains=query) |
                Q(established__icontains=query)
            ).distinct()
            special_event_results =special_event_results.filter(
                Q(topic__icontains=query)
            ).distinct()
            return render(request, 'organization/index.html', {
                'organizations': organizations,
                'special_events': special_event_results,
            })
        else:
            return render(request, 'organization/index.html', {'organizations': organizations})

def about(request):
    return render(request,'organization/about.html')


def start(request):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        organizations = Organization.objects.filter(user=request.user)
        special_event_results = Special_event.objects.all()
        query = request.GET.get("q")
        if query:
            organizations = organizations.filter(
                Q(organization_name__icontains=query) |
                Q(established__icontains=query)
            ).distinct()
            special_event_results =special_event_results.filter(
                Q(topic__icontains=query)
            ).distinct()
            return render(request, 'organization/start.html', {
                'organizations': organizations,
                'special_events': special_event_results,
            })
        else:
            return render(request, 'organization/start.html', {'organizations': organizations})




def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'organization/login.html', context)

# this is section 
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                organizations = Organization.objects.filter(user=request.user)
                return render(request, 'organization/index.html', {'organizations': organizations})
            else:
                return render(request, 'organization/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'organization/login.html', {'error_message': 'Invalid login'})
    return render(request, 'organization/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                organizations = Organization.objects.filter(user=request.user)
                return render(request, 'organization/index.html', {'organizations': organizations})
    context = {
        "form": form,
    }
    return render(request, 'organization/register.html', context)


def special_events(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'organization/login.html')
    else:
        try:
            special_event_ids = []
            for organization in Organization.objects.filter(user=request.user):
                for special_event in organization.special_event_set.all():
                    special_event_ids.append(special_event.pk)
            users_special_events = Special_event.objects.filter(pk__in=special_event_ids)
            if filter_by == 'favorites':
                users_special_events = users_special_events.filter(is_favorite=True)
        except Organization.DoesNotExist:
            users_special_events = []
        return render(request, 'organization/special_events.html', {
            'special_event_list': users_special_events,
            'filter_by': filter_by,
        })
