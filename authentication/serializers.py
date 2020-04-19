from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from user.serializers import UserDetailsSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': UserDetailsSerializer(self.user).data})
        # and everything else you want to send in the response
        return data