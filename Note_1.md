##模型
* 职业类型 jon_type
* 职业名称 job_name
* 职业城市 job_city
* 职业职责 job_reponsibility
* 职位要求 job_requirement
* 创建者   creator
* 创建日期 create_date
* 修改时间 modify_date

##增加默认值
> 设置参数'default' 

##增加模型管理类
admin.py
list_display: 展示字段
exclude: 隐藏字段
save_model():保存模型前做一些操作

##增加模板
1. 新建templates文件夹  
2. 定义基础模板（用于子模板继承）eg. Base.html
   > 一般头部和底部都是公共模块，定义在基础模板，其他模板继承该模板，可直接公用一个页面头尾  
   
   > 语法： {% extends 'base.html'%}
   
##在views.py中定义页面视图函数  
**objects**: Model和数据库进行查询的接口
> 获取所有职位：jobs.objects.order_by('job_type') 类名.objects.方法    

>template = loader.get_template('*.html')  
> 
```buildoutcfg
def joblist(request):
    job_list = Job.objects.order_by('job_type')
    template = loader.get_template('job_list.html')
    content = {"job_list": job_list}
    for job in job_list:
        job.city_name = job_cities[job.job_city][1]
        job.type_name = job_types[job.job_type][1]
    return HttpResponse(template.render(content))
```
##在应用urls.py中添加路径解析
```buildoutcfg
urlpatterns = [
    url('joblist/', views.joblist, name="job_list")
]
```
##在项目urls.py中添加路径解析
```buildoutcfg
urlpatterns = [
    url(r'^job/', include('jobs.urls')),
    path('admin/', admin.site.urls),
]
```
> 访问的路径为 job/joblist/  

##路径传递参数
1. 传统 '？'传递
    > 通过request.GET.get()获取参数值
   
2. 正则匹配
    > url(r'detail/(?P<job_id>\d+)/$', views.detail, name="detail"),