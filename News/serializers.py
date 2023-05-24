from rest_framework import serializers

# News Serializer
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'newname', 'image', 'title')

# RegisterNew Serializer
class RegisterNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'newname', 'image', 'title')

    def createNew(self, validated_data):
        user = User.objects.create_user(validated_data['newname'], \
                                        validated_data['image'], validated_data['title'])

        return new