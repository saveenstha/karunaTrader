from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, TemplateView
from .models import Buyer, OwnerDetails
from transactions.models import Transaction
from .forms import BuyerForm, EditBuyerForm, EditBuyerProfileForm
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


# Create your views here.
def home(request):
    return render('login')



def index(request):
    return render(request, 'kTradersApp/index.html')


def index2(request):
    return render(request, 'kTradersApp/index2.html')

# # @login_required
# class Dashboard(ListView):
#     model = Transaction
#     template_name = 'kTradersApp/dashboard.html'
#     paginate_by = 2
#
#     def get_context_data(self, *args, **kwargs):
#         txn_list = Transaction.objects.all().order_by('-bill_number')
#         paginator = Paginator(txn_list, self.paginate_by)
#
#         page_number = self.request.GET.get('page')
#
#         page_obj = paginator.get_page(page_number)
#
#         context = {'txn_list': txn_list,'page_obj': page_obj}
#         return context


class BuyerProfileDetailView(DetailView):
    model = Buyer
    template_name = 'kTradersApp/buyer/buyer_profile.html'

    def get_context_data(self, *args, **kwargs):
        context = super(BuyerProfileDetailView, self).get_context_data(*args, **kwargs)
        company_data = Buyer.objects.filter(pan_num=self.object.pk)
        context["buyer"] = company_data.values()[0]
        if OwnerDetails.objects.filter(pan_num=self.object.pk).exists():
            context["owner"] = OwnerDetails.objects.filter(pan_num=self.object.pk).values()[0]
        context["buyers_txn"] = Transaction.objects.filter(buyer=self.object.pk).order_by()
        # context["particulars"] = ParticularsDetail.objects.all()

        return context


class AllBuyersView(ListView):
    model = Buyer
    template_name = 'kTradersApp/contacts.html'


class BuyerListView(ListView):
    model = Buyer
    template_name = 'kTradersApp/buyer_list.html'
    # context_object_name = 'buyers_with_owners'
    context_object_name = 'buyers'


    def get_queryset(self):
        return Buyer.objects.prefetch_related('ownerdetails_set').all()


class BuyerCreateView(CreateView):
    model = Buyer
    form_class = BuyerForm
    template_name = 'kTradersApp/buyer/add_buyer.html'
    success_url = reverse_lazy('buyer-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

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


# # Repeat similar structure for others
#
# class FarmerListView(LoginRequiredMixin, ListView):
#     model = Farmer
#     template_name = 'kTradersApp/farmer_list.html'
#     context_object_name = 'farmers'
#
# class FarmerCreateView(LoginRequiredMixin, CreateView):
#     model = Farmer
#     form_class = FarmerForm
#     template_name = 'kTradersApp/form.html'
#     success_url = reverse_lazy('farmer-list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'kTradersApp/product_list.html'
#     context_object_name = 'products'
#
# class ProductCreateView(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'kTradersApp/form.html'
#     success_url = reverse_lazy('product-list')
#
# class PurchaseListView(LoginRequiredMixin, ListView):
#     model = Purchase
#     template_name = 'kTradersApp/purchase_list.html'
#     context_object_name = 'purchases'
#
# class PurchaseCreateView(LoginRequiredMixin, CreateView):
#     model = Purchase
#     form_class = PurchaseForm
#     template_name = 'kTradersApp/form.html'
#     success_url = reverse_lazy('purchase-list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
#
# class SaleListView(LoginRequiredMixin, ListView):
#     model = Sale
#     template_name = 'kTradersApp/sale_list.html'
#     context_object_name = 'sales'
#
# class SaleCreateView(LoginRequiredMixin, CreateView):
#     model = Sale
#     form_class = SaleForm
#     template_name = 'kTradersApp/form.html'
#     success_url = reverse_lazy('sale-list')
#
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)