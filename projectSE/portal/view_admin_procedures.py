from django.views import generic
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
import csv, io
from .models import Procedure
from django.urls import reverse_lazy
from .views_admin_users import AdminCheck, admin_check

##Classe che restituisce il model alla page delle procedure 
class ProcedureView(AdminCheck, generic.ListView):
    model = Procedure
    template_name = 'portal/admin/procedures.html'
    context_object_name = 'procedure_list'

    def get_queryset(self):
        return super().get_queryset().order_by('procedureName')

#Creazione procedure tramite file
@user_passes_test(admin_check)
def create_procedure(request):
    template = 'portal/admin/create_procedures.html'

    prompt = {'order': 'Scegli un file .csv con il seguente formato: NomeProcedura,Descrizione'}

    if request.method == 'GET':
        return render(request, template, prompt)
    else:
        try:
            csv_file = request.FILES['file']
        except :
            prompt = {'order': 'Seleziona prima un file .csv da caricare!'}
            return render(request, template, prompt)
        else:
            if not csv_file.name.endswith('.csv'):
                prompt = {'order': 'Formato errato!'}
                return render(request, template, prompt)
            else:
                data_set = csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                num_procedure = 0
                new_procedures = []
                for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                    try:
                        procedure, created = Procedure.objects.update_or_create(
                            procedureName=column[0],
                            procedureDescription=column[1],
                        )
                        if created:
                            num_procedure = num_procedure+1
                            new_procedures.append(procedure)
                    except:
                        pass
                if num_procedure== 0:
                    print(num_procedure)
                    prompt = {'order': 'Procedure già presenti del Database.'}
                    return render(request, template, prompt)
                else:
                    context = { 'new_procedures': new_procedures,
                                'num_procedure': num_procedure
                                }
                    return render(request, template, context)

#Cancellazione di una procedura
class ProcedureDeleteView(AdminCheck, generic.DeleteView):
    model = Procedure
    success_url = reverse_lazy('systemadministrator_procedures')

#Query al db per recuperare le procedure ordinate per nome
class OwnerMixin(object):

    def get_queryset(self):
        return super().get_queryset().order_by('procedureName')

#Definizione degli attributi del modello da restituire
class OwnerProcedureMixin(OwnerMixin):
    model = Procedure
    fields = [
        'procedureName',
        'procedureDescription',
    ]

    success_url = reverse_lazy('systemadministrator_procedures')

#Definizione del template per la modifica della procedura
class OwnerProcedureEditMixin(OwnerProcedureMixin):
    template_name = 'portal/admin/modify_procedure_form.html'

#Definizione degli attributi da modificare nel template fornito
class ProcedureEditView(OwnerProcedureEditMixin, AdminCheck, generic.UpdateView):
    fields = [
        'procedureName',
        'procedureDescription',
    ]

#Definizione degli attributi per la creazione di una procedura tramite il template fornito
class ProcedureCreateView(OwnerProcedureEditMixin, AdminCheck, generic.CreateView):
    fields = [
        'procedureName',
        'procedureDescription',
    ]
