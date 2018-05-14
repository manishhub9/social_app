 from django.template.loader import get_template 
 from django.template import Context
 import pdfkit

 template = get_template("htmltopdf.html")
 context = Context({"data": data})  
 html = template.render(context)  
 pdfkit.from_string(html, 'out.pdf')
 pdf = open("out.pdf")
 response = HttpResponse(pdf.read(), content_type='application/pdf')  
 response['Content-Disposition'] = 'attachment; filename=output.pdf'
 pdf.close()
 os.remove("out.pdf")  
 return response  
