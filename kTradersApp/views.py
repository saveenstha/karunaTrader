from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Buyer, Transaction, ParticularsDetail
from .forms import BuyerForm, EditBuyerForm, AddTransactionForm, AddParticularsForm
from django.urls import reverse_lazy


# Create your views here.
def home(request):
    return render('login')


def starter(request):
    return render(request, 'kTradersApp/starter.html')


def index(request):
    return render(request, 'kTradersApp/index.html')


def index2(request):
    return render(request, 'kTradersApp/index2.html')

@login_required
def dashboard(request):
    txn_list = Transaction.objects.all().order_by('-bill_number')
    context = {'txn_list': txn_list}
    return render(request, 'kTradersApp/dashboard.html', context)


class BuyerProfileDetailView(DetailView):
    model = Buyer
    template_name = 'kTradersApp/pages/buyer/buyer_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BuyerProfileDetailView, self).get_context_data(*args, **kwargs)
        context["buyers_info"] = Buyer.objects.all()
        context["buyers_txn"] = Transaction.objects.filter(pan_num=self.object.pk).order_by()
        context["particulars"] = ParticularsDetail.objects.all()
        return context


class AllBuyersView(ListView):
    model = Buyer
    template_name = 'kTradersApp/contacts.html'


class BuyerListView(ListView):
    model = Buyer
    template_name = 'kTradersApp/buyer_list.html'


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'kTradersApp/pages/buyer/add_buyer.html'


class BuyerUpdateView(UpdateView):
    model = Buyer
    form_class = EditBuyerForm
    template_name = 'kTradersApp/pages/buyer/update_buyer.html'


class BuyerDeleteView(DeleteView):
    model = Buyer
    template_name = 'kTradersApp/pages/buyer/delete_buyer.html'
    success_url = reverse_lazy('buyer-list')

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.success_url
            return HttpResponseRedirect(url)
        else:
            return super(BuyerDeleteView, self).post(request, *args, **kwargs)


class AddTransactionView(CreateView):
    model = Transaction
    form_class = AddTransactionForm
    template_name = 'kTradersApp/pages/buyer/add_transaction.html'


def AddParticulars(request):
    particularsFormSet = formset_factory(AddParticularsForm)

    if request.method == 'POST':
        form = AddTransactionForm(request.POST)
        formset = particularsFormSet(request.POST)
        if all([form.is_valid(), formset.is_valid]):
            txn = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    particular = inline_form.save(commit=False)
                    particular.particulars = txn
                    particular.save()
            return render(request, 'kTradersApp/dashboard.html', {})
    else:
        form = AddTransactionForm()
        formset = particularsFormSet()
    return render(request, 'kTradersApp/pages/buyer/add_transaction.html', {'form': form, 'formset': formset})
