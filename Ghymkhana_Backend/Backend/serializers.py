from rest_framework import serializers
from .models import meeting,ugSenator,pgSenator,facultyExecutivebodie,studentExecutivebodie,upcomingEvent
class meetingSerializer(serializers.ModelSerializer):
   class Meta:
      model= meeting
      fields='__all__'

class ugSenatorSerializer(serializers.ModelSerializer):
   class Meta:
      model= ugSenator
      fields='__all__'

class pgSenatorSerializer(serializers.ModelSerializer):
   class Meta:
      model= pgSenator
      fields='__all__'

class facultyExcecutiveSerializer(serializers.ModelSerializer):
   class Meta:
      model= facultyExecutivebodie
      fields='__all__'

class studentExcecutiveSerializer(serializers.ModelSerializer):
   class Meta:
      model= studentExecutivebodie
      fields='__all__'

class upComingSerializer(serializers.ModelSerializer):
   class Meta:
      model= upcomingEvent
      fields='__all__'
