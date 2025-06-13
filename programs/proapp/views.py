from django.shortcuts import render
from rest_framework.response import Response
from.serializers import MessageForm
from.models import Message_tbl
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def messageview(request):
    obj=Message_tbl.objects.all()
    form=MessageForm(obj,many=True)
    return Response(form.data)

@api_view(['GET'])
def readone(request,pk):
    obb=Message_tbl.objects.get(id=pk)
    form=MessageForm(obb,many=False)
    return Response(form.data)

@api_view(['GET'])
def PostData(request):
    form=MessageForm(data=request.data)
    if form.is_valid():
        form.save()
    return Response(form.data)

@api_view(['PUT'])
def UpdateData(request,pk):
    obb=Message_tbl.objects.get(id=pk)
    form=MessageForm(instance=obb,dat=request.data)
    if form.is_valid():
        form.save()
    return Response(form.data)

@api_view(['PATCH'])
def UpdateOne(request,pk):
    obb=Message_tbl.objects.get(id=pk)
    one={'fnm':request.data.get('fnm')}
    form=MessageForm(instance=obb,data=one,partial=True)
    if form.is_valid():
        form.save()
    return Response(form.data)

@api_view(['DELETE'])
def DeleteData(request,pk):
    obb=Message_tbl.objects.get(id=pk)
    obb.delete()
    return Response("Item Deleted Successfully")
