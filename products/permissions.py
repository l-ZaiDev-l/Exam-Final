from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
    Permission personnalisée :
    - Lecture seule pour tout le monde (GET, HEAD, OPTIONS)
    - Écriture seulement pour le propriétaire de l'objet
    """

    def has_object_permission(self, request, view, obj):
        # Les méthodes sécurisées (GET, HEAD, OPTIONS) sont autorisées
        if request.method in SAFE_METHODS:
            return True
        
        # Pour les autres méthodes (PUT, PATCH, DELETE), vérifier la propriété
        return getattr(obj, "user_id", None) == getattr(request.user, "id", None)
