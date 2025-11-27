from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt

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
    try:
        pet = Pets.objects.get(pk=id)
    except Pets.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PetsSerializer(instance=pet, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def pets_delete(request, id: int):
    try:
        pet = Pets.objects.get(pk=id)
    except Pets.DoesNotExist:
        return Response({'Detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    pet.delete()
    return Response({'Detail': 'Registro eliminado'}, status=status.HTTP_200_OK)

@csrf_exempt
def pets_daily_dose(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            daily_dose = data.get('daily_dose', [])
            total_dose = 0
            message = ""
            for dose in daily_dose:
                total_dose += dose
                
            if total_dose < 100:
                message = "Tratamiento de baja intensidad"
            elif total_dose < 300:
                message = "Tratamiento moderado"
            else:
                message = "Tratamiento fuerte, seguir observación"
                
            return JsonResponse({"Dosis total": total_dose, "mensaje": message}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"Error": 'El dato requerido es una lista de dosis. Ej. ("daily_dose": [100,200,300])'}, status=400)
    
@csrf_exempt
def pets_weight_control(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            current_weight = data.get('current_weight')
            ideal_weight = data.get('ideal_weight')
            weight_diff = 0
            message = ""
            
            weight_diff = current_weight - ideal_weight
            
            if weight_diff > 0:
                message = "La mascota está por encima del peso ideal"
            elif weight_diff < 0:
                message = "La mascota está por debajo del peso ideal"
            else:
                message = "Peso ideal alcanzado"
                
            return JsonResponse({"Diferencia de pesos": weight_diff, "mensaje": message}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({"Error": 'El dato requerido es el peso ideal(kg) y el peso actual (kg). Ej. ("current_weight": 50, "ideal_weight": 60)'}, status=400)