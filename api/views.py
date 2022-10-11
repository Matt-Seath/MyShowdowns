from rest_framework.response import Response
from rest_framework.decorators import api_view
from core.models import Battle
from core.serializers import BattleSerializer

# Create your views here.

@api_view(["GET"])
def get_battles(request):
    queryset = Battle.objects.all()
    serializer = BattleSerializer(queryset, many=True)
    return Response(serializer.data)