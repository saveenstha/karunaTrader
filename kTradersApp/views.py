from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Buyer, OwnerDetails
from transactions.models import Transactions
from .forms import BuyerForm, EditBuyerForm, EditBuyerProfileForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render('login')


def starter(request):
    return render(request, 'kTradersApp/starter.html')


def index(request):
    return render(request, 'kTradersApp/index.html')


def index2(request):
    return render(request, 'kTradersApp/index2.html')

# @login_required
class Dashboard(ListView):
    model = Transactions
    template_name = 'kTradersApp/dashboard.html'
    paginate_by = 2
    def get_context_data(self, *args, **kwargs):
        txn_list = Transactions.objects.all().order_by('-bill_number')
        paginator = Paginator(txn_list, self.paginate_by)

        page_number = self.request.GET.get('page')

        page_obj = paginator.get_page(page_number)

        context = {'txn_list': txn_list,'page_obj': page_obj}
        return context





class BuyerProfileDetailView(DetailView):
    model = Buyer
    template_name = 'kTradersApp/buyer/buyer_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BuyerProfileDetailView, self).get_context_data(*args, **kwargs)
        company_data = Buyer.objects.filter(pan_num=self.object.pk)
        context["buyer"] = company_data.values()[0]
        if OwnerDetails.objects.filter(pan_num=self.object.pk).exists():
            context["owner"] = OwnerDetails.objects.filter(pan_num=self.object.pk).values()[0]
        context["buyers_txn"] = Transactions.objects.filter(pan_num=self.object.pk).order_by()
        # context["particulars"] = ParticularsDetail.objects.all()
        print("Balance", context["buyer"]["Balance"])
        return context


class AllBuyersView(ListView):
    model = Buyer
    template_name = 'kTradersApp/contacts.html'


class BuyerListView(ListView):
    model = Buyer
    template_name = 'kTradersApp/buyer_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BuyerListView, self).get_context_data(*args, **kwargs)
        context['owner'] = OwnerDetails.objects.select_related().all().values()
        print(context['owner'])
        return context

    # def get_queryset(self):
        # return OwnerDetails.objects.


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'kTradersApp/buyer/add_buyer.html'


class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = EditBuyerForm
    template_name = 'kTradersApp/buyer/update_buyer.html'

class BuyerProfileUpdateView(UpdateView):
    model = OwnerDetails
    form_class = EditBuyerProfileForm
    template_name = 'kTradersApp/buyer/update_owner_info.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset

    def get_queryset(self):
        return self.model.objects.filter(pan_num=self.kwargs['pk'])



class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'kTradersApp/buyer/delete_buyer.html'
    success_url = reverse_lazy('buyer-list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(BuyerDeleteView, self).post(request, *args, **kwargs)




