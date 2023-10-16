from django.contrib.auth.models import User
from rest_framework import serializers
import re

class UserSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True)

  def validate_password(self, password):
    #se tem maiúscula
    if not re.search('[A-Z]', password):
      raise serializers.ValidationError("Pelo menos uma maiúscula")
    #se tem minúscula
    if not re.search('[a-z]', password):
      raise serializers.ValidationError("Pelo menos uma minúscula")
    if not re.search('[0-9]', password):
      raise serializers.ValidationError("Pelo menos um número")
    if not re.search('[^A-Za-z0-9]', password):
      raise serializers.ValidationError("Pelo menos um símbolo especial")
    if len(password) < 8:
      raise serializers.ValidationError("Comprimento pelo menos 8")
    return password

  class Meta:
    model = User
    fields = ['id', 'username', 'email', 'password']