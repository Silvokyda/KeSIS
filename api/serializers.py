from rest_framework import serializers

try:
    from home.models import Student, School, Subcounty, County
except:
    pass

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class SubcountySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcounty
        fields = '__all__'

class CountySerializer(serializers.ModelSerializer):
    subcounties = SubcountySerializer(many=True, read_only=True)
    
    class Meta:
        model = County
        fields = '__all__'
