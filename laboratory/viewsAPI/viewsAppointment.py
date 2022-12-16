from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from laboratory.models import Appointment
from laboratory.serializer import AppointmentSerializer


class LaboratoryAppointmentApiView(APIView):

    def get(self, request):
        appointment = Appointment.objects.all()
        serializer = AppointmentSerializer(appointment, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validatedData = serializer.validated_data
            appointment = Appointment(**validatedData)
            appointment.save()
            serializerResponse = AppointmentSerializer(
                                 appointment)
            return Response(serializerResponse.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboratoryAppointmentDetailApiView(APIView):
    """
        Class where the method needs a id to return or update
        any information
    """

    def getObject(self, id):
        """
            Validated if object exist
        """
        appointment = get_object_or_404(Appointment, id=id)
        return (appointment)

    def get(self, request, id):
        appointment = self.getObject(id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """
            El deserializa y serializa al mismo tiempo?
        """
        appointment = self.getObject(id)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if (serializer.is_valid()):
            appointment = Appointment(**serializer.validated_data)
            appointment.id = id
            appointment.save(update_fields=['date', 'hour', 'idTest',
                             'idAffiliate'])
            appointment = Appointment.objects.get(id=id)
            serializerRespose = AppointmentSerializer(appointment)
            return Response(serializerRespose, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        appointment = self.getObject(id)
        appointment.delete()
        return Response(status=status.HTTP_200_OK)
"""
    # Traer todas las citas de un afiliado   
    def getbyaffiliates(self, idAffiliate):
        affiliate = self.getObject(idAffiliate)
        affiliate.idAffiliate.all()
    # traer los afiliados con cita en una fecha especifica
    def getbydate(date):
        pass
"""
