from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class OwnerMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Миксин для фильтрации по пользователю"""
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)
    

class OwnerEditMixin(LoginRequiredMixin, PermissionRequiredMixin):
    """Миксин для установки владельца"""
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
