from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from pets.models import Pets
from pets.serializers.pets import PetsSerializer

@api_view(["GET"])
def pets_get_list(request):
    qs = Pets.objects.all()
    q = (request.query_params.get("q") or "").strip()
    if q:
        qs = qs.filter(Q(name__icontains=q))
    data = PetsSerializer(qs, many=True).data
    return Response(data, status=status.HTTP_200_OK)

@api_view(["POST"])
def pets_post_create(request):
    serializer = PetsSerializer(data=request.data)
    if serializer.is_valid():
        pet = serializer.save()
        return Response(PetsSerializer(pet).data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def pets_get_by_id(request, id: int):
    try:
        pet = Pets.objects.get(pk=id)
        print(pet.id)
    except Pets.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    return Response(PetsSerializer(pet).data, status=status.HTTP_200_OK)

@api_view(["PUT"])
def pets_put(request, id: int):
    print("Ingresa")
    
    try:
        pet = Pets.objects.get(pk=id)
    except Pets.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PetsSerializer(isinstance=pet, data=request.data)
    if serializer.is_valid:
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def pets_delete(request, id: int):
    print("Ingresa")
    try:
        pet = Pets.objects.get(pk=id)
    except Pets.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    pet.delete()
    return Response({'Detail': 'Registro eliminado'}, status=status.HTTP_200_OK)