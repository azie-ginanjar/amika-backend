from django.contrib.auth import get_user_model
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import Role
from user.serializers import UserSerializer, UserDetailsSerializer

User = get_user_model()


class UserView(generics.ListAPIView):
    queryset = User.objects.all().filter(is_active=True)
    # permission_classes = (AdminRequired, )
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    queryset = User.objects.all().filter(is_active=True)
    # permission_classes = (AdminRequired, )
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        if request.data['role'] not in [Role.CUSTOMER_SERVICE, Role.PEMOTONG, Role.PENJAHIT]:
            return Response(
                data={"error": "invalid role"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(
            password=request.data["password"],
            username=request.data["username"],
            email=request.data["email"],
            name=request.data["name"],
            role=request.data["role"]
        )

        user.set_password(request.data['password'])
        user.save()

        return Response(
            data=UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def put(self, request, *args, **kwargs):
        if request.user.is_authenticated:  # is_superuser or (request.user.is_authenticated and request.user.pk == kwargs["pk"]):
            try:
                user = self.queryset.get(pk=kwargs["pk"])
                serializer = UserDetailsSerializer()
                updated_user = serializer.update(user, request.data)
                return Response(UserDetailsSerializer(updated_user).data)
            except User.DoesNotExist:
                return Response(
                    data={
                        "message": "User with id: {} does not exist".format(kwargs["pk"])
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                data={
                    "message": "Unauthorized"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

    def destroy(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                user = self.queryset.get(pk=kwargs["pk"])
                user.is_active = False
                user.save()
                return Response(
                    data={
                        "status": "success"
                    }
                )
            except User.DoesNotExist:
                return Response(
                    data={
                        "message": "User with id: {} does not exist".format(kwargs["pk"])
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                data={
                    "message": "Unauthorized"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
