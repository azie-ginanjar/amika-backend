from rest_framework import serializers

from material.models import Material, MaterialHistory


class MaterialHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialHistory
        fields = ("material", "quantity")

    def create(self, validated_data):
        material_history = super(MaterialHistorySerializer, self).create(validated_data)
        material_history.type = 'in'
        material_history.source = 'stock_in'
        material_history.save()

        return material_history


class MaterialSerializer(serializers.ModelSerializer):
    material_histories = MaterialHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = ("name", "material_histories")

    def create(self, validated_data):
        material = super(MaterialSerializer, self).create(validated_data)

        return material
