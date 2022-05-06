import imp
from unicodedata import category
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .serializers import *
from .models import *

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class Index(generics.GenericAPIView):
    def get(self, request, name):
    #     cred = credentials.Certificate(r"C:\Users\user\Desktop\hackathon-348110-firebase-adminsdk-72jye-b6876c5045.json")
    #     fb_url = 'https://hackathon-348110-default-rtdb.asia-southeast1.firebasedatabase.app/test'
    #     firebase_admin.initialize_app(cred, {'databaseURL': fb_url})
    #     ref = db.reference('/bestcomputers')

    #     bestcomputers = ref.get()
    #     newlist=[]
    #     for key, value in bestcomputers.items():
    #         BestComputers.objects.create(**value)
        

        print(request.META['REMOTE_ADDR'])
        queryBest = BestComputers.objects.filter(name__icontains = name)
        queryHitech = HiTech.objects.filter(name__icontains = name)
        queryNewTech = NewTech.objects.filter(name__icontains = name)

        serializerBest = AllSerializer(queryBest, many = True)
        serializerHitech = AllSerializer(queryHitech, many = True)
        serializerNewtech = AllSerializer(queryNewTech, many = True)

        return Response({'BestComputers':serializerBest.data,
                         'HiTech':serializerHitech.data,
                         'NewTech':serializerNewtech.data})
