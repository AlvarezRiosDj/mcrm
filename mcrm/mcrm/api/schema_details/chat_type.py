import strawberry
from strawberry import relay
import strawberry_django
from strawberry import auto
from typing import Optional, List

from strawberry_django.relay import ListConnectionWithTotalCount

from .operation_result import OperationResult
from ..models import ChatType


@strawberry_django.type(ChatType, fields='__all__')
class ChatTypeType(relay.Node):
    pass


@strawberry.type
class Query:
    chat_type_relay: ChatTypeType = relay.node()
    chat_type_relay_all: ListConnectionWithTotalCount[
        ChatTypeType
    ] = strawberry_django.connection()
    
@strawberry.type
class Mutation:
    
    @strawberry_django.mutation(handle_django_errors=True)
    def chat_type_relay_create(self, info,
        input_name: str                       
        ) -> ChatTypeType:
        pass
    
    @strawberry_django.mutation(handle_django_errors=True)
    def chat_type_relay_update(self, info,
        id: str,
        input_name: Optional[str] = None,                       
        ) -> OperationResult:
        
        node = relay.from_global_id(id)
        node = relay.from_base64(id)
        
        chat_type = ChatType.objects.get(id=node.id)
        
        if input_name:
            chat_type.name = input_name
            chat_type.save()
            
        return OperationResult(success=True, message="Chat type updated successfully")
        
    
    