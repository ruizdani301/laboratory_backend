from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from laboratory.models import Affiliate
from laboratory.serializer import AffiliateSerializer


class LaboratoryAffiliateApiView(APIView):

    def get(self, request):
        affiliate = Affiliate.objects.all()
        serializer = AffiliateSerializer(affiliate, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AffiliateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validatedData = serializer.validated_data
            affiliate = Affiliate(**validatedData)
            affiliate.save()
            serializerResponse = AffiliateSerializer(affiliate)
            return Response(serializerResponse.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboratoryAffiliateDetailApiView(APIView):
    """
        Class where the method needs a id to return or update
        any information
    """

    def getObject(self, id):
        """
            Validated if object exist
        """
        affiliate = get_object_or_404(Affiliate, id=id)
        return affiliate

    def get(self, request, id):
        affiliate = self.getObject(id)
        serializer = AffiliateSerializer(affiliate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """
            El deserializa y serializa al mismo tiempo?
        """
        affiliate = self.getObject(id)
        serializer = AffiliateSerializer(affiliate, data=request.data)
        if (serializer.is_valid()):
            affiliate = Affiliate(**serializer.validated_data)
            affiliate.id = id
            affiliate.save(update_fields=['name', 'age', 'email'])
            affiliate = Affiliate.objects.get(id=id)
            serializerRespose = AffiliateSerializer(affiliate)
            return Response(serializerRespose.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        affiliate = self.getObject(id)
        affiliate.delete()
        return Response(status=status.HTTP_200_OK)
