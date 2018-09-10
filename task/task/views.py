from annoying.decorators import render_to

# Create your views here.
from django.db.models import Sum
from django.db.models.functions import Coalesce
from django.views.generic import ListView, DetailView

from task.models import Site


class SitesList(ListView):
    model = Site
    template_name = "sites.html"


class SiteDetail(DetailView):
    model = Site
    template_name = "site_detail.html"

    def get_queryset(self):
        return super().get_queryset().prefetch_related('records')


@render_to("summary.html")
def summary(request):
    """
    Returns sum for a_value and b_value of Record instances grouped by Site
    :param request:
    :return:
    """
    data = {'sites': [], 'sum': True}
    sites = Site.objects.all().prefetch_related('records')
    # Aggregation in python
    for site in sites:
        site_data = {'title': site.title, 'a_value': 0, 'b_value': 0}
        for record in site.records.all():
            site_data['a_value'] += record.a_value
            site_data['b_value'] += record.b_value
        data['sites'].append(site_data)

    # Alternative way to do it via ORM. Using Coalesce to set default sum to 0.
    # data['sites'] = sites.annotate(
    #     a_value=Coalesce(Sum('records__a_value'), 0),
    #     b_value=Coalesce(Sum('records__b_value'), 0)
    # ).values('title', 'a_value', 'b_value')
    return data


@render_to("summary.html")
def summary_average(request):
    """
    Returns averages for a_value and b_value of Record instances grouped by Site
    :param request:
    :return:
    """
    data = {
        'sites': None,
        'avg': True
    }
    sites = Site.objects.raw(
        """
        SELECT ts.id, ts.title, COALESCE(AVG(tr.a_value), 0) AS a_value, COALESCE(AVG(tr.b_value), 0) AS b_value 
        FROM task_site ts LEFT JOIN task_record tr ON (ts.id = tr.site_id) 
        GROUP BY ts.id
        """
    )
    data['sites'] = sites
    return data
