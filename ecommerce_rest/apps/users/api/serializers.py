from rest_framework import serializers
from apps.users.models import User

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name' )


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

    def update(self,instance, validate_data):
        update_user = super().update(instance,validated_data)
        update_user.set_password(validate_data['password'])
        update_user.save()
        return update_user


    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    # print(instance)
    # print(representation)

    # return {
    #     'id': representation['id'],
    #     'username': representation['username'],
    #     'email': representation['email'],

    #     }
    

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': representation['id'],
            'username': representation['username'],
            'email': representation['email'],
            'password': representation['password'],
        }



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

