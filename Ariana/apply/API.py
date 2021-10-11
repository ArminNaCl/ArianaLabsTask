from rest_framework import serializers
from .models import Apply

class ApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Apply
        fields= ['id','email','create_timestamp']
