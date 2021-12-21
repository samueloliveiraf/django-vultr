from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

from django.views.generic import View

from .models import Sale
from company.models import Company
from datetime import datetime


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePDF(View):
    def get(self, request, id_sale, *args, **kwargs):
        template = get_template('product/pdf.html')
        sales = Sale.objects.filter(
            user=request.user,
            id=id_sale,
        )

        companys = Company.objects.filter(
            user=request.user
        )
    
        myDate = datetime.now()
        formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

        context = { 
            'sales': sales, 
            'companys': companys,
            'myDate': formatedDate
        }

        html = template.render(context)
        pdf = render_to_pdf('product/pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341232")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")

            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response

        return HttpResponse("Not found")
