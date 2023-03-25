from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
#base class serializers . Serializer is class name so caps
   """serializes a name field for testing our APIView"""
   name = serializers.CharField(max_length=10)
