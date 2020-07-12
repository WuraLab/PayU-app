from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from rest_framework.decorators import action
from rest_framework.authentication import TokenAuthentication
from .models import Profile
from .serializers import   UserRegistrationSerializers, ProfileSerializer, EditProfileSerilizer
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.parsers import FileUploadParser

#login was
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegistrationSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    # update - default method should be restricted
    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant Update your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # destroy - IsAuthenticated an isSelf
    def destroy(self, request,  *args, **kwargs):
        response = {'message': 'You cant delete Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    # retrieve - default method for all should be restricted,
    def list(self, request, *args, **kwargs):
        response = {'message': 'You cant  list or retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None, *args, **kwargs):
        response = {'message': 'You cant  list or retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)




class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (TokenAuthentication,)  #this option is used to authenticate a user, thus django can identify the token and its owner
    permission_classes = (IsAuthenticated,)

    # only set permissions for actions as update
    # remember to customise Create, delete, retrieve

    def update(self, request, *args, **kwargs):
        response = {'message': 'You cant edit your Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        response = {'message': 'You cant create Profile like that'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request,  *args, **kwargs):
        response = {'message': 'You cant delete Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        if request.user:
            user = request.user
        profile = Profile.objects.get(user=user.id)
        print(profile)
        serializer = ProfileSerializer(profile, many=False)
        response = {'message': 'User profile ', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None,  *args, **kwargs):
        response = {'message': 'You cant   retrieve users Profile like this'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


    # write a custom method that uses the authToken for access privileges
    @action(detail=True, methods=['POST'])
    def update_profile(self, request, pk=None,):
        if request.data :
            fetched_data =  request.data
            user = request.user
            try :
                 profile = Profile.objects.filter(user=user.id, id=pk )
                 profile.update(facebook_user=fetched_data['facebook_user'],
                                phone=fetched_data['phone'],
                                profile=request.FILES.get('profile'))
                 serializer = EditProfileSerilizer(profile, many=False)
                 response = {'message': 'User profile  Updated', 'result': serializer.data}
                 return Response(response, status=status.HTTP_200_OK)

            except IndexError :
                response = {'message': 'user profile does not exit'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'message': 'Nothing to update!'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)