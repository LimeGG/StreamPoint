from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from streamers.models import AllStreamers
from lkusers.models import HisStreamers


class UserApi(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user_id = request.user.id
        name = request.data.get("streamerName")
        nameuser = request.user
        print(name, user_id, nameuser)
        try:
            streamers = AllStreamers.objects.get(name=name)
        except:
            return Response({"msg": "Этот стример пока не подключен к платформе"})
        try:
            update_points = HisStreamers.objects.get(streamers_id=streamers.id, user_id=user_id)
            update_points.points += 10
            update_points.save()
        except:
            HisStreamers.objects.create(
                user_id=user_id,
                streamers_id=streamers.id,
                points=10
            )
            sav = HisStreamers.objects.get(streamers_id=streamers.id, user_id=user_id)
            sav.save()
        point1 = HisStreamers.objects.get(streamers_id=streamers.id, user_id=user_id)
        point = point1.points
        print(point)
        return Response({"msg": point})



class TokenApi(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token, created = Token.objects.get_or_create(user=request.user)
        user = str(request.user)
        print(user)
        return Response({'token': token.key, "user": user})


class ValidateTokenApi(APIView):
    def post(self, request):
        token = request.data.get('token')
        try:
            Token.objects.get(key=token)
            return Response({'valid': True})
        except Token.DoesNotExist:
            return Response({'valid': False})


@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrf_token': request.COOKIES.get('csrftoken')})
