from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404
import markdown
import json
import datetime
from django_datatables_view.base_datatable_view import BaseDatatableView
# Create your views here.


def index(request,):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request,'index.html',
        context={ 'name':'wenhe','post_list': post_list})


def detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', context={'post': post})


def leave(request):
    return render(request, 'leave.html')

def LeaveAdd(request):
    if request.method == 'POST':
        print(request.POST)

        data = request.POST

        lc = Leave_class.objects.get(id=data['req_class'])

        obj = Leave(req_name=data['req_name'],
                    req_date=datetime.datetime.now(),
                    depart_name=data['depart_name'],
                    position='test',
                    req_class=lc,
                    start_time=datetime.datetime.now(),
                    end_time=datetime.datetime.now(),
                    resion=data['resion'],
                    file_url='blank',)

        obj.save()
        result = {'status': 0, 'msg': '请求成功', 'data': [11, 22, 33, 44]}  # 假如传人的数据为一字典
        return HttpResponse(json.dumps(result), content_type='application/json')



def hello(request):
    return HttpResponse('hello dog')

def AuditPersonJson(request):
    response_data = [{'optionValue':'0','optionDisplay':'项目经理A'},
                     {'optionValue':'1','optionDisplay':'项目经理B'},
                     {'optionValue':'2','optionDisplay': '项目经理C'}]

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def ReqClassListJson(request):
    response_data = []
    leave_class_list = Leave_class.objects.all().order_by('id')
    for leav_class in leave_class_list:
        response_data.append({'optionValue':leav_class.id,'optionDisplay':leav_class.name})

    return HttpResponse(json.dumps(response_data), content_type="application/json")


class PostListJson(BaseDatatableView):
    # The model we're going to show
    model = Leave

    # define the columns that will be returned
    columns = ['req_name', 'req_date','depart_name','req_class','resion','start_time','end_time']


    # define column names that will be used in sorting
    # order is important and should be same as order of columns
    # displayed by datatables. For non sortable columns use empty
    # value like ''
    order_columns = ['req_name', 'req_date','depart_name','req_class','resion','start_time','end_time']

    # set max limit of records returned, this is used to protect our site if someone tries to attack our site
    # and make it return huge amount of data
    #max_display_length = 500

    def render_column(self, row, column):
        # We want to render user as a custom column
        if column == 'req_class':
            return '{0}'.format(row.req_class.name)
        else:
            return super(PostListJson,self).render_column(row, column)
    '''
    def filter_queryset(self, qs):
        # use parameters passed in GET request to filter queryset

        # simple example:
        search = self.request.GET.get(u'search[value]', None)
        if search:
            qs = qs.filter(name__istartswith=search)

        # more advanced example using extra parameters
        filter_customer = self.request.GET.get(u'customer', None)

        if filter_customer:
            customer_parts = filter_customer.split(' ')
            qs_params = None
            for part in customer_parts:
                q = Q(customer_firstname__istartswith=part)|Q(customer_lastname__istartswith=part)
                qs_params = qs_params | q if qs_params else q
            qs = qs.filter(qs_params)
        return qs
'''