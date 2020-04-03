from rest_framework import serializers
from employee.models import Employee, EmployeeType, Product, GENDER_STATUS


class EmployeeTypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)

    class Meta:
        model = EmployeeType
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Product
        fields = '__all__'


class JSONSerializerField(serializers.Field):
    """ Serializer for JSONField -- required to make field writable"""
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)
    address = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    gender = serializers.ChoiceField(choices=GENDER_STATUS, required=False)
    age = serializers.IntegerField(required=False)
    mobile = serializers.IntegerField(required=False)
    photo = serializers.ImageField(required=False)
    status = serializers.BooleanField(required=False)
    credit = serializers.FloatField(required=False)
    created_at = serializers.DateTimeField(required=False)
    # type = EmployeeTypeSerializer(required=False)
    type = serializers.SlugRelatedField(required=False, slug_field='name', read_only=True)
    product = ProductSerializer(required=False, many=True)
    meta_data = JSONSerializerField(required=False)
    production_user = serializers.ListField(child=serializers.CharField(), required=False)

    class Meta:
        model = Employee
        fields = '__all__'


