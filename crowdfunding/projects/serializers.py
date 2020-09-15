from rest_framework import serializers 
from .models import Project, Pledge

class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    amount = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    supporter_id = serializers.IntegerField()
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)



class ProjectSerializer(serializers.Serializer):
    # looking at list of projects
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=None) # no text fields in serializer
    goal = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    # pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        return Project.objects.create(**validated_data) # get project from earlier, use global method create and creates new project

class ProjectDetailSerializer(ProjectSerializer):
    # when just looking at one project
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
        # update variable with new value, if no new given - use default which is existing variable

class PledgeDetailSerializer(PledgeSerializer):

    # where any additional fields go

    def update(self, instance, validated_data):

        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.save()
        return instance