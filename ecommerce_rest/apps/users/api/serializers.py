from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from apps.users.models import User

# class UserTokenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'name', 'last_name' )

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name' )

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    # cuando quieres registrar o actualizar
    class Meta:
        model = User
        # fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
        fields = '__all__'

    def create(self,validate_data):
        user = User(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ( 'username', 'email', 'name', 'last_name' )
   
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name'] 

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return {
            'id': representation['id'],
            'name': representation['name'],
            'username': representation['username'],
            'email': representation['email'],
            # 'password': representation['password'],
        }

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)
    
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Las contraseñas no coinciden')
        return data
    

class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    # valiadaciones solo con el campo name
    def validate_name(self,value):
        if len(value) < 5:
            raise serializers.ValidationError('Name must be at least 5 characters long.')
        
        # print(self.context['email'])
        return value

    # validaciones solo con el campo email
    def validate_email(self, value):
        if value == '':
            raise serializers.ValidationError('Email cannot be empty.')
        # elif self.validate_name(self.context['name']) in value:
        #     raise serializers.ValidationError('Name cannot be in email.')
        return value

    # validaciones con todos los campos disponibles
    def validate(self,data):
            
            return data
        
    def create(self, validated_data):
        return User.objects.create(**validated_data)
        # print(validated_data)
        # return validated_data
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    def save(self):
        print(self.validated_data)
        send_email()

