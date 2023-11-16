from rest_framework import serializers
from .models import Student

# validators
def starts_with_k(value):
    if value[0].lower() != 'k':
        raise serializers.ValidationError('name should start with k')
    

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100, validators=[starts_with_k])
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
    
    """
    creates a entry in databse when .save() method is called inside post method in views, this create() method is called, 
    object is created in database
    """
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    """
    updates a entry in databse when .save() method is called inside put method in views
    this create() method is called, object is created
    """
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.roll = validated_data.get('roll',instance.roll)
        instance.city = validated_data.get('city',instance.city)
        instance.save()
        return instance
    
    """
    Field level Validation when post request is called this method is executed when is_valid() is called in views 
    """
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Class is of full capacity')
        return value

    """
    Object level Validation(when we do validation for multiple field use object level validation) 
    here data is dictionary of inputs we get from users
    when post request is called this method is executed when is_valid() is called in views
    """
    def validate(self,data):
        roll_no = data.get('roll')
        city = data.get('city')
        name = data.get('name')
        if roll_no == 100 and name.lower() == 'krishna' and city.lower() == 'madhura':
            raise serializers.ValidationError('He is everything')
        return data

