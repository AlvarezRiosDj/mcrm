from django.db import models

# Create your models here.
from .model_details.profile import Profile
from .model_details.client_user import ClientUser
from .model_details.chat_type import ChatType
from .model_details.chat_integration import ChatIntegration
from .model_details.chat_conversation import ChatConversation
from .model_details.chat_message import ChatMessage











from django.db.models import Lookup
from django.db.models.fields import Field


@Field.register_lookup
class Like(Lookup):
    lookup_name = 'like'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
      
        params[0] = ('%' + '%'.join(params[0].split(' ')) + '%').lower()
        
        return 'LOWER(%s) LIKE %s' % (lhs, rhs), params
