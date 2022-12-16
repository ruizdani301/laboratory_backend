from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from laboratory.models import Test
from laboratory.serializer import TestSerializer


class LaboratoryTestApiView(APIView):
    """
        contains functions that do not require a parameter
    """

    def get(self, request):
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validatedData = serializer.validated_data
            test = Test(**validatedData)
            test.save()
            serializerResponse = TestSerializer(test)
            return Response(serializerResponse.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LaboratoryTestDetailApiView(APIView):
    """
        Class where the method needs a id to return or update
        any information
    """

    def getObject(self, id):
        """
            Validated if object exist
        """
        test = get_object_or_404(Test, id=id)
        return test

    def get(self, request, id):
        test = self.getObject(id)
        serializer = TestSerializer(test)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        """
            El deserializa y serializa al mismo tiempo?
        """
        test = self.getObject(id)
        serializer = TestSerializer(test, data=request.data)
        if (serializer.is_valid()):
            test = Test(**serializer.validated_data)
            test.id = id
            test.save(update_fields=['name', 'description'])
            test = Test.objects.get(id=id)
            serializerRespose = TestSerializer(test)
            return Response(serializerRespose.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        test = self.getObject(id)
        test.delete()
        return Response(status=status.HTTP_200_OK)
