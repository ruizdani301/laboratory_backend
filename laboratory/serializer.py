from rest_framework import serializers
from laboratory.models import Test, Affiliate, Appointment

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['id', 'name', 'description']

class AffiliateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Affiliate
        fields = ['id', 'name', 'age', 'email']

class AppointmentSerializer(serializers.ModelSerializer):
   # idTest = TestSerializer()
   # idAffiliate = AffiliateSerializer()
    class Meta:
        
        model = Appointment
        #fields = ['id', 'date', 'hour', 'idTest', 'idAffiliate']

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'date': instance.date,
            'hour': instance.hour,
            'idTest': {'id': instance.idTest.id,
                       'name':instance.idTest.name,
                       'description':instance.idTest.description
                       },
            'idAffiliate': {'id': instance.idAffiliate.id,
                            'name':instance.idAffiliate.name,
                            'age': instance.idAffiliate.age,
                            'email': instance.idAffiliate.email
                            },
        }
# Serializar la relación
#  idTest = serializers.StringRelatedField() en este caso
#  me devuelve un solo string.
