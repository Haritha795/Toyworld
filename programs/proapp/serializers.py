from rest_framework import serializers
from.models import Message_tbl

class MessageForm(serializers.ModelSerializer):
    class Meta:
        model=Message_tbl
        fields='__all__'



    
    