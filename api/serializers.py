from rest_framework import serializers

from usermanagement.models import Profile
from main.models import HighScores


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8, trim_whitespace=True, write_only=True)

    class Meta:
        model = Profile
        fields = ('id',
                  'url',
                  'username',
                  'email',
                  'password',
                  'groups',
                  'birthday',
                  'bio',
                  'followers')

    def create(self, validated_data):
        user = Profile.objects.create_user(validated_data['username'], validated_data['email'],
                                           password=validated_data['password'])
        return user

    def update(self, instance, validated_data):
        # TODO
        # user = Profile.objects.filter(id=instance.id).update()

        user = super().update(instance, validated_data)
        user.set_password(validated_data['password'])
        return user


class HighscoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighScores
        fields = ('username', 'score')
