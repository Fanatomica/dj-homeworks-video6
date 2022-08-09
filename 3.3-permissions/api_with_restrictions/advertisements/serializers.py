from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'draft', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        data["creator"] = self.context["request"].user
        if data['status'] == 'OPEN':
            statuses = Advertisement.objects.filter(creator=data["creator"])
            k = 0
            for stat in statuses:
                if stat.status == "OPEN":
                    k += 1
            if k == 10:
                raise serializers.ValidationError("Количество открытых объявлений 10,"
                                                    "удалите одно объявление или измените его статус на CLOSED")
            else: return data
        return data
