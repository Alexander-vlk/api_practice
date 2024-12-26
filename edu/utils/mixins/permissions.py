class OwnerMixin:
    """Миксин для фильтрации по пользователю"""
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)
    

class OwnerEditMixin:
    """Миксин для установки владельца"""
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
